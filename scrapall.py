import asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import UserStatusRecently, UserStatusOnline, UserStatusLastWeek, UserStatusLastMonth, UserStatusEmpty, UserStatusOffline

import csv
import time
async def main():
    api_id = 0 #you can get it from https://my.telegram.org/
    api_hash = 'api' #you can get it from https://my.telegram.org/
    phone='+1xxxxxxxxxxxxx' # Your Number 

    client = TelegramClient('session/'+phone, api_id, api_hash)
    await client.connect()
    connected= await client.is_user_authorized()
    if not connected:
        await client.send_code_request(phone)
        await client.sign_in(phone, input('Enter the code: '))
    chats = []
    last_date = None
    chunk_size = 200
    i=0
    groups= []
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            groups.append(dialog)
    for g in groups:
        print(str(i) + '- ' + g.title)
        i+=1
     
    g_index = input("Enter a Number: ")
    chat=groups[int(g_index)]
    #all_participants = await client.get_participants(chat)
    
    all_participants=await getUsers(client,chat)
    active_users=[]
    active_no=[]
    i=0
    print(str(0) + '- Scrap online users')
    print(str(1) + '- Scrap recently users ')
    print(str(2) + '- Scrap last month login users')
    selected_date = int(input("Enter a Number: "))
    for active in all_participants:
        if isinstance(active.status,UserStatusOnline) and selected_date==0:
            i+=1
            active_users.append(active)
        elif (isinstance(active.status, UserStatusLastMonth) or isinstance(active.status, UserStatusLastWeek)) and  selected_date==2  :
            i+=1
            active_users.append(active)
        if isinstance(active.status,UserStatusRecently) and selected_date==1:
            i+=1
            active_users.append(active)
    with open("data/"+phone+".csv","w",encoding='UTF-8') as f:
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
        for user in active_users:
        # for user in all_participants:
            if user.username:
                username= user.username
            else:
                username= ""
            if user.first_name:
                first_name= user.first_name
            else:
                first_name= ""
            if user.last_name:
                last_name= user.last_name
            else:
                last_name= ""
            name= (first_name + ' ' + last_name).strip()
            writer.writerow([username,user.id,user.access_hash,name,chat.title, chat.id]) 
    print(str(i)+' Members has been scraped successfully.')
async def getUsers(auth,group):
    offset = 0
    limit = 200
    all_participants = []
    while True:
        participants = await auth(GetParticipantsRequest(
            group, ChannelParticipantsRecent(), offset, limit,
            hash=0
        ))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset += len(participants.users)
    return all_participants

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())