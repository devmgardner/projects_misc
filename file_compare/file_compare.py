# This program compares the hash of any number of selected files and reports any files that have different hashes.
# Useful if you have multiple files with identical names and want to check for duplicates.
import hashlib,os,sys,traceback

def choose_file_gui():
    from tkinter import Tk, filedialog
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    open_file = filedialog.askopenfilename()
    root.destroy()
    return open_file

def choose_file():
    print(Messages.Service,f'enter complete filepath>',Messages.Reset)
    filename = input(' ')
    try:
        hasher = hashlib.md5()
        with open(filename,'rb') as fhand:
            buf = fhand.read()
            hasher.update(buf)
        return filename
    except Exception as e:
        return [str(e),traceback.format_exc()]

class Messages:
    # ALWAYS AT END OF EVERY PRINT STATEMENT
    Reset = '\033[0m'
    # black foreground, red background
    Error = '\033[30;41m'
    # green foreground, used if file is unique
    Unique = '\033[32m'
    # yellow foreground, used if file is a duplicate
    Duplicate = '\033[93m'
    # blue foreground, used for service messaging
    Service = '\033[34m'

def num_of_files():
    print(Messages.Service,f'enter the number of files you would like to compare>',Messages.Reset)
    num_files = input(' ')
    try:
        num_files = int(num_files)
        return num_files
    except:
        print(Messages.Error,f'Invalid value entered. Please enter an integer 2 or higher.',Messages.Reset)
        quit()

files = []
num = num_of_files()
if num < 2:
    print(Messages.Error,f'Please enter an integer 2 or higher.',Messages.Reset)
    quit()
for i in range(num):
    filename = choose_file()
    if isinstance(filename, list):
        print(Messages.Error,f'Error encountered:\n',filename[0],filename[1],Messages.Reset)
    elif isinstance(filename, str):
        files.append(filename)

#print(files)

file_dict = {}

for f in files:
    hasher = hashlib.md5()
    with open(f,'rb') as fhand:
        buf = fhand.read()
        hasher.update(buf)
        file_dict[f] = hasher.hexdigest()

flip_dict = {}

for k,v in file_dict.items():
    flip_dict.setdefault(v, set()).add(k)
    result = [k for k, v in flip_dict.items() if len(v) > 1]

for k,v in file_dict.items():
    if v in result:
        file_dict[f'{Messages.Duplicate}{k}{Messages.Reset}'] = Messages.Duplicate+file_dict.pop(k)+Messages.Reset
    elif v not in result:
        file_dict[f'{Messages.Unique}{k}{Messages.Reset}'] = Messages.Unique+file_dict.pop(k)+Messages.Reset

print(f'{Messages.Service}Results are shown below. {Messages.Unique}Green text means the file is unique. {Messages.Duplicate}Yellow text means the file is a duplicate.{Messages.Reset}\n')

for i in sorted(file_dict.keys()):
    print(f'{Messages.Service}File name: {i}')
    print(f'{Messages.Service}File hash: {file_dict[i]}\n')
        

#class Colors:
#    class fg:
#        red = '\033[31'
#        blue = '\033[34'
#        green = '\033[32'
#        grey = '\033[37'
#        yellow = '\033[93'
#    class bg:
#        red = ';41'
#        blue = ';44'
#        green = ';42'
#        grey = ';47'
#        yellow = ';103'
#    class reset:
#        reset = '\033[0m'

#print(Colors.fg.red,Colors.bg.yellow,'mtest',Colors.reset.reset)

#print(Messages.Error,'test error message black foreground red background',Messages.Reset)