import requests

from rich import print

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

        response = self.session.get(url, timeout=5)
        response.raise_for_status()

        return response.json()


    def get_character_by_id(self, character_id: int) -> Character:
        """
        Get a character by ID.
        """

        response = self._get(f'people/{character_id}/')

        return Character(**response)


    def get_planet_by_id(self, planet_id: int) -> Planet:
        """
        Get a planet by ID.
        """

        response = self._get(f'planets/{planet_id}/')

        return Planet(**response)

    def get_film_by_id(self, planet_id: int) -> Film:
        """
        Get a film by ID.
        """

        response = self._get(f'films/{planet_id}/')

        return Film(**response)


    def search_character_by_name(self, name: str) -> Character:
        """
        Search for a character by name.
        """

        response = self._get(f'people/?search={name}')

        return Character(**response['results'][0])


    def get_characters_in_film(self, film_id: int) -> list[Character]:
        """
        Get all characters in a film.
        """

        film = self.get_film_by_id(film_id)

        characters: list[Character] = []

        for character_url in film.characters:
            character_id = int(character_url.split('/')[-2])
            character = self.get_character_by_id(character_id)

            characters.append(character)


        return characters


    def get_films_by_character(self, character_id: int) -> list[Film]:
        """
        Get all films a character has appeared in.
        """

        character = self.get_character_by_id(character_id)

        films: list[Film] = []

        for film_url in character.films:
            film_id = int(film_url.split('/')[-2])
            film = self.get_film_by_id(film_id)

            films.append(film)

        return films
