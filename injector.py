from os import system


def newword(eng, qor):
    import json
    with open('./dictionary.json', 'r+') as dictfile:
        before = json.load(dictfile)
        
    eng = eng.lower()
    qor = qor.lower()
    
    if eng in before.keys():
        return print('Word already has a definition.')
        
    before[eng] = qor
    before = dict(sorted(before.items(), key=lambda item: item[0]))
    
    with open('./dictionary.json', 'w+') as dictfile:
        json.dump(before, dictfile, indent=4)
    print(f'Added "{eng}" to the dictionary with translation "{qor}"')
        
def sort():
    import json
    with open('./dictionary.json', 'r+') as dictfile:
        d = json.load(dictfile)

    d = dict(sorted(d.items(), key=lambda item: item[0]))
    with open('./dictionary.json', 'w+') as dictfile:
        json.dump(d, dictfile, indent=4)
    
def check(w):
    import json
    with open('./dictionary.json', 'r+') as dictfile:
        d = json.load(dictfile)
        
    if w.lower() in d.keys():
        print(f'Word is defined: {d[w.lower()]}')
    else:
        print('Word has not yet been defined.')
        
def dlength():
    import json
    with open('./dictionary.json', 'r+') as dictfile:
        d = json.load(dictfile)
        
    result = 0
    for i in d.keys(): 
        result += 1
    
    print(result)
    
def otranslate():
    exec(open('translator.py').read())