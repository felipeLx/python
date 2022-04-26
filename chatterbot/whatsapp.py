import pyautogui as pt
from time import sleep
import pyperclip
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

bot = ChatBot(
    name='PyBot',
    logical_adapter=['chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation']
    )

small_talk = ['hi there!',
          'Hello',
          'hi!',
          'how do you do?',
          'how are you?',
          'i\'m cool.',
          'fine, you?',
          'always cool.',
          'i\'m ok',
          'glad to hear that.',
          'i\'m fine',
          'glad to hear that.',
          'i feel awesome',
          'excellent, glad to hear that.',
          'not so good',
          'sorry to hear that.',
          'what\'s your name?',
          'i\'m pybot. ask me a math question, please.']
math_talk_1 = ['pythagorean theorem',
          'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines',
          'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

list_trainer = ListTrainer(bot)

for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')

sleep(3)

# define position to start bot
start_pos = pt.locateOnScreen('face_att.png', confidence=0.6)
x = start_pos[0]
y = start_pos[1]

# gets message
def get_message():
    global x, y
    position = pt.locateOnScreen('face_att.png', confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration = 0.05)
    pt.moveTo(x+80, y-40, duration = 0.5)
    pt.tripleClick()
    pt.hotkey('ctrl', 'c')
    message = pyperclip.paste()
    print('get: ', message)
    return message

# post message
def post_message(message):
    global x, y
    position = pt.locateOnScreen('face_att.png', confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration = 0.5)
    pt.click()
    print('post: ', message)
    pt.typewrite(message)
    pt.press('enter')

# process response
def process_response(message):
    response = bot.get_response(message)
    print('process: ', response)
    return response

# check new message
def check_new_message():
    pt.moveTo(x+80, y-40, duration = 0.5)

    while True:
        # continuos looks for new message
        try:
            position = pt.locateOnScreen('green.png', confidence=0.7)
            if position is not None:
                pt.moveTo(position)
                # pt.moveRel(-100, 0)
                pt.click()
                pt.moveTo(start_pos)
                response = process_response(get_message())
                print('check new: ', response)
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