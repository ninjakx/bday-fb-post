import facebook
import json
import requests
import datetime

now = datetime.datetime.now()
bdate=str(input("Enter bdate in the format date/month/year : "))  

date,month,year=bdate.split('/')

bdate_time=str(now.year)+'-'+month+'-'+date+'T00:00:00+0000'

access_token=''        # Put Acess Token Here
 
def convey_msg():
    payload = {'access_token' : access_token}
    r = requests.get('https://graph.facebook.com/me/feed', params=payload)
    result = json.loads(r.text)
    feeds = result['data']
    
    graph = facebook.GraphAPI(access_token)
   
    for post in feeds:
       print(post)
       msg="Thank you"       # Put your message here

       if post["created_time"] > bdate_time:

           graph.put_object(post["id"],connection_name="comments",message=msg)
           #print("posted")
     
    

if __name__ == '__main__':
    convey_msg()
