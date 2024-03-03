#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Dec 11, 2022 05:45:38 PM EST  platform: Darwin
import sys
import tkinter as tk
import tkinter.ttk as ttk
#
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
#
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
#
def set_Tk_var():
    global check1
    check1 = tk.IntVar()
    global check2
    check2 = tk.IntVar()
    global check3
    check3 = tk.IntVar()
    global check4
    check4 = tk.IntVar()
    global check5
    check5 = tk.IntVar()
    global check6
    check6 = tk.IntVar()
    global check7
    check7 = tk.IntVar()
    global check8
    check8 = tk.IntVar()
    global check9
    check9 = tk.IntVar()
    global check10
    check10 = tk.IntVar()
    global check11
    check11 = tk.IntVar()
    global check12
    check12 = tk.IntVar()
    global check13
    check13 = tk.IntVar()
    global check14
    check14 = tk.IntVar()
    global check15
    check15 = tk.IntVar()
    global check16
    check16 = tk.IntVar()
    global check17
    check17 = tk.IntVar()
    global check18
    check18 = tk.IntVar()
    global check19
    check19 = tk.IntVar()
    global check20
    check20 = tk.IntVar()
    global check21
    check21 = tk.IntVar()
    global check22
    check22 = tk.IntVar()
    global check23
    check23 = tk.IntVar()
    global check24
    check24 = tk.IntVar()
    global check25
    check25 = tk.IntVar()
    global check26
    check26 = tk.IntVar()
    global check27
    check27 = tk.IntVar()
    global check28
    check28 = tk.IntVar()
    global check29
    check29 = tk.IntVar()
    global check30
    check30 = tk.IntVar()
    global check31
    check31 = tk.IntVar()
    global check32
    check32 = tk.IntVar()
#
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    set_Tk_var()
    top = window_main(root)
    init(root, top)
    root.mainloop()
