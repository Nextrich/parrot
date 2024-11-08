from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from textwrap import wrap
from colorama import init, Fore
import ctypes
import os

#Python tgBotCreator.py
tk = Tk()
tk.geometry("768x860")
tk.title('Telegram Bot Creator')
tk.configure(background='#0080FF')
init()

#----------------------TKinter var----------------------------

langs = ['Start', 'trigger']

variables_message = ('Text', 'If')#'Text', 'If', 'Buttons', 'Input'
state_variables = ''

text_message = ''
if_text = ''

message_name = 'Start'

messages = [['`', '`']]

export_messages = [['`','`']]

export_command = ['']

api = "none"

name = 'Main_file'

variables = ['a']

#----------------------Systems var----------------------------

path = os.getcwd()

#------------------------Frames-------------------------------

menu_frame = Frame(bg='#0080FF')
menu_frame.pack(side=TOP, fill=X)

message_menu_frame = LabelFrame(fg="white", bg='#0080FF', text="Events")
message_menu_frame.pack(side=LEFT)

editor_frame = LabelFrame(fg="white", bg='#0080FF', text="Editor", width=50)
editor_frame.pack(side=RIGHT, fill=Y, padx= 30, pady=60)

#code

def about():
	ctypes.windll.user32.MessageBoxW(0, """This program is designed to simplify the work when creating telegram bots based on visual programming. Created by Mr_next.""", "About programm", 0)

def edit_variable(event):
	global text_message, if_text, message_name, langs, messages
	select = edit_message.get()
	if select == "Text":
		message_text.pack_forget()

		entry_label.pack(pady=20)
		entry_message.pack()
		entry_button.pack(pady=20)
		message_text.pack(pady=10)

		if_message.pack_forget()
		if_label.pack_forget()
		if_button.pack_forget()

		for b in messages:
			if message_name in b[0]:
				if "//" in b[1]:
					message_text['text'] = "Текст сообщения: " + b[1][:-2]
					entry_message.delete(0, END)
					entry_message.insert(0, b[1][:-2])
					return message_name
				elif "{" in b[1] and "}" in b[1]:
					message_text['text'] = "Текст сообщения: " + b[1]
					entry_message.delete(0, END)
					entry_message.insert(0, b[1])
		else: 
			message_text['text'] = "Текст сообщения: "
			entry_message.delete(0, END)

	elif select == "If":
		message_text.pack_forget()

		if_label.pack(pady=20)
		if_message.pack()
		if_button.pack(pady=20)
		message_text.pack(pady=10)

		entry_message.pack_forget()
		entry_label.pack_forget()
		entry_button.pack_forget()

		for b in messages:
			if message_name in b[0]:
				if "||" in b[1]:
					message_text['text'] = "Текст сообщения: " + b[1][:-2]
					if_message.delete(0, END)
					if_message.insert(0, b[1][:-2])
					return message_name
		else: 
			message_text['text'] = "Текст сообщения: "
			if_message.delete(0, END)
		
def save_text():
	global text_message, if_text, message_name, messages, a

	select = edit_message.get()
	if select == "Text":
		text_message = entry_message.get()
		message_text['text'] = "Текст сообщения: " + text_message
		for i in messages:
			print(i)
			if i[0] == message_name:
				if "{" in i[1] and "}" in i[1]:
						i[1] = text_message
						return a
				elif "[" in i[1] and "]" in i[1]:
						i[1] = text_message
						return a
				elif "//" in i[1]:
					print(i[1])
					i[1] = text_message + "//"
					print("before: " + i[1])
					return a

			else:
				pass
		if "{" in text_message and "}" in text_message:
						a = [message_name, text_message]
						messages.append(a)
						print(a)
						return a
		if "[" in text_message and "]" in text_message:
						a = [message_name, text_message]
						messages.append(a)
						print(a)
						return a
		a = [message_name, text_message+"//"]
		messages.append(a)
		print(a)

	elif select == "If":
		if_text = if_message.get()
		message_text['text'] = "Текст сообщения: " + if_text
		for i in messages:
			print(i)
			if i[0] == message_name:
				if "||" in i[1]:
					print(i[1])
					i[1] = if_text + "||"
					print("before: " + i[1])
					return a
		a = [message_name, if_text+"||"]
		messages.append(a)
		print(messages)

