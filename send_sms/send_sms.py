from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACeef1b02b359fad7bf493f482dd52a669"
# Your Auth Token from twilio.com/console
auth_token  = "4adb1ba44d96c74eed587cb35ccb1e94"
from_phone = "+18070265802"

client = Client(account_sid, auth_token)

def send_sms(to_phone, body)
    message = client.messages.create(
        to=to_phone, 
        from_= from_phone
        body=body)
    
    return message.sid


