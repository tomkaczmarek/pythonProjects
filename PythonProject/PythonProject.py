print("Hello World")
x=1
st = "test"
print(x)
print(st)


#Comments

zero = None
print(zero)
one = 1
two = 2
three = one + two
print(three)

s1 = "Hello"
s2 = "World"
s1 = s1 + s2
print(s1)

#Conditions

if s2 == "World":
    print("Hej")
if isinstance(s1, str) or s1 == "Hello":
    print("I am here")
if(zero == None):
    print("Jest None")

#Lists and loops
mylist = []
mylist.append(1)
mylist.append("test")
mylist.append(7.0)

print(mylist[0])

for x in mylist:
    print(x)

mylist1 = [1,2,"hej"]
print(mylist1[2])

print("Hello, what its your name?")
name = input("???")
age = 1000

print("Hello %s test, Age: %d blbla %s" % (name, age, name))


def my_method() :
    print("my first method in python")

def my_secondMethod(arg1, arg2, arg3):
    s = arg1 + arg2 + arg3
    print(s)

my_method()
my_secondMethod("323","2332","233")


from sys import argv
import math
import Math

print(math.pi)

def add(arg1, arg2):
    return arg1 + arg2

print(add(4,6))

Math.Math.myfunction()


