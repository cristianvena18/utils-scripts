import webbrowser
import os
from googlesearch import search
import wikipedia

def open_browser(search_query):
    search_results = search(search_query)
    if 'https://' in search_results[0]:
        webbrowser.open(search_results[0])
    else:
        for result in search_results:
            if 'https://' in result:
                webbrowser.open(result)
                break

def search_on_wikipedia(search_query):
    wikipedia.set_lang("es")
    print(wikipedia.summary(search_query))

def open_application(name):
    os.popen(name)

command = input('what is execute?: ')

if 'run:' in command:
    open_application(command.split(':')[1])
elif 'search:' in command:
    open_browser(command.split(':')[1])
elif 'info:' in command:
    search_on_wikipedia(command.split(':')[1])
else:
    print('not found command')
