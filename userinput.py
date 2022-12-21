import  time
import  webbrowser
print("please enter something : ")
# input is used to accept user data 
x=input()
# delay of 5 seconds 
time.sleep(5)
# lets print number
print("user input is ",x)
# checking data type 
t1=type(x)
print(t1)
# lets search on google 
webbrowser.open_new_tab("https://www.google.com/search?q="+x)




