try:
	# python 3.x
	import sys
	import math
	import tkinter as tk
	from tkinter import messagebox
except ImportError:
	# python 2.x
	import Tkinter as tk
#from PIL import Image, ImageTk


class Pedrosadora(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.result = ()
		self.num1 = tk.StringVar()
		self.txtDisplay=tk.Entry(self, textvariable = self.num1, bd = 10, insertwidth = 1, font = 30)
		self.txtDisplay.bind('<KeyPress>', self.keyPress)
		self.txtDisplay.pack(fill=tk.Y)

		frame1 = tk.Frame(self)
		frame1.pack(fill=tk.Y)

		button1 = tk.Button(frame1, padx = 16, pady = 16, bd = 8, text="1", fg="black",command = lambda:self.set_text('1'))
		button1.pack(side = tk.LEFT)

		button2 = tk.Button(frame1, padx = 16, pady = 16, bd = 8, text="2", fg="black",command = lambda:self.set_text('2'))
		button2.pack(side = tk.LEFT)

		button3 = tk.Button(frame1, padx = 16, pady = 16, bd = 8, text="3", fg="black",command = lambda:self.set_text('3'))
		button3.pack(side = tk.LEFT)

		button4 = tk.Button(frame1, padx = 13.52, pady = 16, bd = 8, text="+", fg="black",command = lambda:self.set_text('+'))
		button4.pack(side = tk.LEFT)

		button5 = tk.Button(frame1, padx = 15, pady = 16, bd = 8, text="-", fg="black",command = lambda:self.set_text('-'))
		button5.pack(side = tk.LEFT)

		button6 = tk.Button(frame1, padx = 16, pady = 16, bd = 8 , text="*", fg="black",command = lambda:self.set_text('*'))
		button6.pack(side = tk.LEFT)

		frame2 = tk.Frame(self)
		frame2.pack(fill=tk.Y)

		button1 = tk.Button(frame2, padx = 16, pady = 16, bd = 8, text="4", fg="black",command = lambda:self.set_text('4'))
		button1.pack(side = tk.LEFT)

		button2 = tk.Button(frame2, padx = 16, pady = 16, bd = 8, text="5", fg="black",command = lambda:self.set_text('5'))
		button2.pack(side = tk.LEFT)

		button3 = tk.Button(frame2, padx = 16, pady = 16, bd = 8, text="6", fg="black",command = lambda:self.set_text('6'))
		button3.pack(side = tk.LEFT)

		button4 = tk.Button(frame2, padx = 13.52, pady = 16, bd = 8, text="n", fg="black",command = lambda:self.set_text('**'))
		button4.pack(side = tk.LEFT)

		button5 = tk.Button(frame2, padx = 15, pady = 16, bd = 8, text="r", fg="black",command = lambda:self.set_text('**0.5'))
		button5.pack(side = tk.LEFT)

		button6 = tk.Button(frame2, padx = 16, pady = 16, bd = 8 , text="*", fg="black",command = lambda:self.set_text('*'))
		button6.pack(side = tk.LEFT)

		frame3 = tk.Frame(self)
		frame3.pack(fill=tk.Y)

		button1 = tk.Button(frame3, padx = 16, pady = 16, bd = 8, text="7", fg="black",command = lambda:self.set_text('7'))
		button1.pack(side = tk.LEFT)
		
		button2 = tk.Button(frame3, padx = 16, pady = 16, bd = 8, text="8", fg="black",command = lambda:self.set_text('8'))
		button2.pack(side = tk.LEFT)

		button3 = tk.Button(frame3, padx = 16, pady = 16, bd = 8, text="9", fg="black",command = lambda:self.set_text('9'))
		button3.pack(side = tk.LEFT)

		button4 = tk.Button(frame3, padx = 11, pady = 16, bd = 8, text="CE", fg="black",command = self.Clear_all)
		button4.pack(side = tk.LEFT)

		button5 = tk.Button(frame3, padx = 13, pady = 16, bd = 8, text="C", fg="black",command = self.Clear)
		button5.pack(side = tk.LEFT)

		button6 = tk.Button(frame3, padx = 16, pady = 16, bd = 8 , text="*", fg="black",command = lambda:self.set_text('*'))
		button6.pack(side = tk.LEFT)

		frame4 = tk.Frame(self)
		frame4.pack(fill=tk.Y)

		button1 = tk.Button(frame4, padx = 72, pady = 16, bd = 8, text="0", fg="black",command = lambda:self.set_text('0'))
		button1.pack(side = tk.LEFT)
		
		button2 = tk.Button(frame4, padx = 72, pady = 16, bd = 8, text="=", fg="black",command = self.calc_total)
		button2.pack(side = tk.LEFT)
		
	def set_text(self,text):
		self.txtDisplay.insert(tk.END,text)

	def Clear_all(self):
		self.txtDisplay.delete(0,tk.END)

	def Clear(self):
		self.txtDisplay.delete(len(self.txtDisplay.get())-1, tk.END)

	def calc_total(self):
		try:
			self.result = eval(self.txtDisplay.get())
		except:
			messagebox.showerror(message = 'Que has escrito?')
		self.Clear_all()
		self.set_text(self.result)
	def keyPress(self,event):
		if event.char in ('1','2','3','4','5','6','7','8','9','0','*','/','-','+','.'):
			print (event.char)
		elif event.keysym not in ('BackSpace','Alt_r', 'Alt_L', 'F4'):
			print (event.keysym)
			return 'break'
if __name__ == "__main__":
	root = tk.Tk()
#	bg_image = ImageTk.PhotoImage(file ="fondo_metal.jpg")
#	w = bg_image.width()
#	h = bg_image.height()
	root.title("Pedrossadora")
	Pedrosadora(root).pack(fill="both", expand=True)
	root.mainloop()