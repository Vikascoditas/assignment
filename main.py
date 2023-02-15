file=open('C:\\Users\\Coditas\\Desktop\\question.txt')
answer=0
for i in file:
    answer+=sum(list(map(int,i.split(','))))
print(answer)