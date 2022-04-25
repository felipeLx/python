import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

# define position to start bot
start_pos = pt.locateOnScreen('whatsapp/face_att.png', confidence=0.6)
x = start_pos[0]
y = start_pos[1]

# gets message
def get_message():
    global x, y
    position = pt.locateOnScreen('whatsapp/face_att.png', confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration = 0.05)
    pt.moveTo(x+80, y-40, duration = 0.5)
    pt.tripleClick()
    pt.hotkey('ctrl', 'c')
    message = pyperclip.paste()
    print(message)
    return message

# post message
def post_message(message):
    global x, y
    position = pt.locateOnScreen('whatsapp/face_att.png', confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration = 0.5)
    pt.click()
    pt.typewrite(message, interval=0.05)
    pt.typewrite("\n", interval=0.05)

# process response
def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        sleep(1)
        return "Eu nao sei responder isso."
    elif "!" in str(message).lower():
        return "Tem certeza?"
    else:
        if random_no == 0:
            return "That's cool."
        elif random_no == 1:
            return "I'm not sure."
        else:
            return "Mensagens escritas por um chatbot (robot)"

# check new message
def check_new_message():
    pt.moveTo(x+80, y-40, duration = 0.5)

    while True:
        # continuos looks for new message
        try:
            position = pt.locateOnScreen('whatsapp/green.png', confidence=0.7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                pt.moveTo(start_pos)
                response = process_response(get_message())
                post_message(response)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(0.5)
        except(Exception):
            print("No new message")
        """
        if pt.pixelMatchesColor(int(x + 50), int(y - 40), (255,255,255), tolerance=10):
            print("have new message")
        else:
            print("no new message")
        """
        sleep(5)

check_new_message()