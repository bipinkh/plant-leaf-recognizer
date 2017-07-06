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
		self.filename="Select an image"
		defaultimage="C:/Users/bipin/Downloads/cc.jpg"
		self.selectedFileName=StringVar()
		self.selectedFileName.set(self.filename)
		

		#dimensions
		tab_height=300
		tab_width=400

		#tabs
		tabs = ttk.Notebook(root)
		self.tab1 = ttk.Frame(tabs, width=tab_width, height=tab_height)
		tab2 = ttk.Frame(tabs, width=tab_width, height=tab_height)
		tab3 = ttk.Frame(tabs, width=tab_width, height=tab_height)
		tabs.add(self.tab1, text='Home')
		tabs.add(tab2, text='Databases')
		tabs.add(tab3, text='Help')

		#button and label for selecting image
		selectedFileNameLabel = Label(self.tab1,textvariable=self.selectedFileName)
		selectImage = Button(self.tab1, text="Select Image", command=self.selectfile)
		previewImage = Button(self.tab1, text="Preview Image", command=self.displayimage)
		#closebutton
		closeButton = Button(self.tab1, text = "Quit", command=master.quit)
		closeButton.pack()
		#image
		img1=Image.open(defaultimage)
		img1=img1.resize((120,200), Image.ANTIALIAS)
		img1 = ImageTk.PhotoImage(img1)
		self.imagePanel = ttk.Label(self.tab1,image=img1)
		self.imagePanel.image=img1

		#layout
		tabs.grid(column=0)
		selectImage.pack()
		previewImage.pack()
		selectedFileNameLabel.pack()
		closeButton.place(x=300,y=270)

		self.imagePanel.pack()


	def selectfile(self):
		self.filename = filedialog.askopenfilename()
		self.selectedFileName.set(self.filename)
		return True

	def displayimage(self):
		img2 = Image.open(self.filename)
		img2 = img2.resize((120,200), Image.ANTIALIAS)
		img2 = ImageTk.PhotoImage(img2)
		self.imagePanel.configure(image=img2)
		self.imagePanel.image=img2
		return True


		
root = Tk()
my_gui = LeafRecognition(root)
root.mainloop()
