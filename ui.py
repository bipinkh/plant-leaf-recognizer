from tkinter import Tk, Label, Button, Entry
from tkinter import IntVar,StringVar
from tkinter import N, W, E, END, CENTER
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

class LeafRecognition:

	def __init__(self, master):
		self.master = master
		master.title("Plant Leaf Recognition")

		#variables and constants
		self.filename=" Select the file clicking above button."
		self.selectedFileName=StringVar()
		self.selectedFileName.set(self.filename)

		#dimensions
		tab_height=300
		tab_width=400

		#tabs
		tabs = ttk.Notebook(root)
		tab1 = ttk.Frame(tabs, width=tab_width, height=tab_height)
		tab2 = ttk.Frame(tabs, width=tab_width, height=tab_height)
		tab3 = ttk.Frame(tabs, width=tab_width, height=tab_height)

		tabs.add(tab1, text='Home')
		tabs.add(tab2, text='Databases')
		tabs.add(tab3, text='Help')
		tabs.grid(column=0)

		#button and label for selecting image
		selectedFileNameLabel = Label(tab1,textvariable=self.selectedFileName)
		selectImage = Button(tab1, text="Check Image", command=self.selectfile)
		#closebutton
		closeButton = Button(tab1, text = "Quit", command=master.quit)
		closeButton.pack()



		#layout
		selectImage.pack()
		selectedFileNameLabel.pack()
		closeButton.place(x=300,y=270)



	def selectfile(self):
		self.filename = filedialog.askopenfilename()
		self.selectedFileName.set(self.filename)
		return True
		





root = Tk()
my_gui = LeafRecognition(root)
root.mainloop()
