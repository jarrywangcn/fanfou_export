import fanfou
import pandas as pd
import json



consumer = {'key': 'your_key', 'secret': 'your_secret'}
client = fanfou.XAuth(consumer, 'your_id', 'your_password')
fanfou.bound(client)

#  get all the statuses
page = 1
last = False

total_df = pd.DataFrame(columns=['created_at', 'text'])

while last == False:
    body = {'page' : page}
    resp = client.statuses.user_timeline(body)
    data = resp.json()
    
    # control the loop
    if len(data) == 0:
        last = True
        break
    

    datas = pd.DataFrame(data)
    current_df = pd.DataFrame(datas, columns=['created_at', 'text'])
    
    # put every current_df into csv
    if page == 1:
        current_df.to_csv('fanfou_exp.csv', index = False )
    else:
        current_df.to_csv('fanfou_exp.csv', index = False, header = False, mode = 'a')

    
    # add the counter
    page += 1