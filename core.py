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
		
def consensus(blocks):
	blocks=json.loads(blocks)
	for block in blocks:
		found=0
		for token in blockchain:
			if(block.hash==token.hash):
				found=1
			else:
				#not node
				pass
		#hash of block not found
		if(found==0):
			return "fail"
		else:
			#block found
			pass
	#block has error
	return "pass"

def Proc():
	#used to process votes
	n=len(network)
	votes=0
	i=0
	while(i<n):
		plug=socket(AF_INET,SOCK_DGRAM)
		blocks=json.dumps(blockchain)
		plug.sendto(blocks,network[i])
		response,addr=plug.recvfrom(4096)
		if(response=="pass"):
			votes=votes+1
		else:
			#failing consensus
			break
		i=i+1
	#number of votes archived
	if(votes==n):
		return 1
	else:
		return 0
		
def Stamp(data):
	data=json.loads(data)
	size=len(data)
	body=[]
	i=1
	while(i<size):
		body.append(data[i])
		i+=1
	n=len(blockchain)
	hashn=blockchain[n-1].hash
	block=Block(hashn,data[0],body)
	
	consensus=Proc()
	if(consensus==1):
		blockchain.append(block)
		for node in network:
			plug=socket(AF_INET,SOCK_DGRAM)
			block=json.dumps(block)
			plug.sendto(block.encode(),(node,6060))
	else:
		#failed consensus
		pass
	return consensus

def Request(req):
	#processing request
	#retreaval method
	if((len(req)+1)>len(blockchain[0].log)):
		#retrival request.
		response=Retrival(req)
		response=json.dumps(response)
		return response
	elif(len(req)==len(json.dumps(blockchain))):
		#consensus vote
		response=Consensus(req)
		return response
		
	elif(len(req)>len(json.dumps(blockchain[0]))):
		#update block
		data=json.loads(data)
		size=len(data)
		body=[]
		i=1
		while(i<size):
			body.append(data[i])
			i+=1
		n=len(blockchain)
		hashn=blockchain[n-1].hash
		block=Block(hashn,data[0],body)
		blockchain.append(block)
	else:
		#stamp
		response=Stamp(req)
		return response
	


#initialilsing network by requesting network block
def init():
	print("INITIALISING....")
	net=socket(AF_INET,SOCK_DGRAM)
	req="network-block"
	net.sendto(req.encode(),('',6060))
	netwk,addr=net.recvfrom(4096)
	network.create(netwk)
	if(len(network.nodes)!=0):
		print("NETWORK LOADED")
	else:
		print("FAILED TO LOAD NETWORK")
		#loop again
		init()
	#loading block
	#place holder code------------------------------------------>
	req="blockchain-block"
	net.sendto(req.encode(),('',6060))
	blocks,addr=net.recvfrom(4096)
	blocks=json.loads(blocks)
	net.close()
	return blocks

#initialisation	
network=Network()
blocks=init()
blockchain=[]
for x in blocks:
	#extract body first
	size=len(x)
	i=2
	body=[]
	while(i<size):
		body.append(x[i])
		i+=1
	#create block object
	block=Block(x[0],x[1],body)
	#add blocks into blockchain list
	blockchain.append(block)
#initialisation complete	

ip=''
#creating the server
server=socket(AF_INET,SOCK_DGRAM)
server.bind((ip,6060))
#open server
while True:
	request,address=server.recvfrom(4096)
	#post request for processing
	response=Request(request)
	server.sendto(response.encode(),address)
