def name_of_message(event):
	global text_message, if_text, message_name, langs, messages

	num_message = listbox.curselection()
	message_name = listbox.get(num_message)
	a = message_name
	if message_name != "":
		label_message['text'] = message_name

	select = edit_message.get()
	if select == "Text":
		for b in messages:
			if message_name in b[0]:
				if "//" in b[1]:
					message_text['text'] = "Текст сообщения: " + b[1][:-2]
					entry_message.delete(0, END)
					entry_message.insert(0, b[1][:-2])
					return message_name
		else: 
			message_text['text'] = "Текст сообщения: "
			entry_message.delete(0, END)

	elif select == "If":
		for b in messages:
			if message_name in b[0]:
				if "||" in b[1]:
					message_text['text'] = "Текст сообщения: " + b[1][:-2]
					if_message.delete(0, END)
					if_message.insert(0, b[1][:-2])
					return message_name
		else: 
			message_text['text'] = "Текст сообщения: "
			if_message.delete(0, END)

def new_message():

	def add_new_message():
		global langs

		b = new_enter.get()
		listbox.insert(0, b)
		c = len(langs)
		langs.insert(c+1, b)
		print(langs)
		new.destroy()

	new = Toplevel()
	new.geometry('300x150')
	new.configure(background='#0080FF')
	new_label = Label(new, text="Enter the name of the message:", fg="white", bg="#0080FF")
	new_enter = Entry(new)
	new_button = Button(new, text="Add", fg="white", bg="#009999", command=add_new_message)
	new_label.pack(pady=5)
	new_enter.pack(pady=5)
	new_button.pack(pady=5)

def del_message():
	global langs, message_name

	num_message = listbox.curselection()
	print(num_message)
	listbox.delete(num_message)

	d = message_name
	langs.remove(d)
	print(langs)

def config():

	def aply_config():
		global api, name
		api = conf_api_entry.get()
		name = conf_name_entry.get()
		name = name.replace(" ", "")

		if name == "":
			name = 'Main_file'

		print(Fore.RED + "API: " + api)
		print(Fore.RED + "Name: " + name)

		ctypes.windll.user32.MessageBoxW(0, """Configuration saved.""", "Configure", 0)

		conf.destroy()

	conf = Toplevel()
	conf.geometry('400x200')
	conf.configure(background='#0080FF')

	conf_api_frame = LabelFrame(conf, fg="white", bg='#0080FF', text="API")
	conf_api_frame.pack(side=LEFT, padx=15)

	conf_name_frame = LabelFrame(conf, fg="white", bg='#0080FF', text="Name")
	conf_name_frame.pack(side=RIGHT, padx=15)

	config_label  = Label(conf, text="Config", fg="white", bg="#0080FF")

	conf_api_label = Label(conf_api_frame, text="Bot API:", fg="white", bg="#0080FF")
	conf_api_entry = Entry(conf_api_frame)
	conf_api_entry.insert(0, api)

	conf_name_label = Label(conf_name_frame, text="Bot name:", fg="white", bg="#0080FF")
	conf_name_entry = Entry(conf_name_frame)
	conf_name_entry.insert(0, name)

	conf_btn = Button(conf, text="Aply", fg="white", bg="#009999", width=20, command=aply_config)

	config_label.pack(pady=20)
	conf_api_label.pack()
	conf_api_entry.pack(pady=5, padx=5)
	conf_name_label.pack()
	conf_name_entry.pack(pady=5, padx=5)
	conf_btn.pack(side=BOTTOM, pady=20)


