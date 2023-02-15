import collections
location=input("enter file location")
file=open(location,'r')
delim_count=collections.defaultdict()
delim_count['\n']=0
delim_limit=int(input("enter delim limit"))
answer=0
delimitter=input("enter delimitter")
for i in file:
      for element in i:
            if element not in '1234567890' and ord(element)<65 or ord(element)>90 and ord(element)<97 or ord(element)>122:
                 delim_count[element]= delim_count.get(element,0)+1
    
      i=i.split('\n')
      print(i)
      temp=''.join(i).split(delimitter)
      if temp:
            print(1)
   
      answer+=sum([int(j) for j in temp if j.isnumeric()] )
       
print(answer)

print(delim_count)
for key,value in delim_count.items():
      if value>delim_limit:
            print("Wrong Data or Damaged Data")
file.close()