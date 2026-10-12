import os
import requests
import time

TOKEN = os.getenv("IPINFO_TOKEN")
GEOTOKEN = os.getenv("GEOIPINFO_TOKEN")


try:
    with open("ips.txt", "r") as file:
        ips = file.read().splitlines()

except FileNotFoundError:
    with open("ips.txt", "a") as file:
        file.write("8.8.8.8")
        exit()

for ip in ips:
    ip = ip.strip()
    url = f"https://api.ipinfo.io/lite/{ip}?token={TOKEN}"
    geourl = f"https://api.ipapi.com/api/{ip}"


    response = requests.get(url)
    georesponse = requests.get(geourl, params={"access_key": GEOTOKEN})

    dataSTR = response.text
    geodataSTR = georesponse.text

    dataJSON = response.json()
    geodataJSON = georesponse.json()

    with open("ipinfo.txt", "a") as file:
        file.write(f"{dataSTR}\n\n-------------------------------------------\n\n{geodataSTR}\n\n")
    
    with open("ipinfo-json.txt", "a") as file:
        file.write(f"{dataJSON}\n\n-------------------------------------------\n\n{geodataJSON}\n\n")

    time.sleep(0.5) # for rate limits
