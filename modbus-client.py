from argparse import ArgumentParser
from socket import create_connection
from umodbus.client import tcp
from cryptography.fernet import Fernet
import rsa

#Parse the argument of address.
parser = ArgumentParser()	
parser.add_argument("-a", "--address")
args = parser.parse_args()
host, port = args.address.rsplit(":", 1)
port = int(port)

values = [1, 2, 3, 4]

sock = create_connection((host, port)) #creating connection with modbus proxy 

# receiving the public key of proxy

proxy_public_key = rsa.PublicKey.load_pkcs1(sock.recv(1024))
EncryptionKey = Fernet.generate_key()

#sending the encrypted Encryption key to modbus proxy
print("Public key of modbus proxy is : " + str(proxy_public_key))
print("Client Encryption key generated is : " + str(EncryptionKey))
print("Clients encryption key encrypted with PublicKey of modbus proxy is :" + str(rsa.encrypt(EncryptionKey, proxy_public_key)))
sock.sendall(rsa.encrypt(EncryptionKey, proxy_public_key))
fernet = Fernet(EncryptionKey)

#creating a modbus ADU to write multiple coils with starting address 1 and values 1, 0, 1, 0,0,1,0.
message = tcp.write_multiple_coils(slave_id=1, starting_address=1, values=[1, 0, 1, 0,0,1,0])


# response recieved depends on command requested as it will return the number of coils written
response = tcp.send_message(fernet.encrypt(message), sock)
#this is one request , now client can request any commands just like above


#closing the socket connection
sock.close()