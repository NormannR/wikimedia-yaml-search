import argparse
from wikimedia_yaml_search.downloader import dl_commons_images

def main():
    """Parse command-line arguments and run the download logic."""
    parser = argparse.ArgumentParser(description="Search and download images from Wikimedia Commons.")
    parser.add_argument("--filename", type=str, required=True, help="YAML file with search terms")
    parser.add_argument("--limit", type=int, default=2, help="Number of images to download per query (default: 2)")
    args = parser.parse_args()

    filename = args.filename
    limit = args.limit
    dl_commons_images(filename, limit=limit)

if __name__ == "__main__":
    main()