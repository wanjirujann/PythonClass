x=1
while x<10:
    print(x)
    x+=1
    
x=100
while x>=30:
     print(x)
     x-=10
    
x=100
while x>=30:
    print(x)
    if x<50:
        break
    x-=10
  
x=1
while x<50:
    print(x)   
    if x%17==0:
        break
    x+=1
    
x=0
while x<10:
  x+=1
  if x%2==0:
    continue
  print(x)    
  
x=1
while x<50:
  x+=1
  if x%2!=0:
    continue
  print(x)  
  
x=0
while x<=50:
  x+=1
  if x%2!=0:
    continue
  print(x)
  