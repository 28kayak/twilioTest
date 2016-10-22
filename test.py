__author__ = 'kaya'
from twilio.rest import TwilioRestClient

account_sid = "AC06a7ed3cebe05e8bab4f0f541c438cc6"
auth_token = "30e187f14f14b226d85171adf5800b7d"
sideline = "+14084096757"
twilioNum = "+16502032422"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from python",
                                 to=sideline,
                                 from_=twilioNum)
print(message.sid)