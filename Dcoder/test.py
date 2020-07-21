#Question 1
x=range(1,100)
for y in x:
  if y%3==0 and y%5==0:
    print("FizzBuzz")
  elif y%5==0:
    print("Buzz")
  elif y%3==0:
    print("Fizz")
  else:
    print(y)
        
print("**********")   


#Question 2   
j="akirachix"
for z in j:
  if j.index(z)%2!=0:
    print(z.upper())
  elif j.index(z)%2==0:
    print(z.lower())
    
print("**********") 


#Question 3
leap = range(2020,2090)
for p in leap:
  if p%4==0:
    print(p)
 
print("**********")
    
    
#Question 4
w = 0
while w<100:
  w += 1
  if w%7!=0:
    print(w)
  else:
    w -= 1
    continue
    print(sum)