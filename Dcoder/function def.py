def hello():
  print("Hello Akirachix")
 
hello()


def hello(name):
  print("Hello {}".format(name))
 
hello("Akirachix")


def year_of_birth(name,age):
    year=2020-age
    print("Hello {} you were born in year {} ".format(name,year))
year_of_birth("Eunice",20)

def add(a,b):
    answer=a+b
    return answer 
    
j=add(12,4)
k=add(60,20)
l=add(500,300)
print(j)
print(k)
print(l)

#subtract 
def subtract(l,k):
    answer=l-k
    return answer
    
m=subtract(77,11)
n=subtract(8888,4444)
o=subtract(5,2)
print(m)
print(n)
print(o)

#divide
def divide(m,o):
    answer=m/o
    return answer
    
p=divide(1000,50)
q=divide(52,9)
r=divide(110,10)
print(p)
print(q)
print(r)

#multiply 
def multiply(x,y):
    answer=x*y
    return answer
    
s=multiply(23,78)
t=multiply(44,60)
u=multiply(77,29)
print(s)
print(t)
print(u)

#remainder
def remainder(j,k):
    answer=j%k
    return answer
    
a=remainder(99,6)
b=remainder(77,5)
c=remainder(800,277)
print(a)
print(b)
print(c)
    