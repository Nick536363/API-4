from requests import *
from save_tools import *
from argparse import *
import dotenv
import os
def main():
    dotenv.load_dotenv(dotenv.find_dotenv())
    parser = ArgumentParser()
    parser.add_argument("--folder",type=str,default="./")
    parser.add_argument("count",type=int)
    api_key = default=os.getenv("APOD_EPIC_API")
    args = parser.parse_args()
    url_apod = "https://api.nasa.gov/planetary/apod"
    params = {
            "api_key":api_key,
           "count":args.count
           }
    response_apod = get(url_apod,params=params)
    for index, value in enumerate(response_apod.json(), 1):
        filename = f"apod_{index}.png"
        apod_link = value["url"]
        image_download(apod_link,f"{args.folder}",f"{filename}")

main()