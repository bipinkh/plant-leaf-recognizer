from tkinter import Tk, Label, Button, Entry
from tkinter import IntVar,StringVar
from tkinter import N, W, E, END, CENTER
from tkinter import ttk
from PIL import ImageTk, Image
import dbconnector
import main
import ui2
 

class LeafRecognition(ui2.uifunctions):

	def __init__(self, master):

		self.source = dbconnector.main()
		self.model = main.build()
		self.folderOK=0

		self.master = master
		self.master.title("Plant Leaf Recognition")
		self.master.minsize(width=600, height=400)

		#variables and constants
		self.defaultimage="banner.jpg"
		self.filename="Select an image"
		self.selectedFile_variable=StringVar()
		self.selectedFile_variable.set(self.filename)
		self.tab2Text = "Build the model. It may take a while. Be patient."
		self.tab2Text_variable=StringVar()
		self.tab2Text_variable.set(self.tab2Text)
		self.trainfolderText = "F:/minorproject/data/train"
		self.trainfolder_variable=StringVar()
		self.trainfolder_variable.set(self.trainfolderText)

		#dimensions
		self.tab_height=400
		self.tab_width=600

		#tabs
		self.tabs = ttk.Notebook(root)
		self.tabs.configure(background="#fff")
		self.tab1 = ttk.Frame(self.tabs, width=self.tab_width, height=self.tab_height)
		self.tab2 = ttk.Frame(self.tabs, width=self.tab_width, height=self.tab_height)
		self.tab3 = ttk.Frame(self.tabs, width=self.tab_width, height=self.tab_height)
		self.tabs.add(self.tab1, text='Home')
		self.tabs.add(self.tab2, text='CNN Model')
		self.tabs.add(self.tab3, text='Help')

		#tab-1 widgets
		self.selectedFile_label = Label(self.tab1,textvariable=self.selectedFile_variable)
		self.load_model_button = Button(self.tab1, text="Boot Up Model", command=self.bootupmodel)
		self.select_button = Button(self.tab1, text="Select Image", command=self.selectfile)
		self.scan_button = Button(self.tab1, text="Identify Image", command=self.scan)
		self.close_button = Button(self.tab1, text = "Quit", command=self.quitwindow)

		#tab-2 widgets
		self.trainfolder_button = Button(self.tab2, text="Change Train Folder Location", command=self.selectfolder)
		self.trainfolder_label = Label(self.tab2,textvariable=self.trainfolder_variable)
		self.build_button = Button(self.tab2, text="Build Model", command=self.buildmodel)
		self.tab2_label = Label(self.tab2,textvariable=self.tab2Text_variable)

		#default image
		img1=Image.open(self.defaultimage)
		img1=img1.resize((600,350), Image.ANTIALIAS)
		img1 = ImageTk.PhotoImage(img1)
		self.imagePanel = ttk.Label(self.tab1,image=img1)
		self.imagePanel.image=img1
		print ("check")
		self.layout()


	def layout(self):
		self.imagePanel.place(x=0,y=0)
		self.tabs.grid(column=0)
		#layout-tab1
		self.selectedFile_label.place(x=5, y=350)
		self.close_button.place(x=560,y=370)
		self.load_model_button.place(x=5,y=370)
		self.select_button.place(x=105,y=370)
		self.scan_button.place(x=195,y=370)
		#layout-tab2
		self.trainfolder_label.pack()
		self.trainfolder_button.pack()
		self.build_button.place(x=230,y=170)
		self.tab2_label.place(x=100,y=150)

		return True
	
root = Tk()
my_gui = LeafRecognition(root)
root.mainloop()
