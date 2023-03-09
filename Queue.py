class Queue:
    def __init__(self):
        self.__list=[]
    def push(self,x):
        self.__list.append(x)
    def pop(self):
        self.__list.pop(0)
    def front(self):
        return self.__list[0]
    def isEmpty(self):
        if(len(self.__list)==0):
            return True
        else:
            return False
    def size(self):
        return len(self.__list)
    def pr(self):
        print(self.__list)
nav1=Queue()
n=int(input('n='))
for i in range(n):
    nav1.push(input('ism='))
nav1.pr()
i=0
m=0
ism=''
while(i<n):
    k=nav1.front()
    nav1.pop()
    if(len(k)>m):
        m=len(k)
        ism=k
    nav1.push(k)
    i+=1
print(ism, m)
new=input('new=')
i=0
while(i<n):
    k=nav1.front()
    nav1.pop()
    nav1.push(k)
    if(k==ism):
        nav1.push(new)
    i+=1
nav1.pr()