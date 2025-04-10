from requests import *
from telegram import *
import time
import os
import dotenv
from random import *
def publish(folder,chat_id):
    print(os.walk(folder))
    dotenv.load_dotenv(dotenv.find_dotenv())
    bot = Bot(token=os.getenv("TELEGRAM_API"))
    iter = 1
    files = []
    sended = []
    for image in os.walk(folder):
        files.append(image)
        
    while True:
        print(f"Count of all elements:{len(files[0][2])-len(sended)}")
        print(f"Alreadysended files:{sended}")
        try:
            file = choice(files[0][2])
            if file not in sended:
                sended.append(file)
                print(f"Sended file is:{file}")
                bot.send_photo(chat_id=chat_id,photo=open(f"{folder}\{file}","rb"))
            else:
                continue
            
            time.sleep(int(os.getenv("PUBLISH_FREQ")))
            iter+=1
        except KeyboardInterrupt:
            bot.send_message(text="Стоп",chat_id=chat_id)
            print("-------------------LOG------------------\nScript ended by user")
            break
        if iter > len(files[0][2]):
            bot.send_message(text="Рестарт",chat_id=chat_id)
            print("-------------------LOG------------------\nScript restarted")
            sended = []
            iter = 1
            continue

def image_download(url, folder, file_name, api_key=""):
    if not os.path.exists(folder):
        os.mkdir(folder)
    full_path = os.path.join(folder, file_name)
    response = get(url)
    response.raise_for_status()
    with open(full_path, "wb") as file:
        file.write(response.content)