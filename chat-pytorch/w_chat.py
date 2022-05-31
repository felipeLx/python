import random
import json
import torch
from model import NeuralNet
from nltk_utils import tokenize, bag_of_words
import pyautogui as pt
from time import sleep
import pyperclip

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = 'data.pth'
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Tour Guide"
print('Let\'s chat! (type quit to exit)')
while True:
    sentence = input('You: ')
    if sentence == 'quit':
        break
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                responses = intent['responses']
                print(f'{bot_name}: {random.choice(responses)}')
    else:
        print(f'{bot_name}: I do not understand.')


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
    sentence = input(pyperclip.paste())
    return sentence

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