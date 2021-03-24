import eel

eel.init("web")

@eel.expose
def bot(place):
	
	a = place
	b = "неверный шифр, повторите ввод! "
	c = "Адрес научной лаборатории: Чусовская, ул. дом 2, 6 этаж!"
	if a == "штаммценозреконимаго":
		return c
	else:
		#return "ошибка! /nпопробуй /nеще раз!"
		return b
	#return place
	

eel.start("main.html", size=(700, 700))