w = None
def create_window_main(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_window_main(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    set_Tk_var()
    top = window_main (w)
    init(w, top, *args, **kwargs)
    return (w, top)
def destroy_window_main():
    global w
    w.destroy()
    w = None
class window_main:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        top.geometry("450x600+525+199")
        top.minsize(450, 600)
        top.maxsize(450, 600)
        top.resizable(0,  0)
        top.title("Vital Config to Hex")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.hex_value = tk.Label(top,font=("Arial",25))
        self.hex_value.place(relx=0.333, rely=0.05, height=42, width=150)
        self.hex_value.configure(background="#d9d9d9")
        self.hex_value.configure(foreground="#000000")
        def check_buttons():
            button_list = [check1,check2,check3,check4,check5,check6,check7,check8,check9,check10,check11,check12,check13,check14,check15,check16,check17,check18,check19,check20,check21,check22,check23,check24,check25,check26,check27,check28,check29,check30,check31,check32,]
            result = []
            for button in button_list:
                if button.get() == 1:
                    result.append('1')
                elif button.get() == 0:
                    result.append('0')
            result = ''.join(result)
            groups = []
            while len(result) > 0:
                groups.append(result[:4])
                result = result[4:]
            def bin_to_hex(inp):
                total = 0
                # split the string into a list of 4 characters
                inp = list(inp)
                # enumerate the reversed copy of the input string
                for ind,i in enumerate(reversed(inp)):
                    exp = 2 ** ind
                    if i == '1':
                        total += exp
                    else:
                        continue
                return total
            answer = []
            for group in groups:
                answer.append(bin_to_hex(group))
            hex = '0123456789ABCDEF'
            hex_dict = {}
            for ind,i in enumerate(hex):
                hex_dict[ind] = i
            # go through the 'answer' variable and compare to the hex_dict
            final_answer = []
            for i in answer:
                final_answer.append(hex_dict[i])
            final_answer = ''.join(final_answer)
            self.hex_value.configure(text=final_answer)
        self.VS1 = tk.Checkbutton(top)
        self.VS1.place(relx=0.067, rely=0.133, relheight=0.053, relwidth=0.262)
        self.VS1.configure(activebackground="#ececec")
        self.VS1.configure(activeforeground="#000000")
        self.VS1.configure(background="#d9d9d9")
        self.VS1.configure(foreground="#000000")
        self.VS1.configure(highlightbackground="#d9d9d9")
        self.VS1.configure(highlightcolor="black")
        self.VS1.configure(justify='left')
        self.VS1.configure(text='''Vital Setting 1''')
        self.VS1.configure(variable=check1)
        self.VS1.configure(command=check_buttons)
        self.VS2 = tk.Checkbutton(top)
        self.VS2.place(relx=0.067, rely=0.183, relheight=0.053, relwidth=0.262)
        self.VS2.configure(activebackground="#ececec")
        self.VS2.configure(activeforeground="#000000")
        self.VS2.configure(background="#d9d9d9")
        self.VS2.configure(foreground="#000000")
        self.VS2.configure(highlightbackground="#d9d9d9")
        self.VS2.configure(highlightcolor="black")
        self.VS2.configure(justify='left')
        self.VS2.configure(text='''Vital Setting 2''')
        self.VS2.configure(variable=check2)
        self.VS2.configure(command=check_buttons)
        self.VS3 = tk.Checkbutton(top)
        self.VS3.place(relx=0.067, rely=0.233, relheight=0.053, relwidth=0.262)
        self.VS3.configure(activebackground="#ececec")
        self.VS3.configure(activeforeground="#000000")
        self.VS3.configure(background="#d9d9d9")
        self.VS3.configure(foreground="#000000")
        self.VS3.configure(highlightbackground="#d9d9d9")
        self.VS3.configure(highlightcolor="black")
        self.VS3.configure(justify='left')
        self.VS3.configure(text='''Vital Setting 3''')
        self.VS3.configure(variable=check3)
        self.VS3.configure(command=check_buttons)
        self.VS4 = tk.Checkbutton(top)
        self.VS4.place(relx=0.067, rely=0.283, relheight=0.053, relwidth=0.262)
        self.VS4.configure(activebackground="#ececec")
        self.VS4.configure(activeforeground="#000000")
        self.VS4.configure(background="#d9d9d9")
        self.VS4.configure(foreground="#000000")
        self.VS4.configure(highlightbackground="#d9d9d9")
        self.VS4.configure(highlightcolor="black")
        self.VS4.configure(justify='left')
        self.VS4.configure(text='''Vital Setting 4''')
        self.VS4.configure(variable=check4)
        self.VS4.configure(command=check_buttons)
        self.VS5 = tk.Checkbutton(top)
        self.VS5.place(relx=0.067, rely=0.333, relheight=0.053, relwidth=0.262)
        self.VS5.configure(activebackground="#ececec")
        self.VS5.configure(activeforeground="#000000")
        self.VS5.configure(background="#d9d9d9")
        self.VS5.configure(foreground="#000000")
        self.VS5.configure(highlightbackground="#d9d9d9")
        self.VS5.configure(highlightcolor="black")
        self.VS5.configure(justify='left')
        self.VS5.configure(text='''Vital Setting 5''')
        self.VS5.configure(variable=check5)
        self.VS5.configure(command=check_buttons)
        self.VS6 = tk.Checkbutton(top)
        self.VS6.place(relx=0.067, rely=0.383, relheight=0.053, relwidth=0.262)
        self.VS6.configure(activebackground="#ececec")
        self.VS6.configure(activeforeground="#000000")
        self.VS6.configure(background="#d9d9d9")
        self.VS6.configure(foreground="#000000")
        self.VS6.configure(highlightbackground="#d9d9d9")
        self.VS6.configure(highlightcolor="black")
        self.VS6.configure(justify='left')
        self.VS6.configure(text='''Vital Setting 6''')
        self.VS6.configure(variable=check6)
        self.VS6.configure(command=check_buttons)
        self.VS7 = tk.Checkbutton(top)
        self.VS7.place(relx=0.067, rely=0.433, relheight=0.053, relwidth=0.262)
        self.VS7.configure(activebackground="#ececec")
        self.VS7.configure(activeforeground="#000000")
        self.VS7.configure(background="#d9d9d9")
        self.VS7.configure(foreground="#000000")
        self.VS7.configure(highlightbackground="#d9d9d9")
        self.VS7.configure(highlightcolor="black")
        self.VS7.configure(justify='left')
        self.VS7.configure(text='''Vital Setting 7''')
        self.VS7.configure(variable=check7)
        self.VS7.configure(command=check_buttons)
        self.VS8 = tk.Checkbutton(top)
        self.VS8.place(relx=0.067, rely=0.483, relheight=0.053, relwidth=0.262)
        self.VS8.configure(activebackground="#ececec")
        self.VS8.configure(activeforeground="#000000")
        self.VS8.configure(background="#d9d9d9")
        self.VS8.configure(foreground="#000000")
        self.VS8.configure(highlightbackground="#d9d9d9")
        self.VS8.configure(highlightcolor="black")
        self.VS8.configure(justify='left')
        self.VS8.configure(text='''Vital Setting 8''')
        self.VS8.configure(variable=check8)
        self.VS8.configure(command=check_buttons)
        self.VS9 = tk.Checkbutton(top)
        self.VS9.place(relx=0.067, rely=0.533, relheight=0.04, relwidth=0.262)
        self.VS9.configure(activebackground="#ececec")
        self.VS9.configure(activeforeground="#000000")
        self.VS9.configure(background="#d9d9d9")
        self.VS9.configure(foreground="#000000")
        self.VS9.configure(highlightbackground="#d9d9d9")
        self.VS9.configure(highlightcolor="black")
        self.VS9.configure(justify='left')
        self.VS9.configure(text='''Vital Setting 9''')
        self.VS9.configure(variable=check9)
        self.VS9.configure(command=check_buttons)
        self.VS10 = tk.Checkbutton(top)
        self.VS10.place(relx=0.067, rely=0.583, relheight=0.04, relwidth=0.278)
        self.VS10.configure(activebackground="#ececec")
        self.VS10.configure(activeforeground="#000000")
        self.VS10.configure(background="#d9d9d9")
        self.VS10.configure(foreground="#000000")
        self.VS10.configure(highlightbackground="#d9d9d9")
        self.VS10.configure(highlightcolor="black")
        self.VS10.configure(justify='left')
        self.VS10.configure(text='''Vital Setting 10''')
        self.VS10.configure(variable=check10)
        self.VS10.configure(command=check_buttons)
        self.VS11 = tk.Checkbutton(top)
        self.VS11.place(relx=0.067, rely=0.633, relheight=0.04, relwidth=0.278)
        self.VS11.configure(activebackground="#ececec")
        self.VS11.configure(activeforeground="#000000")
        self.VS11.configure(background="#d9d9d9")
        self.VS11.configure(foreground="#000000")
        self.VS11.configure(highlightbackground="#d9d9d9")
        self.VS11.configure(highlightcolor="black")
        self.VS11.configure(justify='left')
        self.VS11.configure(text='''Vital Setting 11''')
        self.VS11.configure(variable=check11)
        self.VS11.configure(command=check_buttons)
        self.VS12 = tk.Checkbutton(top)
        self.VS12.place(relx=0.067, rely=0.683, relheight=0.04, relwidth=0.278)
        self.VS12.configure(activebackground="#ececec")
        self.VS12.configure(activeforeground="#000000")
        self.VS12.configure(background="#d9d9d9")
        self.VS12.configure(foreground="#000000")
        self.VS12.configure(highlightbackground="#d9d9d9")
        self.VS12.configure(highlightcolor="black")
        self.VS12.configure(justify='left')
        self.VS12.configure(text='''Vital Setting 12''')
        self.VS12.configure(variable=check12)
        self.VS12.configure(command=check_buttons)
        self.VS13 = tk.Checkbutton(top)
        self.VS13.place(relx=0.067, rely=0.733, relheight=0.04, relwidth=0.278)
        self.VS13.configure(activebackground="#ececec")
        self.VS13.configure(activeforeground="#000000")
        self.VS13.configure(background="#d9d9d9")
        self.VS13.configure(foreground="#000000")
        self.VS13.configure(highlightbackground="#d9d9d9")
        self.VS13.configure(highlightcolor="black")
        self.VS13.configure(justify='left')
        self.VS13.configure(text='''Vital Setting 13''')
        self.VS13.configure(variable=check13)
        self.VS13.configure(command=check_buttons)
        self.VS14 = tk.Checkbutton(top)
        self.VS14.place(relx=0.067, rely=0.783, relheight=0.04, relwidth=0.278)
        self.VS14.configure(activebackground="#ececec")
        self.VS14.configure(activeforeground="#000000")
        self.VS14.configure(background="#d9d9d9")
        self.VS14.configure(foreground="#000000")
        self.VS14.configure(highlightbackground="#d9d9d9")
        self.VS14.configure(highlightcolor="black")
        self.VS14.configure(justify='left')
        self.VS14.configure(text='''Vital Setting 14''')
        self.VS14.configure(variable=check14)
        self.VS14.configure(command=check_buttons)
        self.VS15 = tk.Checkbutton(top)
        self.VS15.place(relx=0.067, rely=0.833, relheight=0.04, relwidth=0.278)
        self.VS15.configure(activebackground="#ececec")
        self.VS15.configure(activeforeground="#000000")
        self.VS15.configure(background="#d9d9d9")
        self.VS15.configure(foreground="#000000")
        self.VS15.configure(highlightbackground="#d9d9d9")
        self.VS15.configure(highlightcolor="black")
        self.VS15.configure(justify='left')
        self.VS15.configure(text='''Vital Setting 15''')
        self.VS15.configure(variable=check15)
        self.VS15.configure(command=check_buttons)
        self.VS16 = tk.Checkbutton(top)
        self.VS16.place(relx=0.067, rely=0.883, relheight=0.04, relwidth=0.284)
        self.VS16.configure(activebackground="#ececec")
        self.VS16.configure(activeforeground="#000000")
        self.VS16.configure(background="#d9d9d9")
        self.VS16.configure(foreground="#000000")
        self.VS16.configure(highlightbackground="#d9d9d9")
        self.VS16.configure(highlightcolor="black")
        self.VS16.configure(justify='left')
        self.VS16.configure(text='''Vital Setting 16''')
        self.VS16.configure(variable=check16)
        self.VS16.configure(command=check_buttons)
        self.VS17 = tk.Checkbutton(top)
        self.VS17.place(relx=0.644, rely=0.133, relheight=0.053, relwidth=0.284)
        self.VS17.configure(activebackground="#ececec")
        self.VS17.configure(activeforeground="#000000")
        self.VS17.configure(background="#d9d9d9")
        self.VS17.configure(foreground="#000000")
        self.VS17.configure(highlightbackground="#d9d9d9")
        self.VS17.configure(highlightcolor="black")
        self.VS17.configure(justify='left')
        self.VS17.configure(text='''Vital Setting 17''')
        self.VS17.configure(variable=check17)
        self.VS17.configure(command=check_buttons)
        self.VS18 = tk.Checkbutton(top)
        self.VS18.place(relx=0.644, rely=0.183, relheight=0.053, relwidth=0.282)
        self.VS18.configure(activebackground="#ececec")
        self.VS18.configure(activeforeground="#000000")
        self.VS18.configure(background="#d9d9d9")
        self.VS18.configure(foreground="#000000")
        self.VS18.configure(highlightbackground="#d9d9d9")
        self.VS18.configure(highlightcolor="black")
        self.VS18.configure(justify='left')
        self.VS18.configure(text='''Vital Setting 18''')
        self.VS18.configure(variable=check18)
        self.VS18.configure(command=check_buttons)
        self.VS19 = tk.Checkbutton(top)
        self.VS19.place(relx=0.644, rely=0.233, relheight=0.053, relwidth=0.282)
        self.VS19.configure(activebackground="#ececec")
        self.VS19.configure(activeforeground="#000000")
        self.VS19.configure(background="#d9d9d9")
        self.VS19.configure(foreground="#000000")
        self.VS19.configure(highlightbackground="#d9d9d9")
        self.VS19.configure(highlightcolor="black")
        self.VS19.configure(justify='left')
        self.VS19.configure(text='''Vital Setting 19''')
        self.VS19.configure(variable=check19)
        self.VS19.configure(command=check_buttons)
        self.VS20 = tk.Checkbutton(top)
        self.VS20.place(relx=0.644, rely=0.283, relheight=0.053, relwidth=0.282)
        self.VS20.configure(activebackground="#ececec")
        self.VS20.configure(activeforeground="#000000")
        self.VS20.configure(background="#d9d9d9")
        self.VS20.configure(foreground="#000000")
        self.VS20.configure(highlightbackground="#d9d9d9")
        self.VS20.configure(highlightcolor="black")
        self.VS20.configure(justify='left')
        self.VS20.configure(text='''Vital Setting 20''')
        self.VS20.configure(variable=check20)
        self.VS20.configure(command=check_buttons)
        self.VS21 = tk.Checkbutton(top)
        self.VS21.place(relx=0.644, rely=0.333, relheight=0.04, relwidth=0.282)
        self.VS21.configure(activebackground="#ececec")
        self.VS21.configure(activeforeground="#000000")
        self.VS21.configure(background="#d9d9d9")
        self.VS21.configure(foreground="#000000")
        self.VS21.configure(highlightbackground="#d9d9d9")
        self.VS21.configure(highlightcolor="black")
        self.VS21.configure(justify='left')
        self.VS21.configure(text='''Vital Setting 21''')
        self.VS21.configure(variable=check21)
        self.VS21.configure(command=check_buttons)
        self.VS22 = tk.Checkbutton(top)
        self.VS22.place(relx=0.644, rely=0.383, relheight=0.04, relwidth=0.282)
        self.VS22.configure(activebackground="#ececec")
        self.VS22.configure(activeforeground="#000000")
        self.VS22.configure(background="#d9d9d9")
        self.VS22.configure(foreground="#000000")
        self.VS22.configure(highlightbackground="#d9d9d9")
        self.VS22.configure(highlightcolor="black")
        self.VS22.configure(justify='left')
        self.VS22.configure(text='''Vital Setting 22''')
        self.VS22.configure(variable=check22)
        self.VS22.configure(command=check_buttons)
        self.VS23 = tk.Checkbutton(top)
        self.VS23.place(relx=0.644, rely=0.433, relheight=0.04, relwidth=0.282)
        self.VS23.configure(activebackground="#ececec")
        self.VS23.configure(activeforeground="#000000")
        self.VS23.configure(background="#d9d9d9")
        self.VS23.configure(foreground="#000000")
        self.VS23.configure(highlightbackground="#d9d9d9")
        self.VS23.configure(highlightcolor="black")
        self.VS23.configure(justify='left')
        self.VS23.configure(text='''Vital Setting 23''')
        self.VS23.configure(variable=check23)
        self.VS23.configure(command=check_buttons)
        self.VS24 = tk.Checkbutton(top)
        self.VS24.place(relx=0.644, rely=0.483, relheight=0.04, relwidth=0.282)
        self.VS24.configure(activebackground="#ececec")
        self.VS24.configure(activeforeground="#000000")
        self.VS24.configure(background="#d9d9d9")
        self.VS24.configure(foreground="#000000")
        self.VS24.configure(highlightbackground="#d9d9d9")
        self.VS24.configure(highlightcolor="black")
        self.VS24.configure(justify='left')
        self.VS24.configure(text='''Vital Setting 24''')
        self.VS24.configure(variable=check24)
        self.VS24.configure(command=check_buttons)
        self.VS25 = tk.Checkbutton(top)
        self.VS25.place(relx=0.644, rely=0.533, relheight=0.04, relwidth=0.282)
        self.VS25.configure(activebackground="#ececec")
        self.VS25.configure(activeforeground="#000000")
        self.VS25.configure(background="#d9d9d9")
        self.VS25.configure(foreground="#000000")
        self.VS25.configure(highlightbackground="#d9d9d9")
        self.VS25.configure(highlightcolor="black")
        self.VS25.configure(justify='left')
        self.VS25.configure(text='''Vital Setting 25''')
        self.VS25.configure(variable=check25)
        self.VS25.configure(command=check_buttons)
        self.VS26 = tk.Checkbutton(top)
        self.VS26.place(relx=0.644, rely=0.583, relheight=0.04, relwidth=0.282)
        self.VS26.configure(activebackground="#ececec")
        self.VS26.configure(activeforeground="#000000")
        self.VS26.configure(background="#d9d9d9")
        self.VS26.configure(foreground="#000000")
        self.VS26.configure(highlightbackground="#d9d9d9")
        self.VS26.configure(highlightcolor="black")
        self.VS26.configure(justify='left')
        self.VS26.configure(text='''Vital Setting 26''')
        self.VS26.configure(variable=check26)
        self.VS26.configure(command=check_buttons)
        self.VS27 = tk.Checkbutton(top)
        self.VS27.place(relx=0.644, rely=0.633, relheight=0.04, relwidth=0.282)
        self.VS27.configure(activebackground="#ececec")
        self.VS27.configure(activeforeground="#000000")
        self.VS27.configure(background="#d9d9d9")
        self.VS27.configure(foreground="#000000")
        self.VS27.configure(highlightbackground="#d9d9d9")
        self.VS27.configure(highlightcolor="black")
        self.VS27.configure(justify='left')
        self.VS27.configure(text='''Vital Setting 27''')
        self.VS27.configure(variable=check27)
        self.VS27.configure(command=check_buttons)
        self.VS28 = tk.Checkbutton(top)
        self.VS28.place(relx=0.644, rely=0.683, relheight=0.04, relwidth=0.282)
        self.VS28.configure(activebackground="#ececec")
        self.VS28.configure(activeforeground="#000000")
        self.VS28.configure(background="#d9d9d9")
        self.VS28.configure(foreground="#000000")
        self.VS28.configure(highlightbackground="#d9d9d9")
        self.VS28.configure(highlightcolor="black")
        self.VS28.configure(justify='left')
        self.VS28.configure(text='''Vital Setting 28''')
        self.VS28.configure(variable=check28)
        self.VS28.configure(command=check_buttons)
        self.VS29 = tk.Checkbutton(top)
        self.VS29.place(relx=0.644, rely=0.733, relheight=0.04, relwidth=0.282)
        self.VS29.configure(activebackground="#ececec")
        self.VS29.configure(activeforeground="#000000")
        self.VS29.configure(background="#d9d9d9")
        self.VS29.configure(foreground="#000000")
        self.VS29.configure(highlightbackground="#d9d9d9")
        self.VS29.configure(highlightcolor="black")
        self.VS29.configure(justify='left')
        self.VS29.configure(text='''Vital Setting 29''')
        self.VS29.configure(variable=check29)
        self.VS29.configure(command=check_buttons)
        self.VS30 = tk.Checkbutton(top)
        self.VS30.place(relx=0.644, rely=0.783, relheight=0.04, relwidth=0.282)
        self.VS30.configure(activebackground="#ececec")
        self.VS30.configure(activeforeground="#000000")
        self.VS30.configure(background="#d9d9d9")
        self.VS30.configure(foreground="#000000")
        self.VS30.configure(highlightbackground="#d9d9d9")
        self.VS30.configure(highlightcolor="black")
        self.VS30.configure(justify='left')
        self.VS30.configure(text='''Vital Setting 30''')
        self.VS30.configure(variable=check30)
        self.VS30.configure(command=check_buttons)
        self.VS31 = tk.Checkbutton(top)
        self.VS31.place(relx=0.644, rely=0.833, relheight=0.04, relwidth=0.282)
        self.VS31.configure(activebackground="#ececec")
        self.VS31.configure(activeforeground="#000000")
        self.VS31.configure(background="#d9d9d9")
        self.VS31.configure(foreground="#000000")
        self.VS31.configure(highlightbackground="#d9d9d9")
        self.VS31.configure(highlightcolor="black")
        self.VS31.configure(justify='left')
        self.VS31.configure(text='''Vital Setting 31''')
        self.VS31.configure(variable=check31)
        self.VS31.configure(command=check_buttons)
        self.VS32 = tk.Checkbutton(top)
        self.VS32.place(relx=0.644, rely=0.883, relheight=0.04, relwidth=0.282)
        self.VS32.configure(activebackground="#ececec")
        self.VS32.configure(activeforeground="#000000")
        self.VS32.configure(background="#d9d9d9")
        self.VS32.configure(foreground="#000000")
        self.VS32.configure(highlightbackground="#d9d9d9")
        self.VS32.configure(highlightcolor="black")
        self.VS32.configure(justify='left')
        self.VS32.configure(text='''Vital Setting 32''')
        self.VS32.configure(variable=check32)
        self.VS32.configure(command=check_buttons)
        #
if __name__ == '__main__':
    vp_start_gui()

