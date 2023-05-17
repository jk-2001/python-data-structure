queue=[10,11,12,1,2,34,2343,125]
new=[]

def enqueue(st):
    for i in st:
        if i%2==0:
            new.append(i)
    print(new)
        
def dequeue():
    if not new:
        print("queue is empty")
    else:
        ele=new.pop(0)
        print("deleted",ele)
        print(new)



while True:
    print("select operations 1.enqueue 2.dequeue 3.quit")
    choice=int(input())
    if choice ==1:
        enqueue(queue)
    elif choice ==2:
        dequeue()
    else:
        break