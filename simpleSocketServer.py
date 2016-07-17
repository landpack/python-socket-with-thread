import socket
import threading
from parser import ClientRequestParser

local = threading.local()


class ThreadSocket(object):
	"""
	
	"""
	todo_list = {
		'task_01':'see someone',
		'task_02':'read book',
		'task_03':'play basketball'

	}

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
			threading.Thread(target=self.handleClientRequest, args=(client, address, local)).start()

	def handleClientRequest(self, client, address,local):
		local.todo_list = {}
		while True:
			try:
				data = client.recv(1024)
				if data:
					response=ClientRequestParser(data=data,db=local.todo_list).response()
					client.send(response)
				else:
					raise error("Client has disconnected")
			except Exception as e:
				print 'Error: ',str(e)
				client.close()
		
if __name__ == '__main__':
	server=ThreadSocket('',9000)
	server.listen()
