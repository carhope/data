with open("/content/drive/MyDrive/Colab Notebooks/stack.py","w",encoding="utf-8")as f:
  f.write("""
class stack:
  def __init__(self, size):
    self.size=size
    self.arr=[None]*self.size
    self.top=-1
  def isEmpty(self):
    if self.top==-1:
      print("스택이 공백 상태")
      return 1;
    else :
      return 0;
  def isFull(self):
    if self.top == self.size-1:
      print("스택이 포화상태")
      return 1;
    else :
      return 0;
  def push(self,data):
    if self.isFull():
      return
    else :
      self.top+=1
      self.arr[self.top]=data
  def pop(self):
    if self.isEmpty():
      return
    else:
      data=self.arr[self.top]
      self.arr[self.top]=None
      self.top-=1
    return data
""")
  
import sys
sys.path.append('/content/drive/MyDrive/Colab Notebooks')
from stack import stack
s1 = stack(10)
s1.push('aa')
print(s1.pop())

import sys
sys.path.append('/content/drive/MyDrive/Colab Notebooks')
from stack import stack
def reverse_text(text):
  l=[]
  s1 = stack(20)
  for i in text:
    s1.push(i)
  while not s1.isEmpty():
    l.append(s1.pop())
    print(l.pop(),end="")
text='chahiumang'
reverse_text(text)