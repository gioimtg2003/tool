import os
import random
import sys
import time
import re
import json
from datetime import datetime
from urllib import response
import requests
dau = " [✓] => "
red = '\033[1;91m'
mautim = '\033[95m'
blue = '\033[1;94m'
green = '\033[92m'
UNDERLINE = '\033[4m'
vang = '\033[93m'
intro = \
    f'''
\033[1;94m╔═════════════════════════════════════════════════════════╗

\033[95m                          🚩🚩🚩                           
\033[92m         🏵️🏵️🏵️ Bản quyền: Nguyễn Công Giới 🏵️🏵️🏵️          
\033[93m       👉👉👉       Zalo: 0367093723    👈👈👈            
\033[92m       🤑🤑🤑       Momo: 0367093723    🤑🤑🤑            
\033[93m                ..........❌❌❌..........  
                          
\033[1;94m╚═════════════════════════════════════════════════════════╝

\033[1;91m===========================================================
'''

def load():
    for _ in range(5, 0, -1):
        t = random.randint(1, 5)
        if t == 1:
            mau = red
            icon = '😆'
        elif t == 2:
            mau = blue
            icon = '😉'
        elif t == 3:
            mau = green
            icon = '🤣'
        elif t == 4:
            mau = vang
            icon = '😘'
        elif t == 5:
            mau = mautim
            icon = '😛'
        print(mau, f'🕐   ████{icon}', end=' \r')
        time.sleep(0.1)
        print(mau,f'🕑   ████████{icon}', end=' \r')
        time.sleep(0.1)
        print(mau,f'🕒   ████████████{icon}', end=' \r')
        time.sleep(0.1)
        print(mau,f'🕓   ████████████████{icon}', end=' \r')
        time.sleep(0.1)
        print(mau,f'🕔   ████████████████████{icon}', end=' \r')
        time.sleep(0.1)
        print(mau,f'🕕   ████████████████████████{icon}', end=' \r')
        time.sleep(0.1)
        print(mau,f'🕖   ████████████████████████████{icon}', end=' \r')
        time.sleep(0.1)
        print(mau,f'🕗   ████████████████████████████████', end=' \r')
        time.sleep(0.1)
        print('🕘                                              ', end=' \r')
        time.sleep(0.1)
        print('🕚', end=' \r')
        time.sleep(0.1)
load()
time.sleep(1)
os.system('clear')
print(intro)
link = link0 +link1 + link2 + link3+ link4 +link5 +link6 + link7 +link8 +link9 +link10
key = requests.get(link)
link1s = json.loads(key.text)['link']
message = json.loads(key.text)['success']
if message == "1":
    print(green,"Tool đang bảo trì lại vui lòng liên hệ zalo ")
elif message == "2":
    print(blue,json.loads(key.text)['message'])
    
print(green, "Vào link này để lấy key nha: ", vang, link1s)
key_day = json.loads(key.text)['key_day']
while True:
    key_ = str(input(f"{mautim}➽ Nhập key: "))
    if key_ == key_day:
        break
    else:
        print(red, "Nhập lại")
        
print(blue, "Key Chính xác")
time.sleep(2)
os.system('clear')
print(intro)
tds = str(input(f"{mautim}➽{green} Nhập token TDS: {vang}"))
login = requests.get(f'https://traodoisub.com/api/?fields=profile&access_token={tds}')

try:
    if(login.json()['success']):
        print(green, 'Đăng Nhập Thành Công ✓ ')
except:
    print(red, 'Đăng nhập thất bại 😢')
    pass

print(mautim, "●", green, "User: ", end='')
print(vang, login.json()['data']['user'])
print(mautim, "●", green, "Số xu hiện tại: ", end='')
print(vang, login.json()['data']['xu'])
print(blue, datetime.now().strftime("%H:%M:%S"))
for _ in range(30):
    print(vang, "=", end="")
    time.sleep(0.008)
print("\n")
while True:
    try:
        number_fb = int(
            input(f"{mautim}➽{green} Nhập số nick facebook(mình chưa ra đa luồng nên các bạn nhập 1 thôi nha): {vang}"))
        break
    except:
        print(mautim, "➽", red, "Vui lòng nhập lại số nick facebook để chạy")

list_namefb = []
list_idfb = []
error = 0
token = []

