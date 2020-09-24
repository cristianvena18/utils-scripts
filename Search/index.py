import webbrowser
import os
from googletrans import Translator
from googlesearch import search
import wikipedia
import requests
from tkinter import Tk, Label, Button, Entry
import pyttsx3

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title('Executer')
        self.window.geometry('300x200+10+20')
        self.btn = Button(self.window, text='Close', fg='blue')
        self.btn.place(x=80, y=150)
        self.btn.bind('<Button-1>', self.runCommand)
        self.entry = Entry(self.window, text='Run command...', bd=5)
        self.entry.place(x=80, y=100)
        self.entry.bind('<Enter>', self.runCommand)
        self.center()
        self.entry.focus()
        self.window.mainloop()


    def center(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        frm_width = self.window.winfo_rootx() - self.window.winfo_x()
        win_width = width + 2 * frm_width
        height = self.window.winfo_height()
        titlebar_height = self.window.winfo_rooty() - self.window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.window.winfo_screenwidth() // 2 - win_width // 2
        y = self.window.winfo_screenheight() // 2 - win_height // 2
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.deiconify()

    def open_browser(self, search_query):
        search_results = search(search_query)
        if 'https://' in search_results[0]:
            webbrowser.open(search_results[0])
        else:
            for result in search_results:
                if 'https://' in result:
                    webbrowser.open(result)
                    break

    def search_on_wikipedia(self, search_query):
        wikipedia.set_lang("es")
        searched = wikipedia.summary(search_query)
        self.label = Label(self.window, text=searched[0:100:], fg='black', font=("Helvetica", 12))
        self.label.place(x=10, y=10)
        self.window.geometry('800x200+10+20')
        self.center()
        
    def translate(self, text):
        translator = Translator()
        idiom = translator.detect(text)
        translated = ''
        if 'en' in idiom.lang:
            translated = translator.translate(text, src=idiom.lang, dest='es')
        elif 'es' in idiom.lang:
            translated = translator.translate(text, src=idiom.lang, dest='en')
        else:
            translated = translator.translate(text, src=idiom.lang, dest='es')
        self.label = Label(self.window, text=translated.text, fg='black', font=("Helvetica", 12))
        self.label.place(x=10, y=10)
        self.window.geometry('800x200+10+20')
        self.center()

    def open_application(self, name):
        os.popen(name)

    def sendWhatsappMessage(self, phoneNumber, text):
        webbrowser.open('https://web.whatsapp.com/send?phone={0}&text={1}'.format(phoneNumber, text))

    def playMusic(self, query):
        """Will play video on following topic, takes about 10 to 15 seconds to load"""
        url = 'https://www.youtube.com/results?q=' + query
        count = 0
        cont = requests.get(url)
        data = cont.content
        data = str(data)
        lst = data.split('"')
        for i in lst:
            count+=1
            if i == 'WEB_PAGE_TYPE_WATCH':
                break
        if lst[count-5] == "/results":
            raise Exception("No video found.")

        #print("Videos found, opening most recent video")
        webbrowser.open("https://www.youtube.com"+lst[count-5])
        return "https://www.youtube.com"+lst[count-5]

    def runCommand(self, event):
        command = self.entry.get()

        if 'run:' in command:
            self.open_application(command.split(':')[1])
            self.window.destroy()
        elif 'search:' in command:
            self.open_browser(command.split(':')[1])
            self.window.destroy()
        elif 'info:' in command:
            self.search_on_wikipedia(command.split(':')[1])
            #self.window.destroy()
        elif 'send:' in command:
            self.sendWhatsappMessage('+543562521617', 'hola, probando mandar un mensaje desde el script')
            self.window.destroy()
        elif 'music:' in command:
            self.playMusic(command.split(':')[1])
            self.window.destroy()
        elif 'trans:' in command:
            self.translate(command.split(':')[1])
        else:
            print('not found command')

myWindow = App()
