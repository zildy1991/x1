import json, easygui

ListKey = ['', ' l', ' j', ' h', ' g', ' g l', ' f', ' f l', ' d', ' d l', ' d j', ' d h', ' s', ' s l', ' s j', ' s h', ' a']
ListKey2 = [15, 16, 17, 18, 19, 20, 21, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7]
ListKey3 = {'l': 1, 'j':2, 'h':3, 'g':4, 'f':6, 'd':8, 's':12, 'a':16}

class Script:
	"""Doc kich ban"""
	def __init__(self):
		self.Name = "New Song"
		self.Bpm = 80
		self.Scr = []
	def ReadJson(self, Json):
		data = json.load(Json)
		if type(data) == list: data = data[0]
		self.Name = data['name']
		self.Bpm = data['bpm']
		Type = data['type']
		if Type == 'Script':
			self.scr = data['Script']
		elif Type == 'composed':
			scr = []
			for x in data['columns']:
				scr1 = []
				for y in x[1]:
					scr1 += [ListKey2[y[0]]]
				scr += [scr1]
			self.Bpm = self.Bpm//5
			self.Scr = scr
	def ReadScript(self, Sct):
		nu = '0123456789'
		Sct = Sct.split('||')
		if Sct[0].find('Bpm') != -1:
			info = Sct[0].split('Bpm')
			self.Name = info[0]						#
			sBpm = ''
			for x in info[1]:
				if x in nu: sBpm+=x
			self.Bpm = int(sBpm)		
			Sct[1].replace('\n', ' ')
			notes = Sct[1].split(' ')
			scr = []
			col = []
			for x in notes:
				if x !='':
					try:
						a = int(x)
					except:
						scr += [col]
						col = []
						b = ListKey3[x]
						if b > 1: scr += [[]]*(b-1)
					else:
						col += [a]
			self.Scr = scr	
	def OutGenshinMusic(self):
		if self.Bpm < 80: 
			tem = 2
			Bpm = self.Bpm*2
		else: 
			tem = 1
			Bpm = self.Bpm
		St = self.Name + ' Bpm: ' + str(Bpm) + ' ||'
		dem = 0
		if self.Scr != []: 
			for x in self.Scr:
				if x == []: dem += tem
				else:
					while dem > 16: 
						dem -=16
						St += ListKey[16]
					St += ListKey[dem]
					dem = tem
					for y in x:
						St += ' ' + str(y)
		return St

	def OutGenshinNightly(self):
		outdata = [{"name":"New Song","type":"composed","bpm":220,"pitch":"C","version":3,"folderId":None,"data":{"isComposed":True,"isComposedVersion":True,"appName":"Genshin"},"breakpoints":[0],"instruments":[{"name":"Lyre","volume":90,"pitch":"","visible":True,"icon":"border","alias":""}],"columns":[],"id":None}]
		outdata[0]['name'] = self.Name
		outdata[0]['Bpm'] = self.Bpm*5
		Scr = []
		for x in self.Scr:
			list1 = []
			for y in x:
				for z in range(21):
					if ListKey2[z] == y: 
						y = z
						break
				list1 += [[y, "1"]]
			Scr += [[0, list1]]
		outdata[0]['columns'] = Scr
		St = json.dumps(outdata)
		return St

def Inputscr():
	e = True
	path = easygui.fileopenbox(default='*.json', filetypes=None)
	i = False
	try:
		with open(path, 'r') as f:
				a.ReadJson(f)
	except Exception as e:
		print(e)
	else:
		e = False 
		print('>>> import Success')
	if e: print('>>> import Feiled')
def Outputscr():
	'''
	print('-  --------- Output ----------')
	print('-  A: File .txt  (App Genshin Music Auto)')
	print('-  N: File .Json (App Genshin Music Nightly)')
	print('-  Q: Quiz')
	'''
	Q = True
	K = 'A' #input("// Choose (A/N/Q): ")
	while Q:
		if K == 'A':
			de = a.Name+".txt"
			out = a.OutGenshinMusic()
			Q = False
		elif K == 'N':
			de = a.Name+".json"
			out = a.OutGenshinNightly()
			Q = False
		elif K == Q: Q = False
		else: K = input('// Request to choose again (A/N/Q): ')
		e = True
		path = easygui.filesavebox(default=de)
		try:
			with open(path, "w") as f:
				f.write(out)
		except Exception as e:
			print('Error:')
			print(e)
		else:
			e = False 
			print('>>> Export file successfully')
		if e: print('>>> Export file Feiled')
#Main ---
print('Conversion Program v1.2.0') 
print('Created by LemonChan - TVU (Diep Giai Yen)')
print('facebook: www.facebook.com/giaiyen.china')
print('reddit: u/giaiyen123\n')
a = Script()
input('Press enter to select input file')
try:
	Inputscr()
except Exception as e:
	print('Error:')
	print(e)
else: Outputscr()
input('Thank you for using my program')

