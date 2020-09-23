import webbrowser
import os
from googlesearch import search
import wikipedia
import requests
from tkinter import *

class App:
    def __init__(self, window):
        self.window = window
        self.btn = Button(window, text='Close', fg='blue')
        self.btn.place(x=80, y=100)
        self.entry = Entry(window, text='Run command...', bd=5)
        self.entry.place(x=80, y=150)
        self.entry.bind('<Enter>', self.runCommand)

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
        print(wikipedia.summary(search_query))

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
            self.window.destroy()
        elif 'send:' in command:
            self.sendWhatsappMessage('+543562521617', 'hola, probando mandar un mensaje desde el script')
            self.window.destroy()
        elif 'music:' in command:
            self.playMusic(command.split(':')[1])
            self.window.destroy()
        else:
            print('not found command')
            


window = Tk()
window.title('Executer')
window.geometry('300x200+10+20')
myWindow = App(window)

window.mainloop()