for i in range(number_fb):
    t = str(i+1)
    input_token = str(input(f"{mautim}➽{green} Nhập token thứ {t}: {vang}"))
    token.append(input_token)
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+input_token).text)
   
    if "id" in check_token:
        print(vang, "Token hợp lệ ", red, "✓", green,
              "  id: ", vang, check_token['id'])
        list_idfb.append(check_token['id'])
        list_namefb.append(check_token['name'])
    else:
        print(red, "❌❌❌Token die hoặc không hợp lệ❌❌❌")
        error += 1
        if error == number_fb:
            sys.exit()
time.sleep(2)
print(intro)
while True:
    try:
        stop_tool = int(
            input(f"{mautim}➽{green} Sau bao nhiêu nhiệm vụ thì dừng tool: {vang}"))
        break
    except:
        print(blue, "❗❗Vui lòng nhập lại❗❗")

while True:
    try:
        stop_block = int(
            input(f"{mautim}➽{green} Sau bao nhiêu nhiệm vụ dừng lại chống block: {vang}"))
        break
    except:
        print(blue, "❗❗Vui lòng nhập lại❗❗")

while True:
    try:
        l = str(stop_block)
        delay_block = int(
            input(f"{mautim}➽{green} Sau {vang}{l}{green} Dừng lại chống block bao nhiêu giây: {vang}"))
        break
    except:
        print(blue, "❗❗Vui lòng nhập lại❗❗")
if number_fb > 1:
    while True:
        try:
            convert_fb = int(
                input(f"{mautim}➽{green} Sau bao lâu thì đổi nick facebook: {vang}"))
            break
        except:
            print(blue, "❗❗Vui lòng nhập lại❗❗")
else:
    convert_fb = stop_tool
while True:
    try:
        delay = int(
            input(f"{mautim}➽{green} Nhập time delay cho mỗi nhiệm vụ: {vang}"))
        break
    except:
        print(blue, "❗❗Vui lòng nhập lại❗❗")

os.system('clear')
print(intro)
job = []
while True:
    option_like = str(
        input(f"{vang}➽{green} Nhập (y/n) để làm nhiệm vụ like: {blue}").lower())
    if option_like == "y":
        job.append("like")
        break
    elif option_like == "n":
        break
    else:
        print(blue, "🐺Nhập lại🐺")
while True:
    option_share = str(
        input(f"{vang}➽{green} Nhập (y/n) để làm nhiệm vụ share:(fix) {blue}").lower())
    if option_share == "y":
        job.append("share")
        break
    elif option_share == "n":
        break
    else:
        print(blue, "🐺Nhập lại🐺")
while True:
    option_like = str(input(
        f"{vang}➽{green} Nhập (y/n) để làm nhiệm vụ comment(fix): {blue}").lower())
    # if option_like == "y":
    #     break
    # elif option_like =="n":
    #     break
    # else:
    #     break
    break
while True:
    option_like = str(input(
        f"{vang}➽{green} Nhập (y/n) để làm nhiệm vụ follow(fix): {blue}").lower())
    # if option_like == "y":
    #     break
    # elif option_like =="n":
    #     break
    # else:
    #     break
    break
global count_job, erorr_token, error_job
count_job = 0
error_job = 0
error_jobl = 0
number_fb_ = 0
def delaytime(delay):
    for _ in range(delay, -1, -1):
        if (int(_+1) % 2) == 0:
            color = red    
        else:
            color = blue    
        print(f" {vang}[{color}-{vang}]{blue}  Delay chờ nhiệm vụ {vang}{_}🌸", end=' \r')
        time.sleep(0.1)
        print(f" {vang}[{color}\{vang}]{blue}  Delay chờ nhiệm vụ {vang}{_}   🌸", end=' \r')
        time.sleep(0.1)
        print(f" {vang}[{color}|{vang}]{blue}  Delay chờ nhiệm vụ {vang}{_}      🌸", end=' \r')
        time.sleep(0.1)
        print(f" {vang}[{color}/{vang}]{blue}  Delay chờ nhiệm vụ {vang}{_}         🌸", end=' \r')
        time.sleep(0.1)
        print(f" {vang}[{color}/{vang}]{blue}  Delay chờ nhiệm vụ {vang}{_}             ", end=' \r')
        time.sleep(0.1)
        time.sleep(0.5)
    print("                                                                ", end=' \r')
        
