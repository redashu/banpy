import  socket
# creating UDP socket method
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#              ip type v4 , protocol type UDP  
target_ip="172.16.27.146"
target_port=8182
# only REc will be doing this
s.bind((target_ip,target_port))
# lets rec message 
while 3 > 2 :
    data=s.recvfrom(100)
    print(data)
    # sep data
    actual_data=data[0]
    sender_addr=data[1]
    print("sending response ..........!!")
    common_msg="got it"
    new_common_msg=common_msg.encode()
    s.sendto(new_common_msg,sender_addr)




