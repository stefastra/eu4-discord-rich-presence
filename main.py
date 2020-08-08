from pypresence import Presence
from subprocess import check_output
#from api.windows import get_title, get_process_info, get_status
#TODO: get proccess id somehow
import time
import os

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

savefile_path = os.environ['USERPROFILE'] + "\\Documents\\Paradox Interactive\\Europa Universalis IV\\save games\\autosave.eu4"

while True:
 time.sleep(15) #TODO: tweak intervals so it doesn't waste resources
 startepoch = time.time()

 i=1
 f=open(savefile_path,"r")
 while(i<=5):
  x=f.readline()[:-1]
  if(i == 2):
   current_year = x[5:9]
   current_month = months[int(x[10:][:-1][:-1])-1] #can only read autosaves, or it breaks
  if(i == 5):
   country_name = x[24:len(x)-1]
  i+=1
 f.close()

 ruler_title = "King" #todo

 RPC = Presence('687351243462541358')
 RPC.connect()

 RPC.update(state=f"{current_month}, {current_year}",
 details=f"{ruler_title} of {country_name}",
 large_text="Europa Universalis IV", large_image="eu4logolarge",
 start=startepoch)