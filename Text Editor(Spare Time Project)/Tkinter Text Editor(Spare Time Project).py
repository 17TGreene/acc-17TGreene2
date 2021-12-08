import tkinter as tk
from tkinter import filedialog
def fileopen():
    textbox.delete(1.0,tk.END)
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a file to open.",filetypes = (("Text files", "*.txt*"),("All files","*.*")))
    openFile = open(filename,"r")
    for line in openFile:
        textbox.insert(tk.END,line)
    openFile.close()
        
def filesave():
    filename= filedialog.asksaveasfilename(initialdir = "/",title = "Select a file to save.",filetypes = (("Text files", "*.txt*"),("All files","*.*")),defaultextension="*.txt*")
    openFile = open(filename,"w")
    textboxInput=textbox.get(1.0,tk.END)
    openFile.write(textboxInput)
    openFile.close()
    

window = tk.Tk()
window.winfo_toplevel().title("Text Editor")
topBar = tk.Frame(master = window,bg = "gray")
openButton = tk.Button(master = topBar,text="Open",height = 2,width=7,command=fileopen)
saveButton = tk.Button(master = topBar,text="Save",height = 2,width=7,command=filesave)
wordCount = tk.Label(master = topBar,text = "WordCount:")
wordCount.pack(side=tk.RIGHT,padx = 3)
openButton.pack(side=tk.LEFT,padx=3)
saveButton.pack(side=tk.LEFT,padx=3)
textbox = tk.Text(master= window,width = 100)
topBar.pack(fill=tk.X,pady=3,padx=3)
textbox.pack(fill=tk.Y,padx=50,pady=10,expand=True)
window.mainloop()
