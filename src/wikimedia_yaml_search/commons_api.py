import requests

def search_commons_images(query, limit=4):
    """
    Queries Wikimedia Commons for image files matching the search term.
    Returns the JSON response containing image URLs.
    """
    search_url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": query,
        "gsrlimit": limit,
        "gsrnamespace": 6,
        "prop": "imageinfo",
        "iiprop": "url"
    }
    response = requests.get(search_url, params=params)
    return response.json()
