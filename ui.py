from tkinter import Tk, Label, Button, Entry
from tkinter import IntVar,StringVar
from tkinter import N, W, E, END, CENTER
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import dbconnector as db
import main

class LeafRecognition:

	def __init__(self, master):
		self.master = master
		master.title("Plant Leaf Recognition")
		master.minsize(width=600, height=400)

		#variables and constants
		self.filename="Select an image"
		defaultimage="C:/Users/bipin/Downloads/cc.jpg"
		self.selectedFile_variable=StringVar()
		self.selectedFile_variable.set(self.filename)
		

		#dimensions
		tab_height=400
		tab_width=550

		#tabs
		tabs = ttk.Notebook(root)
		self.tab1 = ttk.Frame(tabs, width=tab_width, height=tab_height)
		tab2 = ttk.Frame(tabs, width=tab_width, height=tab_height)
		tab3 = ttk.Frame(tabs, width=tab_width, height=tab_height)
		tabs.add(self.tab1, text='Home')
		tabs.add(tab2, text='Databases')
		tabs.add(tab3, text='Help')

		#tab-1 widgets
		selectedFile_label = Label(self.tab1,textvariable=self.selectedFile_variable)
		select_button = Button(self.tab1, text="Select Image", command=self.selectfile)
		scan_button = Button(self.tab1, text="Identify Image", command=self.scan)
		close_button = Button(self.tab1, text = "Quit", command=master.quit)
		#image
		img1=Image.open(defaultimage)
		img1=img1.resize((220,300), Image.ANTIALIAS)
		img1 = ImageTk.PhotoImage(img1)
		self.imagePanel = ttk.Label(self.tab1,image=img1)
		self.imagePanel.image=img1


		#layout
		tabs.grid(column=0)
		select_button.pack()
		scan_button.pack()
		close_button.place(x=500,y=350)
		self.imagePanel.pack()
		selectedFile_label.pack()


	def selectfile(self):
		self.filename = filedialog.askopenfilename()
		self.selectedFile_variable.set(self.filename)
		self.displayimage()
		return True

	def displayimage(self):
		img2 = Image.open(self.filename)
		img2 = img2.resize((120,200), Image.ANTIALIAS)
		img2 = ImageTk.PhotoImage(img2)
		self.imagePanel.configure(image=img2)
		self.imagePanel.image=img2
		return True

	def scan(self):
		print ("Function Working")
		print (db.host)
		return True


		
root = Tk()
my_gui = LeafRecognition(root)
root.mainloop()
