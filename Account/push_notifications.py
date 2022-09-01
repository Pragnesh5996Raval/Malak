import requests
from decouple import config
import json

class Notification:
    def Notify(deviceToken, title, message, notify_status):
        serverToken = config('Firebase_Secret')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

        body = {
            'to': deviceToken,
            'notification': 
            {
                'title': title,
                'body': message,
                'sound':'default',
                'content-available': True,
            },
            'data': {
                'title': title,
                'body': message,
                'content-available': True,
                'click_action': 'FLUTTER_NOTIFICATION_CLICK',
                'status':notify_status
            },
            'priority': 'high', 
        }
        response = requests.post("https://fcm.googleapis.com/fcm/send",headers=headers, data=json.dumps(body))
        if response.status_code == 200:
            response = json.loads(response.text) 
        else:
            response = ""
        data_dict = dict()
        if response != "":
            data_dict["response"] = response
            data_dict["data"] = {
                'title': title,
                'body': message,
                'content-available': True,
                'click_action': 'FLUTTER_NOTIFICATION_CLICK',
                'status':notify_status
            }
        else:
            data_dict["response"] = response
            data_dict["data"] = {} 
        return data_dict