def export():
	global langs, messages, export_command, api, name, variables

	print("GO GO GO")

	global_variables = "global "
	checker_variables = ['']
	checker_output_variables = ['']

	api = api.replace(" ", "")
	if api == "" or api == "none":
		ctypes.windll.user32.MessageBoxW(0, """Please, enter API in config!""", "Warning!", 0)
		config()
		return
	export_command = ['']
	total = ['']
	exp_comm_text = ''
	export_file_text = ""
	messages.remove(messages[0])
	for a in langs:
		for b in messages:
			print(a + ", rr, " + b[0])
			if b[0] == a:
				b[0] = "_"+b[0]+"_"
				export_messages.append(b)
				print("Совпало: a  -" + a + ", b - ", b)
				
			else: pass

	print("Процесс отбора окончен.")
	print("Выделено: ")
	print(export_messages)
	print(Fore.GREEN + "Сборка и подготовка переменных:")
	export_messages.remove(export_messages[0])
	for c in export_messages:
		if "//" in c[1]:
			export_command.append("		bot.send_message(message.chat.id,  text='" + c[1][:-2] + "') #" + "_" + c[0] + "_" + " msg1")
			print(Fore.GREEN + "Сошлась комманда вывода текста:")
			print(export_command)
		if "{" in c[1] and "}" in c[1]:
			export_command.append("		bot.send_message(message.chat.id,  text='" + c[1][:-1] + "') #" + "_" + c[0] + "_" + " msg2")
			variables.append("_" + c[0] + "_")
			print(Fore.GREEN + "Сошлась комманда ввода переменной:")
			print(export_command)
			print("Добавлена переменная:")
			print(variables)
		if "[" in c[1] and "]" in c[1]:
			export_command.append("		bot.send_message(message.chat.id,  text=" + c[1][:-1] + ") #" + "_" + c[0] + "_" + " msg3")
			print(Fore.GREEN + "Сошлась комманда вывода переменной:")
			print(export_command)
	for f in variables:
		f = f.replace("_","")

		if global_variables == "global " and variables[0] == "": global_variables = ""
		if global_variables == "global ":
			global_variables = "global " + f
			print(Fore.RED + "Открытие сессии global: " + f)
		else: 
			global_variables = global_variables + "," + f
			print(Fore.RED + "Продолжение сессии global: " + f)
			print(Fore.RED + "Global: " + global_variables)

		if variables[0] == "":export_variables = "" 
		else: export_variables = "\n" + f + " = ''"
	for c in export_messages:
		if "||" in c[1]:
			for d in export_command:
				if c[0] in d:
					print("name: "+c[0]+", function:"+d)
					if "{" in d:
						print("Найдена скобка!")
						for g in variables:
							if g in d:
								for h in checker_variables:
									if g in checker_variables: 
										print(Fore.YELLOW + "Ограничитель")
										print(Fore.RED + "variables: " + g + ", cheker: " + h)
										break
									else:
										if g =="a": pass
										else:
											print(Fore.RED + "variables: " + g + ", cheker: " + h)
											d = d.replace("{","")
											g = g.replace("_","")
											d = "	if message.text == '" + c[1][:-2] + "': " + "\n" + d + "\n		@bot.message_handler(content_types=['text'])\n		def input_step(message):\n			" + global_variables + "\n			" + g + " = message.text\n			bot.reply_to(message, f'{message.text}')\n		bot.register_next_step_handler(message, input_step)"
											print(Fore.GREEN + "Команда создана:")
											print(Fore.CYAN + d)
											print(Fore.RED + "Cheker: " + g)
											checker_variables.append(g)
											total.append(d)
					elif "[" in d:

						d = d.replace("[","")
						print("Встретилась переменная")
						d = "	if message.text == '" + c[1][:-2] + "': " + "\n" + d
						print(Fore.GREEN + "Команда вывода переменной создана:")
						print(Fore.CYAN + d)
						total.append(d)
					else:
						c[1].replace("||","")
						d = "	if message.text == '" + c[1][:-2] + "': " + "\n" + d
						print(Fore.GREEN + "Команда создана:")
						print(Fore.CYAN + d)
						total.append(d)
	print(Fore.GREEN + "Итог сборки команд:")
	print(total)
	print(Fore.GREEN + "Начало компиляции скрипта:")
	for e in total:
		exp_comm_text = exp_comm_text + "\n" + e
	print(Fore.GREEN + "Компиляция комманд:")
	print(Fore.YELLOW + exp_comm_text)
	export_file_text = "import telebot\nfrom telebot import types\n\n" + export_variables + "\nbot = telebot.TeleBot('" + api + "')\n@bot.message_handler(content_types=['text'])\n@bot.message_handler(content_types=['text', 'document', 'audio'])\n\ndef startGame(message):\n	" + global_variables + exp_comm_text + "\nbot.polling(none_stop=True, interval=0)"
	print(Fore.GREEN + "Компиляция текста скрипта:")
	print(Fore.YELLOW + export_file_text)
	file = open(name + '.py', "w+")
	file.write(export_file_text)
	file.close()
	print(Fore.GREEN + "Компиляция завершена.")
	print(Fore.MAGENTA + "Скрипт сохранён!")


