import  socket
# creating UDP socket method
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#              ip type v4 , protocol type UDP  
target_ip="172.16.27.146"
target_port=8182
print("enter message to send :  ")
msg=input()
new_msg=msg.encode()
# lets send data
s.sendto(new_msg,(target_ip,target_port))
print("waiting for response")
my_response=s.recvfrom(50)
print(my_response)



