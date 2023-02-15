location=input("enter file location")
file=open(location,'r')
answer=0
delimitter=input("enter delimitter")
for i in file:
    if delimitter=='\n':
      temp=i.split()
    elif delimitter=='\t':
      temp=i.split(' ')
    else:
      temp=i.split(delimitter)
   
    print(temp)
    answer+=sum([int(j) for j in temp if j.isnumeric()] )
       
print(answer)
file.close()