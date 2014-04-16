from twilio.rest import TwilioRestClient 
from train_adv import func
from datetime import datetime

if __name__ == "__main__":
    alert = ""
    title = ""
    with open("log.txt", 'r') as fp:
        log = fp.read()
        for a in func():
            title, msg = a.split('\t')
            if title not in log:
                alert += msg + '\n'
        if alert == "":
            if "Everything is running" not in log:
                alert = "Everything is running smoothely as of " + str(datetime.now()).split('.')[0]
   
    if alert != "":
    
        ACCOUNT_SID = "AC410387af155b3f5e8d5bcd9f95ab0ca4" 
        AUTH_TOKEN = "8f4b870973aedc7f54fdcbf9586a661e" 
        
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
        
        message = client.messages.create(
            to="2019837309", 
            from_="+12013554927", 
            body=alert,  
            )
        
        with open("log.txt", 'a') as l:
            l.write(str(datetime.now()) + '\t' + str(message.sid) + '\t' + title + '\t' + alert + '\n')

