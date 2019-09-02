import socket
import threading
from tkinter import *

flag = 0
root = Tk()
root.title("Chat Room")
root.geometry("250x80+"+str(int(root.winfo_screenwidth()/2-125))+"+"+str(int(root.winfo_screenheight()/2-40)))
add_Ety = Entry(root)
port_Ety = Entry(root)

class Client:

	def __init__(self, ip):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(ip)
		iThread = threading.Thread(target=self.sendMsg, args=(sock, ))
		iThread.daemon = True
		iThread.start()
		while True:
			data = sock.recv(2048)
			if not data:
				break
			if data[0:1] == b'\x11':
				print("got peers!!")
			else:
				print(str(data, "utf-8"))

	def sendMsg(self, sock):
		while True:
			sock.send(bytes(input(" Enter your msg : "), "utf-8"))

def print_crap(event):
	global add_Ety, port_Ety
	add = add_Ety.get()
	port = port_Ety.get()
	if add != "" and port != "":
		root.destroy()
		ip = (add, int(port))
		Client(ip)

#GUI Part
def GUI():
	add = Label(root, text="Address :")
	port = Label(root, text="Port :")
	button = Button(root, text="Connect")
	add.grid(row=0, column=0, pady=2, padx=2, sticky=E)
	port.grid(row=1, column=0, sticky=E)
	add_Ety.grid(row=0, column=1)
	port_Ety.grid(row=1, column=1)
	button.grid(row=2, column=1, columnspan=2)
	button.bind("<Button-1>", print_crap)
	root.mainloop()

if __name__ == '__main__':
	GUI()
