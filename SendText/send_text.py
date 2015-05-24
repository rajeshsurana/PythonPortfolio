from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC0eeaed40f53b60dec0160652c27d978a"
auth_token  = "a7fb163b406e58a22c5b399feb4a18cb"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi Rajesh, You got message from Twilio",
    to="+14802898922",    # Replace with your phone number
    from_="+16233777354") # Replace with your Twilio number
print message.sid
