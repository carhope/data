class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right=right

if __name__ == "__main__":
    E= TNode(35,None,None)
    D= TNode(40,None,None)
    C= TNode(15,E,None)
    B = TNode(20,D,None)
    A = TNode(10,B,C)

print(A.left.data)
print(A.data)