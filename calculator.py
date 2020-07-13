import tkinter as tk
from tkinter import ttk

class mainScreen():
	def __init__(self, master):
		#Screen setting
		self.master = master
		self.master.title("Calculator")
		self.master.geometry("350x350")
		self.frame = ttk.Frame(self.master)

		#creat entry 
		self.equation = tk.StringVar()
		self.express = ""
		self.entry = ttk.Entry(self.master,font="San_Francisco 45 ", textvariable = self.equation, width = 12, justify= 'right')
		self.entry.grid(row = 0, column = 0, columnspan = 4)
		
		#create Number_button
		self.buttonList = []
		self.buttonList.append([])
		rows = 0
		for j in range(1, 10):
			new_button = ttk.Button(self.master, text= str(j))
			self.buttonList[rows].append(new_button)

			if (j % 3 == 0):
				self.buttonList.append([])
				rows += 1
				
		#create operator_button
		self.buttonList.append([])
		for opt in ['c','÷', 'x', '-', '+', '=', '0', '.']:
			new_opt_button = ttk.Button(self.master, text= opt)
			self.buttonList[4].append(new_opt_button)

		#show buttons
		for rows in range(0, 3) :
			for colm in range(0, 3) :
				self.buttonList[rows][colm].grid(row = rows+1, column= colm, ipadx = 3, ipady = 15, )

		#show '=', '0', '.' button 
		self.buttonList[4][5].grid(row = 5 ,column = 0, ipadx = 3, ipady = 15,columnspan = 3 )
		self.buttonList[4][5].configure(width = 28)
		self.buttonList[4][6].grid(row = 4 ,column = 0, ipadx = 3, ipady = 15,columnspan = 2 )
		self.buttonList[4][6].configure(width = 17)
		self.buttonList[4][7].grid(row = 4, column = 1, ipadx = 3, ipady = 15,columnspan = 2)
		self.buttonList[4][7].configure(width = 6)

		#show operator button
		for rows in range(0, 5) :
			self.buttonList[4][rows].grid(row = rows+1, column= 3, ipadx = 3, ipady = 15)

		self.addEvent()

	def press (self, txt) :
		if (self.isSpecial(txt)) :
			pass
		else:
			self.express += txt
			self.equation.set(self.express)

	def isSpecial (self,txt) :
		operator = ['+', '-', 'x', '÷', '.']
		if (txt == '-' and self.express == '') :
			return False
		elif (txt in operator and self.express[-1] in operator):
			return True
		else:
			return False

	def clear (self) :
		self.express = ''
		self.equation.set(self.express)

	def calculate (self) : ## เช็ค ข้อความ และ แปลง 'x' to '*' & divided sign to '/'
		
		#catch the ZeroDivisionError
		try:
			#replace x, ÷ to *, / 
			if ('x' in self.express) :
				self.express = self.express.replace('x', '*')
			elif ('÷' in self.express) :
				self.express = self.express.replace('÷', '/')

			#convert string into equation and calculate
			total = str(eval(self.express)) 
			self.express = total
			self.equation.set(total)

		except ZeroDivisionError:
			self.express = ''
			self.equation.set('Error !')
			
	def addEvent (self) :
		self.buttonList[0][0].configure(command = lambda: self.press('1'))
		self.buttonList[0][1].configure(command = lambda: self.press('2'))
		self.buttonList[0][2].configure(command = lambda: self.press('3'))
		self.buttonList[1][0].configure(command = lambda: self.press('4'))
		self.buttonList[1][1].configure(command = lambda: self.press('5'))
		self.buttonList[1][2].configure(command = lambda: self.press('6'))
		self.buttonList[2][0].configure(command = lambda: self.press('7'))
		self.buttonList[2][1].configure(command = lambda: self.press('8'))
		self.buttonList[2][2].configure(command = lambda: self.press('9'))
		self.buttonList[4][0].configure(command = self.clear)
		self.buttonList[4][1].configure(command = lambda: self.press('÷'))
		self.buttonList[4][2].configure(command = lambda: self.press('x'))
		self.buttonList[4][3].configure(command = lambda: self.press('-'))
		self.buttonList[4][4].configure(command = lambda: self.press('+'))
		self.buttonList[4][5].configure(command = self.calculate)
		self.buttonList[4][6].configure(command = lambda: self.press('0'))
		self.buttonList[4][7].configure(command = lambda: self.press('.'))


def main(): 
    root = tk.Tk(className="Calculator")
    app = mainScreen(root)
    root.mainloop()

if __name__ == '__main__':
    main()
	
