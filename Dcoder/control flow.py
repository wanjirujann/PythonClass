x = range(10)
print(x)

for y in x:
  print(y)
  
print("----------")
a = range(2, 10)
for x in a:
  print(x)
  
print("----------")    
x = range(10)
for y in x:
  if y%3==0:
    print(y)
    
    
print("----------")
x = range(10)
for y in x:
  if y%3!=0:
    print(y)
    
    
print("----------")
j = range(20)
for w in j:
  if w%5==0:
    print("{} is divisible by 5".format(w))
else:
      print("{} is not divisible by 5".format(w))
 
print("----------")
e = range(30)
for m in e:
    if m%5==0:
        print("{} is divisible by 5".format(m))
    elif m%7==0:
        print("{} is divible by 7".format(m))
    else:
        print("{} is not divisible by 5 or 7".format(m))