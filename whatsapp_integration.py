import requests

def send_whatsapp_message(phone_number, message):
    url = "https://api.whatsapp.com/send"
    data = {
        "phone": phone_number,
        "text": message
    }
    response = requests.post(url, data=data)
    print(response.json())
