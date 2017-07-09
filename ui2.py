from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

class uifunctions:

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
		img2 = img2.resize((120,200), Image.ANTIALIAS)
		img2 = ImageTk.PhotoImage(img2)
		self.imagePanel.configure(image=img2)
		self.imagePanel.image=img2
		return True

	def quitwindow(self):
		self.source.closedatabase()
		self.master.quit()
		return True

	def scan(self):
		if self.filename=="Select an image":
			messagebox.showinfo("Info","You must select an image")
			return True

		reawake=self.model.reawakemodel()
		if reawake==False:
			messagebox.showinfo("Attention","It looks like you haven't built the model.\n"+
				"Build it first.")
			return False

		testresultarray=self.model.test(self.filename)
		print (testresultarray) #array of probabilities
		testresult=max(testresultarray)
		accuracy=round(testresult*100,2)
		position=0
		for value in testresultarray:
			if testresult==value:
				break
			else:
				position+=1

		desc = self.source.getdescription(position)
		name = self.source.getname(position)
		if (desc=="Error2" or name=="Error2"):
			messagebox.showinfo("Info","Database access error")
			return False

		messagebox.showinfo("Output","Accuracy Rate: "+str(accuracy)+"%\n Name: "+name+
			"\nOtherNames:\n"+desc)
		return True


	def buildmodel(self):
		self.model.buildModel(self.trainfolderText)
		self.tab2Text_variable.set("Model build complete. You can now identify image.")
		getresponse=messagebox.askyesno("Info","Model Built Successful.\n"+
			"Do you want to update to your previously trained weights ?")
		if getresponse==True:
			self.model.storemodel()
		return True