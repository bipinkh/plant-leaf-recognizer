from tkinter import Tk, Label, Button, Entry, scrolledtext
from tkinter import IntVar,StringVar
from tkinter import N, W, E, END, CENTER
from tkinter import ttk, INSERT, WORD
from PIL import ImageTk, Image
from tkinter import messagebox
import dbconnector
import main
import ui2
import webbrowser
import textwrap

 

class LeafRecognition(ui2.uifunctions):

	def __init__(self, master):
		super().__init__(master)

		self.source = dbconnector.main()
		self.model = main.build()
		self.folderOK=0

		self.master = master
		self.master.title("Plant Leaf Recognition")
		self.master.minsize(width=700, height=400)

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
		self.tab_width=700

		#tabs
		self.tabs = ttk.Notebook(root)
		self.tab1 = ttk.Frame(self.tabs, width=self.tab_width, height=self.tab_height)
		self.tab2 = ttk.Frame(self.tabs, width=self.tab_width, height=self.tab_height)
		self.tab3 = ttk.Frame(self.tabs, width=self.tab_width, height=self.tab_height)
		self.tabs.add(self.tab1, text='Home')
		self.tabs.add(self.tab2, text='CNN Model')
		self.tabs.add(self.tab3, text='Output')

		#tab-1 widgets
		self.selectedFile_label = Label(self.tab1,textvariable=self.selectedFile_variable)
		self.load_model_button = Button(self.tab1, text="Boot Up Model", command=self.bootupmodel)
		self.select_button = Button(self.tab1, text="Select Image", command=self.selectfile)
		self.scan_button = Button(self.tab1, text="Identify Image", command=self.scanbuttonTrigger)
		self.close_button = Button(self.tab1, text = "Quit", command=self.quitwindow)

		#tab-2 widgets
		self.trainfolder_button = Button(self.tab2, text="Change Train Folder Location", command=self.selectfolder)
		self.trainfolder_label = Label(self.tab2,textvariable=self.trainfolder_variable)
		self.build_button = Button(self.tab2, text="Build Model", command=self.buildmodel)
		self.tab2_label = Label(self.tab2,textvariable=self.tab2Text_variable)

		#default image
		img1=Image.open(self.defaultimage)
		img1=img1.resize((700,350), Image.ANTIALIAS)
		img1 = ImageTk.PhotoImage(img1)
		self.imagePanel = ttk.Label(self.tab1,image=img1)

		self.imagePanel2 = ttk.Label(self.tab1, image="")
		self.imagePanel.image=img1
		print ("check")
		self.layout()


	def layout(self):
		self.imagePanel.place(x=0,y=0)
		self.imagePanel2.place(x=2,y=128)
		self.tabs.grid(column=0)
		#layout-tab1
		self.selectedFile_label.place(x=5, y=350)
		self.close_button.place(x=660,y=370)
		self.load_model_button.place(x=5,y=370)
		self.select_button.place(x=105,y=370)
		self.scan_button.place(x=195,y=370)
		#layout-tab2
		self.trainfolder_label.place(x=175,y=25)
		self.trainfolder_button.place(x=0,y=25)
		self.build_button.place(x=0,y=150)
		self.tab2_label.place(x=90,y=150)
		return True

	def scanbuttonTrigger(self):
		position,accuracy=self.scan()
		information = self.source.getall(position)
		print (information)
		if (information=="Error2"):
			messagebox.showinfo("Info","Database access error")
			return False
		self.resultdisplay(accuracy,information)
		return True

	def resultdisplay(self,accuracy,information):
		self.tab3.pack_forget()
		TextHeading1 = "Accuracy:"
		TextHeading2 = "Name:"
		TextHeading3 = "Scientific Name:"
		TextHeading9 = "More On:"
		TextHeading5 = "Other Names:"
		TextHeading6 = "Dimension:"
		TextHeading7 = "Flowers & Fruits:"
		TextHeading8 = "Climate:"
		TextHeading4= "Blooming Season:"

		LabelHeading1 = Label(self.tab3, text=TextHeading1, font="Helvetica 12 bold")
		LabelHeading2 = Label(self.tab3, text=TextHeading2, font="Helvetica 12 bold")
		LabelHeading3 = Label(self.tab3, text=TextHeading3, font="Helvetica 12 bold")
		LabelHeading4 = Label(self.tab3, text=TextHeading4, font="Helvetica 12 bold")
		LabelHeading5 = Label(self.tab3, text=TextHeading5, font="Helvetica 12 bold")
		LabelHeading6 = Label(self.tab3, text=TextHeading6, font="Helvetica 12 bold")
		LabelHeading7 = Label(self.tab3, text=TextHeading7, font="Helvetica 12 bold")
		LabelHeading8 = Label(self.tab3, text=TextHeading8, font="Helvetica 12 bold")
		LabelHeading9 = Label(self.tab3, text=TextHeading9, font="Helvetica 12 bold")

		TextResult1 = str(accuracy)+"%"
		TextResult2 = information[1]
		TextResult3 = information[2]
		TextResult9 = information[3]
		TextResult5 = information[4]
		TextResult6 = information[5]
		TextResult7 = information[6]
		TextResult8 = information[7]
		TextResult4 = information[8]
		TextResult10 = information[9]

		resultVariable1= StringVar(value=TextResult1)
		resultVariable2= StringVar(value=TextResult2)
		resultVariable3= StringVar(value=TextResult3)
		resultVariable4= StringVar(value=TextResult4)
		resultVariable5= StringVar(value=TextResult5)
		resultVariable6= StringVar(value=TextResult6)
		resultVariable7= StringVar(value=TextResult7)
		resultVariable8= StringVar(value=TextResult8)
		resultVariable9= StringVar(value=TextResult9)
		resultVariable10= StringVar()
		result10 = str(information[9])
		result10 = textwrap.fill(result10, 105)
		resultVariable10.set(result10)

		LabelResult1 = Label(self.tab3,textvariable=resultVariable1, font="Helvetica 12")
		LabelResult2 = Label(self.tab3,textvariable=resultVariable2, font="Helvetica 12")
		LabelResult3 = Label(self.tab3,textvariable=resultVariable3, font="Helvetica 12")
		LabelResult4 = Label(self.tab3,textvariable=resultVariable4, font="Helvetica 12")
		LabelResult5 = Label(self.tab3,textvariable=resultVariable5, font="Helvetica 12")
		LabelResult6 = Label(self.tab3,textvariable=resultVariable6, font="Helvetica 12")
		LabelResult7 = Label(self.tab3,textvariable=resultVariable7, font="Helvetica 12")
		LabelResult8 = Label(self.tab3,textvariable=resultVariable8, font="Helvetica 12")
		LabelResult9 = Label(self.tab3,textvariable=resultVariable9, font="Helvetica 12")
		LabelResult10 = Label(self.tab3,textvariable=resultVariable10, font="Helvetica 12")

		#layout section
		self.tabs.select(self.tab3)
		self.imagePanel3 = ttk.Label(self.tab3, image=self.imagePanel2.image)
		self.imagePanel3.place(x=0,y=0)
		LabelHeading1.place(x=142,y=5)
		LabelHeading2.place(x=142,y=25)
		LabelHeading3.place(x=142,y=45)
		LabelHeading9.place(x=142,y=65)
		LabelHeading5.place(x=142,y=85)
		LabelHeading8.place(x=142,y=105)
		LabelHeading6.place(x=142,y=125)
		LabelHeading7.place(x=142,y=145)
		LabelHeading4.place(x=142,y=165)

		LabelResult1.place(x=288,y=5) #accuracy
		LabelResult2.place(x=288,y=25) #name
		LabelResult3.place(x=288,y=45) #scientific name
		LabelResult9.place(x=288,y=65) #blooming
		LabelResult5.place(x=288,y=85) #other names
		LabelResult6.place(x=288,y=105) # blooming season
		LabelResult7.place(x=288,y=125) #climate
		LabelResult8.place(x=288,y=145) #dimension
		LabelResult4.place(x=288,y=165) # flowers and fruits
		#description = scrolledtext.ScrolledText(self.tab3, wrap=WORD, width=85, height=11, font="Helvetica 12")
		#description.place(x=0,y=240)
		#description.insert(INSERT,result10)

		LabelResult10.place(x=0,y=225) #details

		return True
		

	
root = Tk()
my_gui = LeafRecognition(root)
root.mainloop()
