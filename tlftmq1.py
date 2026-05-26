class TNode:
    def __init__(self, data ,left,right):
        self.data = data
        self.left = left
        self.right = right
def preorder(p):
    if p is None:
        return
    result.append(p.data)
    preorder(p.left)
    preorder(p.right)

def lastorder(p):

    if p is None:
        return
    if p.left is None and p.right is None:
        result.append(p.data)
    lastorder(p.left)
    lastorder(p.right)
    return result



def maxcost(p, current_path, current_sum):
    global best_path, max_sum
    
    if p is None:
        return

    # 1. 현재 노드를 경로에 추가하고 합계를 계산
    new_path = current_path + [p.data]
    new_sum = current_sum + p.data

    # 2. 단말 노드(Leaf)에 도달했는지 확인
    if p.left is None and p.right is None:
        # 지금까지 찾은 최대 합계보다 크면 업데이트
        if new_sum > max_sum:
            max_sum = new_sum
            best_path = new_path
        return

    # 3. 자식 노드로 재귀 호출 (합계와 경로를 들고 내려감)
    maxcost(p.left, new_path, new_sum)
    maxcost(p.right, new_path, new_sum)
    
if __name__ == '__main__':
    result = []
    best_path = []
    max_sum = -1
    a = 0
    D = TNode(40,None,None)
    E = TNode(50,None,None)
    G = TNode(70,None,None)
    F = TNode(60,None,G)
    C = TNode(30,F,None)
    B = TNode(20,D,E)
    A = TNode(10,B,C)

preorder(A)
print(f"total : {sum(result)}")
result = []
lastorder(A)
print(f"FinalCost : {sum(result)}")
result = []
maxcost(A,[],0)
print(f"MaxCost : {max_sum}")

