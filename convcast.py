#for type conversion(automatic)
a=25
b=35.45
print(a+b)#here a is int type and b is float type and we got the output in float which is automatic type conversion

#type casting
a="2"
b=5
print("type of a is :",type(a))#str
c=int(a)#here we change datatype of a(string) to int and store it to c variable
print(type(c))#int
print(b+c)