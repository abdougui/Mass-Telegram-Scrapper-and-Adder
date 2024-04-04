from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputUser
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

import sys
import csv
import traceback
import time
import random
api_id = 0 #you can get it from https://my.telegram.org/
api_hash = 'api' #you can get it from https://my.telegram.org/
phone='+1xxxxxxxxxxxxx' # Your Number 



group=input("Enter the group/channel username you want to join : ") 
client = TelegramClient('data/'+phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
	client.send_code_request(phone)
	client.sign_in(phone, input('Enter the code: '))
client(JoinChannelRequest(group)) 
# client(ImportChatInviteRequest(hash='8a4s84s8K0mJ6xlhhMTBk')) # if you have an invite link  replace the hash with your invit link

