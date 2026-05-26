class TNode:
    def __init__(self,data,left,right):
        self.data =data
        self.left =left
        self.right=right

def preorder(p):
    if p is None:
        return
    result.append(p.data)
    preorder(p.left)
    preorder(p.right)


def inorder(p):
    if p is None:
        return
    inorder(p.left)
    result.append(p.data)
    inorder(p.right)
    
def postorder(p):
    if p is None:
        return
    postorder(p.left)
    postorder(p.right)
    result.append(p.data)
    
def solonode(p):
    if p is None:
        return
    solonode(p.left)
    if p.left is None and p.right is None:
        result.append(p.data)
    solonode(p.right)




def printf(inp):
    global result
    global sum
    result =[]
    if inp == 1:
        print("Pre : ",end=' ')
        size = int(input("얼마나 보다 커야하는가?"))
        preorder(a)
        for i in result:
            if i >size:
                print(i,end=' ')



    elif inp == 2:
        print("In : ",end=' ')
        solonode(a)
        for i in result:
            sum += i
        
        print(sum)


        result =[]
    elif inp == 3:
        print("Post : ",end =' ')
        postorder(a)
        print(result)
        print(len(result))

    else:
        print("잘못된 입력입니다.")
        printf(int(input("1. Preorder 2. Inorder 3. Postorder : ")))

sum = 0
result = []

if __name__ == '__main__':
    f = TNode(25, None, None)
    e = TNode(17,None,None)
    d = TNode(4,None,None)
    c = TNode(20,e,f)
    b = TNode(8,d,None)
    a = TNode(15,b,c)

    print("루트 값 :",a.data,"루트의 자식 노드 :",a.left.data,a.right.data)
    print()
    printf(int(input("1. Preorder 2. Inorder 3. Postorder : ")))
    printf(int(input("1. Preorder 2. Inorder 3. Postorder : ")))
    printf(int(input("1. Preorder 2. Inorder 3. Postorder : ")))
    '''print("루트 값 :",a.data,"루트의 자식 노드 :",a.left,a.right)
    
    print()
    print("Pre : ",end=' ')
    preorder(a)
    print("In",end=' ')
    inorder(a)
    print("Post",end =' ')
    postorder(a)'''