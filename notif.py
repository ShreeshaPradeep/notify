import requests

import time
import datetime
from plyer import notification
from datetime import date

print("\n")
state = input("Enter Your State Name : ")
print("\n")
dis = input("Enter Your District Name : ")
print("\n")
date = input("Enter Sate In The Format  DD-MM-YYYY:\n> ")
print("\n")
age = int(input("Enter Your Age As :\n If 18 and above Enter as 18 \n If 45 and above Enter as 45 \n >  "))
print("\n")



header = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def findAvailability():
    URL1 = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
    result = requests.get(URL1, headers=header)
    response_json = result.json()
    data = response_json["states"]



    for each in data:
        if state == each["state_name"]:
            id = each["state_id"]


    URL2 = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(id)

    result = requests.get(URL2, headers=header)
    response_json = result.json()
    data1 = response_json["districts"]

    for each in data1:
        if dis == each["district_name"]:
            id1 = each["district_id"]




    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(
        id1, date)
    counter=0
    result = requests.get(URL,headers=header)
    response_json = result.json()
    data = response_json["sessions"]

    for each in data:
        if ((each["available_capacity"]>0)&(each["min_age_limit"]==age)):
            counter +=1
            print(each["name"])
            print(each["pincode"])
            print(each["vaccine"])
            print(each["available_capacity"])
            print("\n")
            return True
    if(counter == 0):
        print("no Available Slots\n")
        return False


def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Shreesha\\Downloads\\Icons-Land-Medical-Equipment-Syringe-Full.ico",
        timeout = 10,
        )

while(findAvailability()!=True):

    time.sleep(2)
    findAvailability()

while(findAvailability()==True):
    if __name__ == '__main__':
        notifyMe("HURRY HURRY  !!!", "SLOTS ARE AVAILABLE FOR BOOKING :) ")

    time.sleep(10)
    findAvailability()





