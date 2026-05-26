class TNode:
    def __init__(self,data,left,right):
        self.data =data
        self.left =left
        self.right=right

def preorder(n,result):
    if n is None:
        return
    result.append(n.data)
    preorder(n.left,result)
    preorder(n.right,result)
    return result

def inorder(n,result):
    if n is None:
        return
    inorder(n.left,result)
    result.append(n.data)
    inorder(n.right,result)

    
def postorder(n,result):
    if n is None:
        return
    postorder(n.left,result)
    postorder(n.right,result)
    result.append(n.data)



def printf(inp):
    if inp == 1:
        preorder(a,p)
        print(p)
    elif inp ==2:
        inorder(a,p)
        print(p)
    elif inp ==3:
        postorder(a,p)
        print(p)
    for i in p:
        print(i,end =' ')



p = []

if __name__ == '__main__':
    f = TNode(25, None, None)
    e = TNode(17,None,None)
    d = TNode(4,None,None)
    c = TNode(20,e,f)
    b = TNode(8,d,None)
    a = TNode(15,b,c)

printf(1)
'''print("루트 값 :",a.data,"루트의 자식 노드 :",a.left,a.right)

print()
print("Pre : ",end=' ')
preorder(a)
print("In",end=' ')
inorder(a)
print("Post",end =' ')
postorder(a)'''