import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token = 'abc442f2600a085d9d89ab984427190cca9443cccd45949099b74d6810745dd0bdf8916a3d29852794d42')
longpoll = VkBotLongPoll(vk_session, 210711428)

def sender(id, text):
	vk_session.method('messages.send',{'chat_id':id, 'message' : text, 'random_id' : 0})


for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW:
		if event.from_chat:
			id = event.chat_id
			msg = event.object.message['text'].lower()
			msg2 = msg[:6]
			krim=msg.find('крым')
			test_list = ['1','2','3','4','5','6','7']
			eg=msg.find('забыл')
			eg2=msg.find('ежедневки')
			eg3=msg.find('не сделал')
			cplin=msg.find('скоро рассвет')
			ili=msg.find('или')
			aya=msg.find('а я хочу')
			gdm=msg.find('где мурат')
			gdm1=msg.find('где мурта')
			spi=msg.find('спи')
			hey=msg.find('хэй')
			hey1=msg.find('хей')
			ser=msg.find('сердце')
			dol=msg.find('пофиг')
			nik=msg.find('никогда')



			if msg == 'да':
					sender(id, 'звезда')
			elif msg == 'адель':
				rand3=random.randint(1,2)
				if rand3==1:
					sender(id, 'Я!')
				if rand3==2:
					sender(id, 'Что?')
				
			elif msg == 'нет':
					sender(id, 'мурата ответ')

			elif (gdm>=0 or gdm1>=0):
					sender(id, 'Мурат в подвале')
			elif (hey>=0 or hey1>=0):
					sender(id, 'ХЭЙ (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧')
					sender(id, 'БРАТ ПРИВЕТ')
					sender(id, 'С ТОГО СВЕТА ШЛЮ ТЕБЕ ПРИВЕТ')
			elif (eg2>=0 and (eg>=0 or eg3>=0)):
				sender (id, 'минус гемы')
			elif cplin>=0:
				sender (id, 'ВЫХОДА НЕТ')
			elif krim>=0:
				sender (id, 'крым наш 🇷🇺')
			elif dol>=0:
				sender (id, 'А МНЕ ДО ЛАМПОЧКИ')
				sender (id, 'ЛА. ЛА-ЛА-ЛА-ЛА')
			elif nik>=0:
				sender (id, 'НУ КОГДА Я БУДУ СЧАСТЛИВ')
				sender (id, 'НУ КОГДА НАЙДУ СВОЙ ДОМ')
				sender (id, 'НУ КОГДА ЖЕ В ЭТОМ МИРЕ МЫ ОСТАНЕМСЯ ВДВОЕМ')
				sender (id, 'НИ-КОГ-ДА (づ◡﹏◡)づ')
			elif ser>=0:
				sender (id, 'И МОЕ СЕРДЦЕ')
				sender (id, 'И МОЕ СЕРДЦЕ ЗА-МЕР-ЛО')

			elif spi>=0:
				sender (id, 'СПИ СПОКОЙНО')
				sender (id, 'СЛОВНО НЕ БЫЛО ВОЙНЫ')
			elif aya>=0:
				sender (id, 'А Я ХОЧУ')
				sender (id, 'А Я ХОЧУ ОПЯТЬ ( ° ∀ ° )')
			


			if msg2 == 'адель ':
				if msg == 'адель привет':
					sender(id, 'Халлоу')
				elif msg == 'адель команды':
					sender(id, 'доступные команды:\n\n[обязательные параметры без скобок] \n(необязательные команды без скобок)\n\nадель выбери [вариант1] или [вариант2]\nадель да или нет (выражение)')
				elif msg[6:16]=='да или нет':
					rand1=random.randint(1,7)
					if rand1==1:
						sender(id, 'Да')
					elif rand1==2:
						sender(id, 'Нет')
					elif rand1==3:
						sender(id, 'Херобрин его знает (￣▽￣)')
					elif rand1==4:
						sender(id, 'Возможно')
					elif rand1==5:
						sender(id, 'Скорее нет чем да')
					elif rand1==6:
						sender(id, 'Маловероятно ┐(￣ヘ￣)┌')
					elif rand1==7:
						sender(id, 'Скорее да чем нет')

				elif msg[6:12]=='выбери':
					if ili<0:
						sender(id, 'И из чего мне выбирать?')
					else:
						rand2=random.randint(1,2)
						if rand2==1:
							otv=msg[13:ili-1]
							sender(id, otv)
						if rand2==2:
							otv=msg[ili+3:]
							sender(id, otv)

				elif msg == 'адель хай':
					sender(id, 'Халлоу')
				elif msg == 'адель халлоу':
					sender(id, ':)))')
				elif msg == 'адель :)':
					sender(id, ':))))))))))')
			
				elif msg == 'адель где билл':
					sender(id, 'В подвале. А что, присоединишься? (￢‿￢ )')
				elif msg == 'адель кто во всем виноват?':
					sender(id, 'Мур- Мур?')
				elif krim>=0:
					b=12
				elif eg>=0:
					b=11
				elif cplin>=0:
					b=10
				else: 
					sender(id, 'Не знаю таке')