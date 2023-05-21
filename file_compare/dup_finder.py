# This program compares the hash of any number of selected files and reports any files that have different hashes.
# Useful if you have multiple files with identical names and want to check for duplicates.
import hashlib,os,sys,traceback
from time import sleep
####
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
####
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
####
files = []
def find_files(path):
    for i in os.listdir(path):
        f = os.path.join(path,i)
        if os.path.isdir(f):
            find_files(f)
        elif os.path.isfile(f):
            files.append(f)
####
print(f'{Messages.Service}Enter directory to search>{Messages.Reset}')
file_path = input()
find_files(file_path)
####
file_dict = {}
for f in files:
    hasher = hashlib.md5()
    with open(f,'rb') as fhand:
        buf = fhand.read()
        hasher.update(buf)
        file_dict[f] = hasher.hexdigest()
####
flip_dict = {}
for k,v in file_dict.items():
    flip_dict.setdefault(v, set()).add(k)
    result = [k for k, v in flip_dict.items() if len(v) > 1]
####
final_dict = {}
for k,v in file_dict.items():
    if v in result:
        final_dict[f'{Messages.Duplicate}{k}{Messages.Reset}'] = Messages.Duplicate+file_dict[k]+Messages.Reset
    elif v not in result:
        final_dict[f'{Messages.Unique}{k}{Messages.Reset}'] = Messages.Unique+file_dict[k]+Messages.Reset
####
print(f'{Messages.Service}Results are shown below. {Messages.Unique}Green text means the file is unique. {Messages.Duplicate}Yellow text means the file is a duplicate.{Messages.Reset}\n')
for i in sorted(final_dict.keys()):
    print(f'{Messages.Service}File name: {i}')
    print(f'{Messages.Service}File hash: {final_dict[i]}\n')
####
with open(os.path.join(currentdir,'dup_finder_log.txt'),'w') as fhand:
    fhand.write(f'LIST OF DUPLICATE FILES:\n')
    for i in sorted(final_dict.keys()):
        if final_dict[i].startswith('\033[93m'):
            fhand.write(f'File path: {i[5:-4]}\n')
            fhand.write(f'File hash: {final_dict[i][8:-7]}\n\n')
    fhand.close()