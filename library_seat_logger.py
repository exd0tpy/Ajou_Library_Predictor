import requests
import csv
from time import sleep
from bs4 import BeautifulSoup
import os
#f = open('library_seat_log.csv','a')
#wr = csv.writer(f)
#wr.writerow(['time','Area-C left','Area-D left'])
#f.close()
for _ in range(300000):
    f = open('library_seat_log.csv','a')
    wr = csv.writer(f)
    r=requests.get("http://u-campus.ajou.ac.kr/ltms/mobile/lst.mobile")
    c = r.content
    html = BeautifulSoup(c,"html.parser")
    li = html.find_all("li")

    tm = ['']
    st = ['']
    for l in li:
            tm.append(l.find("span",{"class":"roomTime"}))
            st.append(l.find("div",{"class":"roomStatus"}))


    time = str(tm[2]) 
    time = time[23:-7]
            
    D = str(st[6])
    C = str(st[4])
    D_left = D.split(' : <span>')[1].split('/')[0].strip()
    C_left = C.split(' : <span>')[1].split('/')[0].strip()
    wr.writerow([time,C_left,D_left])
    f.close()
    os.system('./gitpush.sh')
    sleep(120)




