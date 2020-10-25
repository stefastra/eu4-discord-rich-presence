from pypresence import Presence
import time, os, psutil
for proc in psutil.process_iter():
    if proc.name() == "eu4.exe":
        print("EU4 detected with pid: " + str(proc.pid))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
savefile_path = os.environ['USERPROFILE'] + "\\Documents\\Paradox Interactive\\Europa Universalis IV\\save games\\"
startepoch = time.time()
flag = True
RPC = Presence('687351243462541358')
RPC.connect()
RPC.update(state="Loading...",
        large_text="Europa Universalis IV", large_image="eu4logolarge",
        start=startepoch)
while(True):
    save_list = os.listdir(savefile_path)
    savefile_name = save_list[0]
    date_max = os.stat(savefile_path + save_list[0]) #exception for no saves goes here
    for sav in save_list:
        date = os.stat(savefile_path + sav)
        if date.st_mtime > date_max.st_mtime:
            savefile_name = sav
            #if not flag:
            #    print('Newer save found!')
            flag=True

    print("Using data from:", savefile_name)

    if(flag):
        print("Changes found, updating...")
        i=1
        try:
            f=open(savefile_path + savefile_name,"r")
            contents = f.read()
            f.close()
            listconts = contents.split()
            country_rank_num = listconts[listconts.index("human=yes") + 3][16:]
            if(int(country_rank_num) == 1):
                country_rank = "Duchy"
            elif(int(country_rank_num) == 2):
                country_rank = "Kingdom"
            else:
                country_rank = "Empire"
            x = listconts.index("EU4txt")
            country_name = listconts[x + 4][24:len(listconts[x + 4])-1]
            current_month = months[int(listconts[x + 1][10:][:-1][:-1])-1]
            current_year = listconts[x + 1][5:9]

            RPC.update(state=f"{current_month}, {current_year}",
            details=f"{country_rank} of {country_name}",
            large_text="Europa Universalis IV", large_image="eu4logolarge",
            start=startepoch)
            flag = False
            print("Updated presence succesfully")
        except:
            print('Error! Can only read uncompressed autosaves')
        print("Checking for changes...")
    time.sleep(20)