#visual

label = Label(tk, text="Добро пожаловать!", font = ('Arial Italic', 20), fg="white", bg="#0080FF")
label.pack(pady=20, side=TOP, fill=X)

var = Variable(value=langs)
listbox = Listbox(
    message_menu_frame,
    listvariable=var,
    height=6,
)
listbox.pack(side=TOP, pady=10, padx=10)

add_message_button = Button(message_menu_frame, text="+", fg="white", bg="#009999", command=new_message)
add_message_button.pack(pady=10, expand=True, side=LEFT, fill=BOTH, padx=5)
del_message_button = Button(message_menu_frame, text="-", fg="white", bg="#009999", command=del_message)
del_message_button.pack(pady=10, expand=True, side=RIGHT, fill=BOTH, padx=5)

label_message = Label(editor_frame, text="Start", fg="white", bg="#0080FF")
label_message.pack()
edit_message = ttk.Combobox(editor_frame, textvariable=state_variables, values = variables_message, state="readonly")
edit_message.pack(padx=10, pady=10)

export_button = Button(tk, text="Export", fg="white", bg="#009999", command=export, width=40)
export_button.pack(pady=60, padx=10, side=BOTTOM)

mainmenu = Menu(menu_frame)
mainmenu.configure(background='black')
mainmenu.add_command(label = "Config", command= config)
mainmenu.add_command(label = "About", command= about)
#mainmenu.add_command(label = "Help", command= help_f)
mainmenu.add_command(label = "Exit", command= tk.destroy)
tk.config(menu = mainmenu)

#-----------------------------------If------------------------------------

if_label = Label(editor_frame,text="Введите текст сообщения, на \nкоторое отреагирует бот:", fg="white", bg="#0080FF")
if_message = Entry(editor_frame)
if_button = Button(editor_frame, text="Подтвердить", fg="white", bg="#009999", command=save_text)

#----------------------------------Text-----------------------------------

entry_label = Label(editor_frame,text="Введите текст сообщения:", fg="white", bg="#0080FF")
entry_message = Entry(editor_frame)
entry_button = Button(editor_frame, text="Подтвердить", fg="white", bg="#009999", command=save_text)
message_text = Label(editor_frame, text="Текст сообщения: ", fg="white", bg="#0080FF")

#---------------------------------Button----------------------------------

message_text = Label(editor_frame, text="Текст сообщения: ", fg="white", bg="#0080FF")

edit_message.bind("<<ComboboxSelected>>", edit_variable)
listbox.bind("<<ListboxSelect>>", name_of_message)
tk.mainloop()