def delayblock(delay):
    for _ in range(delay, -1, -1):
        if (int(_+1) % 2) == 0:
            color = red    
        else:
            color = blue    
        print(f" {vang}[{color}-{vang}]{blue}  Delay chống block {vang}{_}🌸", end=' \r')
        time.sleep(0.1)
        print(f" {vang}[{color}\{vang}]{blue}  Delay chống block {vang}{_}  🌸", end=' \r')
        time.sleep(0.1)
        print(f" {vang}[{color}|{vang}]{blue}  Delay chống block {vang}{_}    🌸", end=' \r')
        time.sleep(0.1)
        print(f" {vang}[{color}/{vang}]{blue}  Delay chống block {vang}{_}       🌸", end=' \r')
        time.sleep(0.1)
        print(f" {vang}[{color}/{vang}]{blue}  Delay chống block {vang}{_}           ", end=' \r')
        time.sleep(0.1)
        time.sleep(0.5)
        
def like(uid, access_token):
    link = 'https://graph.facebook.com/'+ str(uid) + '/likes'
    data ="access_token=" +access_token
    response_ = requests.post(link, data=data)
    return response_.status_code
def share():
    print()
for q in range(29):
    if (int(q+1)%2) == 0:
        mau_ = blue
    else:
        mau_ = red
    print(mau_, "=", end='')
    time.sleep(0.01)
print('\n')
def get_like(token_tds):
    response = requests.get("https://traodoisub.com/api/?fields=like&access_token="+str(token_tds), time.sleep(0.5) )
    idlike = json.loads(response.text)[0]['id']
    return idlike
def get_money_l(uid, token_tds):
    response = requests.get(
        "https://traodoisub.com/api/coin/?type=LIKE&id="+str(uid)+"&access_token="+str(token_tds), time.sleep(0.5))
    msg =json.loads(response.text)['data']['xu']
    return msg
while True:
    try:
        print("🔷", green,"ID: ", vang,list_idfb[number_fb_], "🔶", green, "Name FB: ", vang, list_namefb[number_fb_])
        data_dat = {
            'iddat': list_idfb[number_fb_]
            }
    except:
        print(green, "🌸🌸🌸🌸Thoát tool🌸🌸🌸🌸")
        sys.exit()
    datnick = requests.get(
        f"https://traodoisub.com/api/?fields=run&id={list_idfb[number_fb_]}&access_token=" + tds)
    if "success" in datnick.json():
        print(blue, "➽", green, " Cấu hình thành công id: ", vang, list_idfb[i])
        error_ = 0
        for _ in range(29):
            if (int(_+1)%2) == 0:
                mau = blue
            else:
                mau = red
            print(mau, "=", end='')
            time.sleep(0.01)
        print('\n')
        
    else:
        print(red, "💢Cấu hình thất bại hoặc có thể bạn chưa thêm vào💢")
        if number_fb == 1:
            sys.exit()
        else:
            error_ = 1
    erorr_token = 0   
    for t in range(convert_fb): 
        error_job_ = 0 
        auto = str(random.choice(job))
        
        if error_ == 1:
            break
        
        if (auto == "like") :
            try:                               
                id_like = get_like(tds)
                error_job_ = 0
                try:
                    like_ = like(id_like, token[number_fb_])
                    if like_ == 400:
                        check = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+str(token[number_fb_])).text)
                        if "id" in check:
                            erorr_token = 0
                            print(vang,"Check lại token!!!", end=' \r')
                        else:
                            print(vang,f"Token die: {erorr_token}", end=' \r')
                            sys.exit()
                                                
                        if erorr_token == 2:
                            print("                                   ")
                            print(red, "Token die hoặc block")
                            break
                except:
                    continue
            except:
                print(vang, "Lỗi tìm id like ", end=' \r')
                if error_job_ == 2:
                    print(red,"Hết nhiệm vụ like😤😤😤")
                    break
                error_job_ += 1                
            
            
                    
                if erorr_token == 2:
                    print("                                   ")
                    print(red, "Token die hoặc block")
                    break
            else:
                erorr_token = 0
            
            try:            
                get_xu_like = get_money_l(uid=id_like, token_tds=tds)
                tgian = datetime.now().strftime("%H:%M:%S")
                print(mautim,f"[{blue}{count_job}{mautim}]{vang}●{blue}{tgian}{mautim} ➽ {vang}By:{green}Nguyễn Công Giới", vang,f"+300xu{red} ●" ,blue,f"Xu:{vang}{get_xu_like}")
                count_job += 1
                error_jobl = 0
            except:
                error_jobl = 1
        
        if (error_jobl == 0) and(delay!= 0):    
            
            delaytime(delay=delay)
        error_jobl = 0            
    number_fb_ +=1
