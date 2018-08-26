from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

boter=ChatBot('Bot')
boter.set_trainer(ListTrainer)


for i in os.listdir('C:/Users/vinay krishna/Desktop/pilot project/ChatBot/english/'):
	data=open('C:/Users/vinay krishna/Desktop/pilot project/ChatBot/english/'+i,'r').readlines()
	boter.train(data)


while True:
	message=input("You: ")
	if message.strip()!="bye":
		reply=boter.get_response(message)
		print('ChatBot:',reply)

	if message.strip()=="bye":
		print("ChatBot: Bye")
		break
