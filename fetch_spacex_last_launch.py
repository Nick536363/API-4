from save_tools import *
from requests import *
from argparse import *

def main():
    parser = ArgumentParser()
    parser.add_argument("--folder", type=str,default="images")
    launch_id = "5eb87d47ffd86e000604b38a"
    args = parser.parse_args()
    url_spacex = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response_spacex = get(url_spacex)
    response_spacex.raise_for_status()

    for index, link in enumerate(response_spacex.json()['links']['flickr']['original']):
        filename = f"spacex_image_{index+1}.jpg"
        image_download(link,args.folder, filename)


main()