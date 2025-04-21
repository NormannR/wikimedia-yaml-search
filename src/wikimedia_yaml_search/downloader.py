import requests
import time
from pathlib import Path
import yaml
from datetime import datetime
import mimetypes

from wikimedia_yaml_search.commons_api import search_commons_images

def dl_commons_images(filename, limit=2):
    """
    Loads search terms from a YAML file and downloads image results from Wikimedia Commons.
    Creates timestamped output folders organized by category and item.
    """
    # Set up HTTP headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    with open(filename, encoding="utf-8") as f:
        data = yaml.safe_load(f)    
    # Create a timestamped folder to store all downloads
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = f"search_{timestamp}"
    main_path = Path(folder_name)
    main_path.mkdir(parents=True, exist_ok=True)
    # Loop through categories and items in the YAML file
    for category in data.keys():
        print(f"Catégorie {category} : Traitement en cours ...")
        category_path = main_path / category
        category_path.mkdir(parents=True, exist_ok=True)
        # Loop over each query within the category
        for query in data[category]:
            item_path = category_path / query
            item_path.mkdir(parents=True, exist_ok=True)
            print(f"   Requête {query} : Traitement en cours ...")

            # Query Wikimedia Commons
            response = search_commons_images(query, limit=limit)
            pages = response.get("query")
            if not pages:
                print(f"   Requête {query} : Aucun résultat obtenu.")
            else:
                # Loop over image results
                for page in pages.get("pages").values():
                    imageinfo = page.get("imageinfo")
                    if not imageinfo:
                        print(f"   Requête {query} : Absence d'URL sur un des résultats.")
                    else:
                        # Download the image using its URL
                        dl = requests.get(imageinfo[0].get("url"), timeout=10, headers=headers)
                        if dl.status_code==200:
                            # Determine file extension from Content-Type
                            content_type = dl.headers.get("content-type", "image/jpeg")
                            extension = mimetypes.guess_extension(content_type)
                            if not extension:
                                extension = ".jpg"
                            
                            # Save the image to the appropriate subfolder
                            with open(item_path / f"{page.get('pageid')}{extension}", "wb") as f:
                                f.write(dl.content)
                            print(f"   Requête {query} : Téléchargement en cours ...")
                        else:
                            print(f"   Requête {query} : Erreur de téléchargement !")
                        # Wait briefly between downloads to be polite
                        time.sleep(0.5)
                print(f"   Requête {query} : Traitement terminé !")
                time.sleep(1)
        print(f"Catégorie {category} : Traitement terminé !")
        time.sleep(2)