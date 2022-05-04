#This program compares the hash of any number of selected files and reports any files that have different hashes. Useful if you have multiple files with identical names and want to check for duplicates.

def choose_file():
    from tkinter import Tk, filedialog
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    open_file = filedialog.askopenfilename()
    root.destroy()
    return open_file

def change_color(inp):
