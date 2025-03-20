import unittest
from api import StarWarsAPIClient,  Character, Planet, Film


class TestStarWarsAPIClient(unittest.TestCase):
    """
    Unit tests for StarWarsAPIClient.
    """

    def setUp(self):
        self.client = StarWarsAPIClient()

    def test_get_character_by_id_success(self):
        character = self.client.get_character_by_id(1)

        self.assertIsInstance(character, Character)
        self.assertEqual(character.name, "Luke Skywalker")

    def test_get_character_by_id_failed(self):
        character = self.client.get_character_by_id(-1)
        self.assertIsNone(character)

    def test_get_planet_by_id_success(self):
        planet = self.client.get_planet_by_id(1)

        self.assertIsInstance(planet, Planet)
        self.assertEqual(planet.name, "Tatooine")

    def test_get_planet_by_id_failed(self):
        planet = self.client.get_planet_by_id(-1)

        self.assertIsNone(planet)

    def test_get_film_by_id_success(self):
        film = self.client.get_film_by_id(1)

        self.assertIsInstance(film, Film)
        self.assertEqual(film.title, "A New Hope")

    def test_get_film_by_id_failed(self):
        film = self.client.get_film_by_id(-1)

        self.assertIsNone(film)

    def test_search_characters_by_name_found(self):
        characters = self.client.search_characters_by_name("Luke")

        self.assertIsInstance(characters, list)
        self.assertIsInstance(characters[0], Character)
        self.assertEqual(characters[0].name, "Luke Skywalker")

    def test_search_characters_by_name_not_found(self):
        characters = self.client.search_characters_by_name("Invalid Name")

        self.assertEqual(len(characters), 0)

    def test_get_characters_in_film_success(self):
        characters = self.client.get_characters_by_film_id(1)

        self.assertIsInstance(characters, list)
        self.assertIsInstance(characters[0], Character)
        self.assertEqual(characters[0].name, "Luke Skywalker")

    def test_get_characters_in_film_failed(self):
        characters = self.client.get_characters_by_film_id(-1)

        self.assertIsNone(characters)

    def test_get_films_by_character_id_success(self):
        films = self.client.get_films_by_character_id(1)

        self.assertIsInstance(films, list)
        self.assertIsInstance(films[0], Film)
        self.assertEqual(films[0].title, "A New Hope")

    def test_get_films_by_character_id_failed(self):
        films = self.client.get_films_by_character_id(-1)

        self.assertIsNone(films)


if __name__ == "__main__":
    unittest.main()
