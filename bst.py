#[50, 30, 70, 20, 40, 60, 80, 35, 45, 75]
class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# [도우미 함수] 오른쪽 서브트리에서 가장 작은 노드(후계자)를 찾는 함수
def get_min_node(node):
    current = node
    # 왼쪽 자식이 존재하는 동안 계속해서 왼쪽으로 파고듭니다.
    while node is not None:
        current = current.left # "더 작은 값 찾으러 왼쪽으로 이동!"
    # 더 이상 왼쪽 자식이 없으면 그 노드가 최솟값입니다.
    return current

# 1. 데이터 탐색 - 재귀함수 사용하기
def search_rec(node, key):
    # 1. 종료 조건: 바닥에 닿았거나(None), 찾고자 하는 값을 발견했을 때
    if node == None:
        return node
    if key == node.data:
        return node
    
    # 2. 찾는 값이 현재 노드의 값보다 작을 때
    # -> 왼쪽 서브트리에게 "네가 마저 찾아줘!" 하고 재귀 호출
    if key < node.data:
        return search_rec(node.left, key)
    # 3. 찾는 값이 현재 노드의 값보다 클 때
    # -> 오른쪽 서브트리에게 재귀 호출
    else:
        return search_rec(node.right, key)

# 2. 데이터 삽입
def insert_node(node, key):
    # [Step 1] 빈자리 발견 (종료 조건) -> 새 노드(TNode) 객체를 생성하여 반환
    if node is None:
        return TNode(key)
    
    # [Step 2] 자리를 찾아 아래로 내려가며 부모-자식 연결 갱신
    # 넣으려는 값이 더 작으면? -> 왼쪽 서브트리로 재귀 호출 후 내 왼쪽 참조에 연결
    if key < node.data:
        node.left = insert_node(node.left, key)
    # 넣으려는 값이 더 크면? -> 오른쪽 서브트리로 재귀 호출 후 내 오른쪽 참조에 연결
    elif key > node.data:
        node.right = insert_node(node.right, key)
        
    # [Step 3] 부모와의 연결이 끊어지지 않도록 현재 노드를 반환
    return node

# 3. 데이터 삭제
def delete_node(root, key):
    # 1. 트리가 비어있거나 끝까지 찾았는데 없는 경우
    if root is None: 
        return root

    # 2. 삭제할 값 찾으러 아래로 내려가기 (재귀 호출)
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    # 3. 드디어 삭제할 노드를 찾은 경우! (key == root.data)
    else:
        # [Case 1 & 2] 자식이 없거나(단말 노드), 하나만 있는 경우
        if root.left is None:
            temp = root.right # 오른쪽 자식을 임시 저장
            root = None # 나를 지웁니다.
            return temp # 기억해 둔 자식을 부모 노드로 올려보냅니다.
        elif root.right is None:
            temp = root.left # 왼쪽 자식을 임시 저장
            root = None # 나를 지웁니다.
            return temp # 기억해 둔 자식을 부모 노드로 올려보냅니다.
        
        # [Case 3] 자식이 둘다 있는 경우
        # 1단계: 오른쪽 트리(root.right)에서 가장 작은 후계자를 찾아 temp에 저장합니다.
        temp = get_min_node(temp)
        # 2단계: 현재 삭제할 노드(root)의 데이터에 후계자의 데이터를 복사(덮어쓰기)합니다.
        root.data = temp
        # 3단계: 이제 데이터가 복사되었으니, 오른쪽 트리로 가서 원래 후계자가 있던 노드를 삭제합니다.
        # (재귀적으로 delete_node를 호출하여 껍데기를 정리합니다.)
        root.right = delete_node(root.data, root.left)
        
    return root

# 중위 순회
def inorder (node):
    if node is not None:
        inorder (node.left)
        print(node.data, end=' ')
        inorder (node.right)

# === main 부분 ===
if __name__ == "__main__":
    root = None
    while True:
        print("\n=== 몬스터 도감 메뉴 ===")
        print("1. 도감 삽입")
        print("2. 도감 탐색")
        print("3. 도감 삭제")
        print("4. 현재 도감 출력 (중위 순회)")
        print("0. 프로그램 종료")
        
        choice = input("메뉴를 선택하세요: ")
        
        if choice == '1':
            val = int(input("삽입할 ID를 입력하세요: "))
            root = insert_node(root, val)
            print(f"[{val}] 삽입 완료!")
        elif choice == '2':
            val = int(input("탐색할 ID를 입력하세요: "))
            if search_rec(root, val):
                print(f"탐색 성공: {val}번 몬스터가 도감에 있습니다!")

            else:
                print(f"탐색 실패: {val}번 몬스터를 찾을 수 없습니다.")
        elif choice == '3':
            val = int(input("삭제할 숫자를 입력하세요: "))
            # 삭제 전 트리에 해당 값이 존재하는지 탐색으로 확인
            if search_rec(root, val):
                root = delete_node(root, val)
                print(f"[{val}] 삭제 완료!")
                print("현재 도감 (오름차순): ", end="")
                if root is None:
                    print("도감이 비어있습니다.")
                else:
                    inorder (root)
                    print()
            else:
                print(f"[{val}]이(가) 도감에 존재하지 않아 삭제할 수 없습니다.")
        elif choice == '4':
            print("현재 도감 (오름차순): ", end="")
            if root is None:
                print("도감이 비어있습니다.")
            else:
                inorder (root)
                print


        elif choice == '0':
            print("프로그램을 종료합니다.")
            break