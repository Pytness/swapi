from dataclasses import dataclass

from utils import get_id_from_url

@dataclass
class Record:
    created: str
    edited: str
    url: str

    def id(self) -> int:
        return get_id_from_url(self.url)

@dataclass
class Character(Record):
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str

    homeworld: str
    films: list[str]
    species: list[str]
    vehicles: list[str]
    starships: list[str]

    def homeworld_id(self) -> int:
        return get_id_from_url(self.homeworld)

    def film_ids(self) -> list[int]:
        return [get_id_from_url(url) for url in self.films]

    def species_ids(self) -> list[int]:
        return [get_id_from_url(url) for url in self.species]

    def vehicle_ids(self) -> list[int]:
        return [get_id_from_url(url) for url in self.vehicles]

    def starship_ids(self) -> list[int]:
        return [get_id_from_url(url) for url in self.starships]


@dataclass
class Planet(Record):
    name: str
    rotation_period: str
    orbital_period: str
    diameter: str
    climate: str
    gravity: str
    terrain: str
    surface_water: str
    population: str
    residents: list[str]
    films: list[str]

    def resident_ids(self) -> list[int]:
        return [get_id_from_url(url) for url in self.residents]

    def film_ids(self) -> list[int]:
        return [get_id_from_url(url) for url in self.films]


@dataclass
class Film(Record):
    title: str
    episode_id: str
    opening_crawl: str
    director: str
    producer: str
    release_date: str

    characters: list[str]
    planets: list[str]
    starships: str
    vehicles: list[str]
    species: list[str]

    def character_ids(self) -> list[int]:
        return [get_id_from_url(url) for url in self.characters]

    def planet_ids(self) -> list[int]:
        return [get_id_from_url(url) for url in self.planets]

    def starship_ids(self) -> list[int]:
        return [get_id_from_url(url) for url in self.starships]

    def vehicle_ids(self) -> list[int]:
        return [get_id_from_url(url) for url in self.vehicles]

    def species_ids(self) -> list[int]:
        return [get_id_from_url(url) for url in self.species]
