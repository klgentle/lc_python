from twilio.rest import Client
from sys import argv

# Your Account SID from twilio.com/console
account_sid = "ACeef1b02b359fad7bf493f482dd52a669"
# Your Auth Token from twilio.com/console
auth_token  = "d1e6e6ff2d46d7046163b0931e5bb85a"
from_phone = "+18070265802"

client = Client(account_sid, auth_token)

def send_sms(to_phone, body):
    message = client.messages.create(
        to=to_phone, 
        from_= from_phone,
        body=body)
    
    return message.sid

if __name__ == "__main__":
    to_phone = argv[1] 
    body = argv[2] 
    #print(f"to_phone:{to_phone}, body:{body}")
    send_sms(to_phone, body)
