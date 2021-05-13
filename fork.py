import json
from socket import socket,AF_INET,SOCK_DGRAM

#network block
class Network:
	def __init__(self,nodes=""):
		self.nodes=nodes
		#shuffle nodes
		#code
	def create(self,nodes):
		self.nodes=json.loads(nodes)
#block object

class Block:
	def __init__(self,hashn,log,body):
		#supposed to calculate hash through n-hash algorithm
		self.hash=hashn+1
		self.log=log
		self.body=body

def Request(req,addr):
	#processing request
	if(req=="network-block"):
		network.append(addr)
		return json.dumps(network)
	elif(req=="blockchain-block"):
		return json.dumps(blockchain)
	else:
		block=json.loads(req)
		blockchain.append(block)
		return "pass"

ip=''
port=6060
network[]
blockchain[]
fork=socket(AF_INET,SOCK_DGRAM)
fork.bind((ip,port))
while True:
	request,address=fork.recvfrom(4096)
	response=Request(request,addresss)
	fork.sendto(response.encode(),address)
