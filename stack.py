
stack=[10,11,12,1,2,34,2343,125]
new=[]

def push(st):
    for i in st:
        if i%2==0:
            new.append(i)
    print(new)
        
def pop_ele():
    if not new:
        print("stack is empty")
    else:
        ele=new.pop()
        print("popped",ele)
        print(new)



while True:
    print("select operations 1.push 2.pop 3.quit")
    choice=int(input())
    if choice ==1:
        push(stack)
    elif choice ==2:
        pop_ele()
    else:
        break

