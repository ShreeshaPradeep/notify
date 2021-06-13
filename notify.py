import time

from plyer import notification


def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Shreesha\\Downloads\\Icons-Land-Medical-Equipment-Syringe-Full.ico",
        timeout = 10,
        )
if __name__ == '__main__':
   

        notifyMe("Hey hurry up !!","Book your slots")
        
