from dataclasses import dataclass


@dataclass
class Record:
    created: str
    edited: str
    url: str

    def id(self) -> int:
        return int(self.url.split('/')[-2])

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
