import  time
import  webbrowser
print("please enter something to search on Google: ")
x=input()
mylist=x.split()
time.sleep(5)
print(mylist)
for i in mylist:

    print("user input is ",i)
    t1=type(i)
    print(t1)
    time.sleep(2)
    webbrowser.open_new_tab("https://www.google.com/search?q="+i)


