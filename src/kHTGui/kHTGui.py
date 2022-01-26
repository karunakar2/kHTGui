import tkinter as tk

class kHTGui:
	#class global variables
	siteOptions = ['']
	measurementAndSite = {'selectMeasurement': 'Flow',
				'selectSite' : 'Mohaka River at Raupunga'}

	def __init__(self,kHTop=None):
		if kHTop == None:
			import kHilltopConnector as kHK
			self.kHTop = kHK.kHilltopConnector(apiUrl='https://data.hbrc.govt.nz/Envirodata/EMAR.hts',refreshInterval=24*3600)
		else:
			self.kHTop = kHTop
        
        
        
		self.measOptions = self.kHTop.measurementsList.copy()
		self.measOptions.sort()

		self.start_gui()
	
	def weAreDone(self):
		self.measurementAndSite = {'selectMeasurement': self.measVariable.get(),
				'selectSite' : self.siteVariable.get()}
		self.window.destroy()
	
	def start_gui(self):
		self.window = tk.Tk()
		self.window.title('kHilltopConnector GUI')

		self.measFrame = tk.Frame(self.window)
		self.measVariable = tk.StringVar(self.measFrame)
		if 'Flow' in self.measOptions:
			self.measVariable.set(self.measurementAndSite['selectMeasurement'])
		else:
			self.measVariable.set(measOptions[0])
		self.measMenu = tk.OptionMenu(self.measFrame, self.measVariable, *self.measOptions)
		self.measMenu.pack(side=tk.LEFT)
		self.changeMeas = tk.Button(self.measFrame, text="update", command=self.getSites)
		self.changeMeas.pack(side=tk.RIGHT)
		self.measFrame.pack()
		
		self.siteFrame = tk.Frame(self.window)
		self.siteVariable = tk.StringVar(self.siteFrame)
		self.siteVariable.set(self.measurementAndSite['selectSite'])
		self.siteMenu = tk.OptionMenu(self.siteFrame, self.siteVariable, *self.siteOptions)
		self.siteMenu.pack(side=tk.LEFT)
		self.getData = tk.Button(self.siteFrame, text="Done", command=self.weAreDone)
		self.getData.pack(side=tk.RIGHT)
		self.siteFrame.pack()
		
		self.window.mainloop()
		
	def getSites(self):
		self.kHTop.selectMeasurement = self.measVariable.get()
		self.siteOptions = self.kHTop.siteList.copy()
		self.siteOptions.sort()
		self.siteVariable.set(self.siteOptions[0])
		self.siteMenu['menu'].delete(0,'end')
		for choice in self.siteOptions:
				self.siteMenu['menu'].add_command(label=choice, command=lambda x=choice: self.weAreDone())

