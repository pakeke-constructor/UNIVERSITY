
class ST(list):
    def push(self, n):
        self.append(n)

    def peek(self): return self[-1]
    def isEmpty(self): return len(self) == 0

stack = ST()


def factorial_reduce():
  if len(stack) > 1:
    stack.push(stack.pop() * stack.pop())
    factorial_reduce()

def factorial_push(n):
    if n < 1:
      stack.push(1)
      return 
    else:
      stack.push(n)
      factorial_push(n-1)

def factorial(n):
    factorial_push(n)
    factorial_reduce()
    return stack.pop()

        
def wrapper():
    num = int(input("Enter a number: "))
    return factorial(num)

if __name__ == '__main__':
    print(wrapper())


'''
from subprocess import Popen


Popen("py run_server.py 8001")

# Popen("py run_client.py")

'''