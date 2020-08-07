from pypresence import Presence
import time

startepoch = time.time()

country_name = "Prussia"
ruler_title = "King-Elector"
enemy_country_name = "Austria"
ironman = "Non-"
#temp: switch for every case 1)In main menu 2)Ruling 3)Leading

RPC = Presence('687351243462541358')
RPC.connect()

RPC.update(state=f"In a war against {enemy_country_name}",
details=f"Leading as {ruler_title} of {country_name}",
large_text="Europa Universalis IV", large_image="eu4logolarge",
small_image="ironmanlogolarge",
small_text=f"{ironman}Ironman Mode",
start=startepoch)
#todo: pid="proccess_id"

while True:
    time.sleep(15)