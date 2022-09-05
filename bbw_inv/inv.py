import json,os,sys
#
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
try:
    inv = {}
    with open(os.path.join(currentdir,'dani.json'),'r') as fhand:
        inv['Dani'] = json.load(fhand)
    with open(os.path.join(currentdir,'dev.json'),'r') as fhand:
        inv['Dev'] = json.load(fhand)
except:
    inv = {}
    inv['Dani'] = {}
    inv['Dev'] = {}
#
running = True
while running:
    name = input(f'scan name> ')
    if name == 'Quit':
        with open(os.path.join(currentdir,'dani.json'),'w') as fhand:
            fhand.write(json.dumps(inv['Dani'],indent=4))
        with open(os.path.join(currentdir,'dev.json'),'w') as fhand:
            fhand.write(json.dumps(inv['Dev'],indent=4))
        running = False
    else:
        upc = input(f'scan barcode> ')
        if upc not in inv[name].keys():
            inv[name][upc] = 1
        else:
            inv[name][upc] += 1