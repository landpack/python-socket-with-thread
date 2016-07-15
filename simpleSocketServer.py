import socket

class ThreadSocket(object):
	"""
	
	"""
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))

	def listen(self):
		self.sock.listen(5)
		while True:
			client, address = self.sock.accept()
			client.settimeout(60)
			while True:
				try:
					data = client.recv(1024)
					if data:
						client.send(data)
					else:
						raise error("Client has disconnected")
				except:
					client.close()
			
if __name__ == '__main__':
	server=ThreadSocket('',9000)
	server.listen()
