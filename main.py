import sys


from api import StarWarsAPIClient


if __name__ == '__main__':
    """
    Example usage of the StarWarsAPIClient.
    """

    client = StarWarsAPIClient()

    luke = client.search_characters_by_name("Luke Skywalker")

    if not luke:
        print("Error: Luke Skywalker not found.")
        sys.exit(1)

    luke = luke[0]

    print(f"Name: {luke.name}")
    print(f"Height: {luke.height}")

    homeworld = client.get_planet_by_id(luke.homeworld_id())

    if not homeworld:
        print("Error: Homeworld not found.")
        sys.exit(1)

    print(f"Homeworld: {homeworld.name}")


    films = client.get_films_by_character_id(luke.id())

    if not films:
        print("Error: Films not found.")
        sys.exit(1)

    print("Films:")
    for film in films:
        print(f" - {film.title}")
