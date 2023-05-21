import json,os,sys
#
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
room = input(f'enter room name> ')
if not os.path.exists(os.path.join(currentdir,room)):
    os.mkdir(os.path.join(currentdir,room))
try:
    inv = {}
    with open(os.path.join(currentdir,room,'dani.json'),'r') as fhand:
        inv['Dani'] = json.load(fhand)
    with open(os.path.join(currentdir,room,'dev.json'),'r') as fhand:
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
        if len(dani.keys()) > 0:
            with open(os.path.join(currentdir,room,'dani.json'),'w') as fhand:
                fhand.write(json.dumps(inv['Dani'],indent=4))
        if len(dev.keys()) > 0:
            with open(os.path.join(currentdir,room,'dev.json'),'w') as fhand:
                fhand.write(json.dumps(inv['Dev'],indent=4))
        running = False
    else:
        upc = input(f'scan barcode> ')
        if upc not in inv[name].keys():
            inv[name][upc] = 1
        else:
            inv[name][upc] += 1