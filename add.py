from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputUser
import sys
import csv
import traceback
import time
import random
api_id = 0 #you can get it from https://my.telegram.org/
api_hash = 'api' #you can get it from https://my.telegram.org/
phone='+1xxxxxxxxxxxxx' # Your Number 

client = TelegramClient('session/'+phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
input_file = "data/all-"+phone+".csv"
users = []
keyword="DM"
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    i=0
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

chats = []
last_date = None
chunk_size = 200
groups=[]

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        # if chat.broadcast == True:
            # groups.append(chat)
        groups.append(chat)
    except:
        continue

print('Choose a group to add members:')
i=0
for group in groups:
    print(str(i) + '- ' + group.title)
    i+=1

g_index = input("Enter a Number: ")
target_group=groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)

mode = int(input("Enter 1 to add by username or 2 to add by ID: "))
n = 0
for user in users:
    n+=1
    if n%200==0:
        time.sleep(900)
    try:
        if mode == 1:
            if user['username'] == "":
                user_to_add = InputUser(user['id'], user['access_hash'])
            else:
                user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputUser(user['id'], user['access_hash'])
        else:
            sys.exit("Invalid Mode Selected. Please Try Again.")  
        client(InviteToChannelRequest(target_group_entity,[user_to_add]))
        print("Waiting 60 Seconds...")
        print ("Adding {}".format(user['id'])) 
        time.sleep(random.randrange(60, 100))
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        # time.sleep(random.randrange(60, 100))
        continue
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
        # time.sleep(random.randrange(60, 100))
        continue
    except:
        traceback.print_exc()
        #time.sleep(60) 
        continue