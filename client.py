import socket
import threading
from tkinter import *

flag = 0
root = Tk()
root.title("Chat Room")
root.geometry("250x80+"+str(int(root.winfo_screenwidth()/2-125))+"+"+str(int(root.winfo_screenheight()/2-40)))
add_entry = Entry(root)
port_entry = Entry(root)

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
			sock.send(bytes(input(""), "utf-8"))

def print_crap(event):
	global add_entry, port_entry
	if add_entry.get() != "" and port_entry.get() != "":
		root.destroy()
		Client((add_entry.get(), port_entry.get()))

#GUI Part
def GUI():
	add = Label(root, text="Address :")
	port = Label(root, text="Port :")
	button = Button(root, text="Connect")
	add.grid(row=0, column=0, pady=2, padx=2, sticky=E)
	port.grid(row=1, column=0, sticky=E)
	add_entry.grid(row=0, column=1)
	port_entry.grid(row=1, column=1)
	button.grid(row=2, column=1, columnspan=2)
	button.bind("<Button-1>", print_crap)
	root.mainloop()

if __name__ == '__main__':
	GUI()
