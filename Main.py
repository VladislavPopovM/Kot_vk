import datetime 
import random
import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VKbot

def write_msg(user_id, message):
   vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(-2147483648, 2147483647)})
def write_msg_pick(user_id, message, image):
    vk.method('messages.send', {'user_id': user_id, 'message': message,'attachment': image ,'random_id': random.randint(-2147483648, 2147483647)})

#Api key
token = os.environ.get('BOT_TOKEN')
list_user=[]
image_list = {
    1: os.environ.get('1'),
    2: os.environ.get('2'),
    3: os.environ.get('3'),
    4: os.environ.get('4'),
    5: os.environ.get('5'),
    6: os.environ.get('6'),
    7: os.environ.get('7'),
    8: os.environ.get('8'),
    9: os.environ.get('9'),
    10:os.environ.get('10'),
    11:os.environ.get('11'),
    12:os.environ.get('12'),
    13:os.environ.get('13'),
    
}
now = datetime.datetime.now()
Last_time = now.day
#autorezation
vk = vk_api.VkApi(token=token)

#work with messages
longpoll = VkLongPoll(vk)

#main cycle
print("Server started")
for event in longpoll.listen():
    #New message 
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            # Message user
            bot = VKbot(event.user_id)
            print("New message:")
            string = bot.get_time()
            lst = string.split(':')
            
            if(Last_time != now.day):
                list_user = []
            Last_time = now.day
            print(f"For me by: {event.user_id}")
            if((event.text.upper() == 'ДАЙ ПЕЧЕНЬКУ') and (event.user_id not in list_user)):
                list_user.append(event.user_id)
                rand_dig = random.randint(1,13)
                image = image_list[rand_dig]
                print(bot.get_time())
                print(list_user)
                write_msg_pick(event.user_id,bot.new_message(event.text),image)
            elif((event.text.upper() == 'ДАЙ ПЕЧЕНЬКУ') and (event.user_id in list_user)):
                message1 = "А-а-а, не больше одной печеньки в день)"
                write_msg(event.user_id, message1)
            else:
                write_msg(event.user_id, bot.new_message(event.text))
            print("Text: ", event.text)
            
            
