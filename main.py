location=input("enter file location")
file=open(location,'r')
answer=0
delimitter=input("enter delimitter")
for i in file:
    
      i=i.split('\n')
      temp=''.join(i).split(delimitter)
   
      answer+=sum([int(j) for j in temp if j.isnumeric()] )
       
print(answer)
file.close()