# Using a modbus proxy between client and server to implement the encryption security through RSA cryptography algorithm.


## Description:
Modbus client is connected to modbus device through a proxy server as we cannot directly implement security algorithms on modbus device as they were build when cyber security was not a big concern so we need to take help of proxy server to exchange cryptic encryption keys with client so that same encryption key can be used for sending and receiving messages between client and server.


## Pre-Requisites:
You should have a Windows 7 or Windows 10 because ModRSSim simulator is compatible with them only.
you should have Python >=3.5 installed on the client system.


## Installation:
1. for installing umodbus library in your (Client) system , Open Terminal or command prompt and run the command "pip install umodbus".
2. for installing modbus-proxy library in your system , Open Terminal or command prompt and run the command "pip install modbus-proxy".
3. Install the modrssim simulator on windows machine (Server) SRC:"https://sourceforge.net/projects/modrssim/files/" and install the msi file.
4. Download the umodbus library files form Github here: https://github.com/AdvancedClimateSystems/uModbus/


##Note:
If you are runnning both client and server on same machine then install all above things in same system.


## Usage:
Step 1. In windows machine, Run the ModRSSim simulator.


## --For running the modbus proxy--


Step 2. Copy the modbus-proxy.py file while i have provided in folder
Step 3. Go to the directory where modbus-proxy library is installed in python/anaconda for example in my case the directory was at location “~/Applications/anaconda3/lib/python3.8/site-packages” and replace it with modbus-proxy.py python file.
Step 4. Create a yml configuration file with text inside it as below --
devices:
- modbus:
   url: host:502     # Put the IP address of system where modbus simulator is running or 127.0.0.1 if you are using the same system for client and server.
   timeout: 10                # communication timeout (s) (optional, default: 10)
   connection_time: 0.1       # delay after connection (s) (optional, default: 0)
 listen:
   bind: 0:9000         #this is the host:port on which proxy server will be listening the clients

Step 4. To run the modbus proxy ,open the Terminal/Command prompt and type the command “modbus-proxy -c [path to yml file created above]”.


## --To run the client --


Step 5. Browse to the folder where you have downloaded the umodbus files from github in step fourth of installation and then go to the directory “~/uModbus/scripts/examples/” and copy paste the file “modbus-client.py” given by me in folder.

Step 6: copy and replace the tcp.py provided in zip folder into the umodbus library installed in python/anaconda i.e ~/python3.8/site-packages/umodbus/client/tcp.py in my system.

Step 7 . to run the client , open the Terminal and write the following command “python ~/uModbus/scripts/examples/modbus-client.py -a 0:9000”