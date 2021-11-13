from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from automata.fa.dfa import DFA
import os

dfa_file = ""
test_file = ""

states = {} 
alphabet = {} 
initial = ''
finals = {}
transitions = {}

WIDTH = 250
HEIGHT = 250

size = str(WIDTH) + "x" + str(HEIGHT)

root = Tk()
root.geometry(size)
root.title('DFA String Tester')
root.resizable(0,0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

def open_dfa():
    global  dfa_file
    file = askopenfile(initialdir='/', title="Please select a dfa file")
    dfa_file = file.name
    print(dfa_file)
    messagebox.showinfo(title='Selected file', message=file.name)

def open_test():
    global test_file
    file = askopenfile(initialdir='/', title="Please select a test file")
    test_file = file.name
    print(test_file)
    messagebox.showinfo(title='Selected file', message=file.name)

def runProg(dfa,test):
    print("--------------")
    print(str(dfa))
    print("--------------")
    print(str(test))
    print("--------------")
    script = "python test.py " + str(dfa) + " " + str(test)
    print(script)
    os.system(script)
    

# UI Elements Created

selectDFAButton = Button(root, text="Select DFA File (txt)", padx=10, pady=10, command= lambda: open_dfa())
selectTestButton = Button(root, text="Select Test File (txt)", padx=10, pady=10, command= lambda: open_test())
applyButton = Button(root, text="Run Test", padx=10, pady=10, command= lambda: runProg(dfa_file, test_file))


# UI Element Placement

selectDFAButton.grid(column=0, row=0, padx=WIDTH/5)
selectTestButton.grid(column=0, row=2, padx=WIDTH/5)
applyButton.grid(column=0, row=4, padx=WIDTH/5)



if __name__== "__main__":
    mainloop()