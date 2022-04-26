from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

bot = ChatBot(
    name='PyBot', 
    read_only=True,
    logical_adapter=['chatterbot.adapters.logic.ClosestMatchAdapter', 'chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation']
    )

small_talk = ['hi there!',
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

print(bot.get_response('hi there!'))
print(bot.get_response('Felling good today!'))
print(bot.get_response('What\'s your name?'))
print(bot.get_response('Show me the pythagorean theorem.'))
print(bot.get_response('Show me the law of cosines.'))