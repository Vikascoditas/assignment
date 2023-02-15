import collections


location=input("enter file location")
delimitter=input("enter delimitter")
delim_limit=int(input("enter delim limit"))
file=open(location,'r')
delim_count=collections.defaultdict()
delim_count['\n']=0

answer=0

for line in file:
      for element in line:
            if element not in '1234567890' and ord(element)<65 or ord(element)>90 and ord(element)<97 or ord(element)>122:
                 delim_count[element]= delim_count.get(element,0)+1
    
      line=line.split('\n')
      temp=''.join(line).split(delimitter)

   
      answer+=sum([int(j) for j in temp if j.isnumeric()] )
       
print(answer)

print(delim_count)
for key,value in delim_count.items():
      if value>delim_limit:
            print("Wrong Data or Damaged Data")
file.close()