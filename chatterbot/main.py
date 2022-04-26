from numpy import logical_and
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

bot = ChatBot('Ricky Talk Bot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logical_adapter=['chatterbot.logic.BestMatch','chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter','chatterbot.logic.SpecificResponseAdapter'],
        database_uri = 'sqlite:///database.sqlite3')

# create a new trainer
trainer = ChatterBotCorpusTrainer(bot)
list_trainer = ListTrainer(bot)

# create a trainer that trains the chatbot based libraries
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.conversations")

bot.get_response("Hello, how are you?")

# getting a response from the bot
while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

# trainning your chatbot
list_trainer.train([
    "Olá, em que posso ajudar?",
    "Olá, tudo bem?",
    "Tudo bem, obrigado",
    "Estou bem, e você?",
    "Bom dia",
    "Boa noite",
    "Obrigado",
    "De nada",
    "Obrigada",
    "Por nada",
    "Muito obrigado",
    "Á disposição",
    "Obrigado, há algo mais que eu possa fazer para te ajudar?",
    "O horário de funcionamento é de segunda a sexta das 8:00 às 18:00",
    "Muito obrigado pelo seu contato. Esperamos seu retorno!",
])