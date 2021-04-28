import json
from time import sleep

import pyperclip

with open('./dictionary.json', 'r+') as dictfile:
    dictionary = json.load(dictfile)
    
print("What do you want to convert to Qorraxish? Note that this program does not currently support plural words.\nYou can convert a Qorraxish word to a plural by adding the suffix '-M'.")
english = input()

result = ''
for w in english.split():
    if w.lower() in dictionary.keys():
        result += dictionary[w.lower()] + ' '
    else:
        result += f'[{w.lower()}] '

print(result)

try:
    pyperclip.copy(result)
    print('Result copied to clipboard')
except:
    print('Tried to copy the result to your clipboard, but something went wrong.')
    
sleep(60)
