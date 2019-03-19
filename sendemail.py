import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxcf842d9f987544928985e1c629c9e53d.mailgun.org/messages",
        auth=("api", "79c122436bd682f8c5ef8c29be25468a-985b58f4-f9b73cec"),
        data={"from": "Excited User <mailgun@sandboxcf842d9f987544928985e1c629c9e53d.mailgun.org>",
              "to": ["aliciajuzhuqing@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

send_simple_message()
