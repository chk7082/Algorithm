def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
        top -= 1
    else:
        stack[top] = item

def pop():
    global top
    if top == -1:
        print('underflow!')
        return
    else:
        top -= 1
        return stack[top+1]


size = 10
stack = [0]*size
top = -1

push(5, size)
push(10, size)
push(15, size)
push(20, size)
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())