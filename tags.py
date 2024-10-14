import os
dir = 'pythonUebungen'

def showTags(tags):
    tags = tags.split()
    for i in range(len(tags)):
        if tags[i].startswith('#'):
            tags[i] = tags[i][1:]

        
# list all files in the directory
    files = os.listdir(dir)
    # iterate over the list getting each file
    for file in files:
        # open the file and then call .read() to get the text
        if file.startswith('aufgaben') and not file.startswith('aufgabengruppen'):
            
            with open(os.path.join(dir, file),encoding='utf-8') as f:
                text = f.read()
                lines = text.split('\n')
                for k in range(len(lines)-1):
                    zeile = lines[k]
                    ok = lines[k].startswith('<!--')
                    for tag in tags:
                        ok = ok and '#'+tag in zeile
                    if ok:
                        zeile = zeile.strip('<!--')
                        zeile = zeile.strip('-->')
                        zeile = zeile.strip()
                        
                        j = k+1
                        while not 'Aufgabe' in lines[j]:
                            j+=1
                        zeile2 = lines[j].strip('Aufgabe')
                        zeile2 = zeile2.strip()
                        print(f'{zeile2:10s} {zeile}')  


showTags('lineareSuche list')

    


 


