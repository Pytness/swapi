import requests

from models import Character, Planet, Film


class StarWarsAPIClient:
    """Star Wars API Client"""

    BASE_URL = 'https://swapi.dev/api/'

    def __init__(self):
        self.session = requests.Session()

    def _get(self, endpoint: str):
        """
        Handle GET requests to the Star Wars API.
        """

        url = f'{self.BASE_URL}{endpoint}'

        try:
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:

            if e.response.status_code == 404:
                return None

            raise e


    def get_character_by_id(self, character_id: int) -> Character | None:
        """
        Get a character by ID.

        Returns None if the character is not found.
        """

        response = self._get(f'people/{character_id}/')

        if response is None:
            return None

        return Character(**response)


    def get_planet_by_id(self, planet_id: int) -> Planet | None:
        """
        Get a planet by ID.

        Returns None if the planet is not found.
        """

        response = self._get(f'planets/{planet_id}/')

        if response is None:
            return None

        return Planet(**response)


    def get_film_by_id(self, film_id: int) -> Film | None:
        """
        Get a film by ID.

        Returns None if the film is not found.
        """

        response = self._get(f'films/{film_id}/')

        if response is None:
            return None

        return Film(**response)


    def search_characters_by_name(self, name: str) -> list[Character] | None:
        """
        Search for a characters by name.
        """

        response = self._get(f'people/?search={name}')

        # `response` should never be None, but we'll check just in case.
        if response is None:
            raise ValueError('Invalid response from API')

        return [Character(**result) for result in response['results']]


    def get_characters_by_film_id(self, film_id: int) -> list[Character] | None:
        """
        Get all characters in a film.

        Returns None if the film is not found.
        """

        film = self.get_film_by_id(film_id)

        if film is None:
            return None

        characters: list[Character] = []

        for character_url in film.characters:
            character_id = int(character_url.split('/')[-2])
            character = self.get_character_by_id(character_id)

            characters.append(character)

        return characters


    def get_films_by_character_id(self, character_id: int) -> list[Film] | None:
        """
        Get all films a character has appeared in.

        Retuns None if the character is not found.
        """

        character = self.get_character_by_id(character_id)

        if character is None:
            return None

        films: list[Film] = []

        for film_url in character.films:
            film_id = int(film_url.split('/')[-2])
            film = self.get_film_by_id(film_id)

            films.append(film)

        return films
