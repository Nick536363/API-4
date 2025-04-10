from requests import *
from save_tools import *
from argparse import *


def main():
    parser = ArgumentParser()
    parser.add_argument("--folder",type=str,default="./")
    api_key =os.getenv("APOD_EPIC_API")
    args = parser.parse_args()
    params = {"api_key":api_key}
    url_epic = "https://api.nasa.gov/EPIC/api/natural/images?"
    responce_epic = get(url_epic,params=params)
    responce_epic.raise_for_status()
    filename = "epic_image"
    for index, value in enumerate(responce_epic.json()):
        date = value["date"].split(" ")[0].split("-")
        url_image =f"https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{value["image"]}.png?api_key=RmuI9523Umwd95LYPYScwaoATdFWWtkdelyIWF4U"
        image_download(url_image,args.folder,f"{filename}_{index+1}.png")

main()