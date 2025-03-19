import requests

from rich import print

from models import Character, Planet, Film


class StarWarsAPIClient:
    """Star Wars API Client"""

    BASE_URL = 'https://swapi.dev/api/'

    def __init__(self):
        self.session = requests.Session()

    def _get(self, endpoint: str):
        url = f'{self.BASE_URL}{endpoint}'

        response = self.session.get(url, timeout=5)
        response.raise_for_status()

        return response.json()


    def get_character_by_id(self, character_id: int) -> Character:
        response = self._get(f'people/{character_id}/')

        return Character(**response)


    def get_planet_by_id(self, planet_id: int) -> Planet:
        response = self._get(f'planets/{planet_id}/')

        return Planet(**response)

    def get_film_by_id(self, planet_id: int) -> Film:
        response = self._get(f'films/{planet_id}/')

        return Film(**response)


    def search_character_by_name(self, name: str) -> Character:
        response = self._get(f'people/?search={name}')

        return Character(**response['results'][0])


    def get_characters_in_film(self, film_id: int) -> list[Character]:
        film = self.get_film_by_id(film_id)

        characters: list[Character] = []

        for character_url in film.characters:
            character_id = int(character_url.split('/')[-2])
            character = self.get_character_by_id(character_id)

            characters.append(character)


        return characters


    def get_films_by_character(self, character_id: int) -> list[Film]:
        character = self.get_character_by_id(character_id)

        films: list[Film] = []

        for film_url in character.films:
            film_id = int(film_url.split('/')[-2])
            film = self.get_film_by_id(film_id)

            films.append(film)

        return films
