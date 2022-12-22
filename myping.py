import os,time
print("enter a valid IP adress : ")
target_ip=input()
print(os.system('ping  '+target_ip))

# testing os module by listing function
'''
for i in dir(os):
    if 'sys' in i:
        print(i)
        time.sleep(1)
'''