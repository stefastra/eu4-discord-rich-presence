from pypresence import Presence
import time, os, sys, psutil
import configparser
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#for proc in psutil.process_iter():
#    if proc.name() == "eu4.exe":
#        print("EU4 detected with pid: " + str(proc.pid))
      

startepoch = time.time()
prev_content = ""
userdata_path = r"C:\Program Files (x86)\Steam\userdata"
most_recent_dir = None
most_recent_time = 0
RPC = Presence('687351243462541358')
RPC.connect()
RPC.update(state="Loading...",
        large_text="Europa Universalis IV", large_image="eu4logolarge",
        start=startepoch)

# Check if ID3 should be read from steam directory
try:
    config = configparser.ConfigParser()
    config.read("id3.txt")
    readOnStart = config['DEFAULT'].get('readonstart')
    sleepTime = config['DEFAULT'].getint('sleeptime')
    print("Read ID3 on startup: " + readOnStart)
    print("Seconds between checks: " + str(sleepTime))
except:
    print("Error reading config file!")

# Reads most recently accessed directory in \userdata, which should be a folder with the name of your steam ID3
if(readOnStart):
    try:
        print("Reading ID3 from steam files")
        for entry in os.scandir(userdata_path):
            if entry.is_dir():
                entry.stat().st_mtime_ns
                mod_time = entry.stat().st_mtime_ns
                if mod_time > most_recent_time:
                    most_recent_dir = entry.name
                    most_recent_time = mod_time
        if 'DEFAULT' in config and 'id3' in config['DEFAULT']:
            config['DEFAULT']['id3'] = most_recent_dir
            with open("id3.txt", 'w') as configfile:
                config.write(configfile)
        else:
            print("You have corrupted the \"id3.txt\" file.")
    except:
        print("Error reading ID3!")

# Reads currently loaded ID3 in config file
try:
    config.read("id3.txt")
    id3 = config['DEFAULT'].get('id3')
    print("Currently using id3: " + id3)
    if 'DEFAULT' in config and 'readOnStart' in config['DEFAULT']:
            config['DEFAULT']['readOnStart'] = str(False)
            with open("id3.txt", 'w') as configfile:
                config.write(configfile)

except:
    print("Error reading config file!")

while(True):
    print("Updating Presence...")
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        driver.get("https://steamcommunity.com/miniprofile/" + str(id3))
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', attrs={'class': 'miniprofile_gamesection'})
        lines = div.text.strip().split("\n")
        if "Europa Universalis IV" in lines:
            print("EU4 is running") #if eu4 is not running it goes to exception, need to do some changes here
            content = lines[2] if len(lines) > 2 else "" #line 2 is rich presence data
            print(content)
            if content != prev_content:
                RPC.update(details=f"{content}",
                large_text="Europa Universalis IV", large_image="eu4logolarge",
                start=startepoch)
                prev_content = content
                print("Updated presence succesfully")
            else:
                print("No change in presence detected")
        else:
            print("EU4 not running")
    except:
        print('Error updating presence or EU4 not running') #todo change some lines here
        RPC.update(details="Stopped...",
        large_text="Europa Universalis IV", large_image="eu4logolarge",
        start=startepoch)
        print("Cleared presence")
        sys.exit(0)


    time.sleep(sleepTime) #def=5 should default be 5 or 20 ?