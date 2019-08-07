import socket
import threading

root = Tk()
root.title("CodeChef")
root.geometry("300x60+"+str(int(root.winfo_screenwidth()/2-150))+"+"
	+str(int(root.winfo_screenheight()/2-30)))
port_entry = Entry(root)

class Server:
	connections = []
	peers = []
	def __init__(self, port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind(("0.0.0.0", port))
		sock.listen(1)
		while True:
			c, a = sock.accept()
			cThread = threading.Thread(target=self.handlers, args=(c,a))
			cThread.daemon = True
			cThread.start()
			self.connections.append(c)
			self.peers.append(a[0])
			print(" Connected client successfully!!")
			print(" Address : " + str(a[0]))
			print(" Port : " + str(a[1]))
			self.sendPeers()
	
	def handlers(self, c, a):
		while True:
			data = c.recv(2048)
			for connection in self.connections:
				if not c == connection:
					connection.send(data)
			if not data:
				print(" Disconected client successfully!!")
				print(" Address : " + str(a[0]))
				print(" Port : " + str(a[1]))
				self.connections.remove(c)
				self.peers.remove(a[0])
				c.close()
				self.sendPeers()
				break

	def sendPeers(self):
		p = ""
		for peer in self.peers:
			p = p + peer + ", "
		for connection in self.connections:
			connection.send(b'\x11' + bytes(p, "utf-8"))

def get_crap(event):
	if port_entry.get() != "":
		root.destroy()
		Server(port_entry.get())

#GUI Part
def GUI():
	name = Label(root, text="Contest Code :")
	button = Button(root, text="Submit")
	name.grid(row=0, column=0, pady=2, padx=2, sticky=E)
	port_entry.grid(row=0, column=1)
	button.grid(row=1, column=1, columnspan=2)
	button.bind("<Button-1>", get_crap)
	root.mainloop()

if __name__ == '__main__':
	GUI()