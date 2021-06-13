import requests
import time
import time

from plyer import notification

dist = 266
date = "13-06-2021"

URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(dist,date)

header = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def findAvailability():
    counter=0
    result = requests.get(URL,headers=header)
    response_json = result.json()
    data = response_json["sessions"]

    for each in data:
        if ((each["available_capacity"]>0)&(each["min_age_limit"]==45)):
            counter +=1
            print(each["name"])
            print(each["pincode"])
            print(each["vaccine"])
            print(each["available_capacity"])
            return True
    if(counter == 0):
        print("no Available Slots")
        return False


def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Shreesha\\Downloads\\Icons-Land-Medical-Equipment-Syringe-Full.ico",
        timeout = 10,
        )

while(findAvailability()!=True):
    
    time.sleep(20)
    findAvailability()

while(findAvailability()==True):
    if __name__ == '__main__':
        notifyMe("HURRY HURRY.... !!!", "SLOTS ARE AVAILABLE TO BOOK")

    time.sleep(10)
    findAvailability()



