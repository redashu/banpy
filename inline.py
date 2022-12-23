import sys
my_input=sys.argv
print(my_input)
# except first value
numbers=my_input[1:]
sum=0
for  i in numbers:
    sum=sum+int(i)

print(sum)


