from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

class uifunctions:
	def __init__(self, master):
		return True


	def bootupmodel(self):
		reawake=self.model.reawakemodel()
		if reawake==False:
			messagebox.showinfo("Attention","It looks like you haven't built the model.\n"+"Build it first.")
			return False
		messagebox.showinfo("Info","Model loaded. Ready to go !")
		return True

	def selectfile(self):
		self.filename = filedialog.askopenfilename()
		self.selectedFile_variable.set(self.filename)
		self.displayimage()
		return True

	def selectfolder(self):
		self.trainfolderText = filedialog.askdirectory()
		self.folderOK=1
		self.trainfolder_variable.set(self.trainfolderText)
		return True

	def displayimage(self):
		img2 = Image.open(self.filename)
		img2 = img2.resize((140,220), Image.ANTIALIAS)
		img2 = ImageTk.PhotoImage(img2)
		#self.imagePanel.configure(image=img2)
		#self.imagePanel.image=img2
		self.imagePanel2.configure(image=img2)
		self.imagePanel2.image=img2
		return True

	def quitwindow(self):
		self.source.closedatabase()
		self.master.quit()
		return True

	def scan(self):
		if self.filename=="Select an image" or not self.filename:
			messagebox.showinfo("Info","You must select an image")
			return False

		try:
			testresultarray=self.model.test(self.filename)
		except:
			messagebox.showwarning("Alert","Model not ready. Boot up the model first.")
			return False
			
		print (testresultarray) #array of probabilities
		testresult=max(testresultarray)
		accuracy=round(testresult*100,2)
		position=0
		for value in testresultarray:
			if testresult==value:
				break
			else:
				position+=1
		return position,accuracy


	def buildmodel(self):
		self.model.buildModel(self.trainfolderText)
		self.tab2Text_variable.set("Model build complete. You can now identify image.")
		getresponse=messagebox.askyesno("Info","Model Built Successful.\n"+
			"Do you want to update to your previously trained weights ?")
		if getresponse==True:
			self.model.storemodel()
		return True