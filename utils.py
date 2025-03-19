def get_id_from_url(url: str) -> int | None:
    """
    Get the ID from a URL in the form: https://swapi.dev/api/characters/1/

    Returns None if the URL is invalid.
    """

    value = url.split('/')[-2]

    try:
        return int(value)
    except ValueError:
        return None
