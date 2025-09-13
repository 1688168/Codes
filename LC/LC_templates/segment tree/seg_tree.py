MAX_LEN=1000

def build_tree(arr, tree, node, start, end):
    if start==end:
        tree[node]=arr[start]
        return
    left_node=2*node+1
    right_node=2*node+2
    mid = start +(end-start)//2
    build_tree(arr, tree, left_node, start, mid)
    build_tree(arr, tree, right_node, mid+1, end)

    tree[node]=tree[left_node]+tree[right_node]



def update_tree(arr, tree, node, start, end, idx, val):
    if start==end:
        arr[idx]=val
        tree[node]=val
        return
    mid=start+(end-start)//2
    left_node=2*node+1
    right_node=2*node+2
    if idx >= start and idx <= mid:
        update_tree(arr, tree, left_node, start, mid, idx, val)
    else:
        update_tree(arr, tree, right_node, mid+1, end, idx, val)

    tree[node]=tree[left_node]+tree[right_node]

def query_tree(arr, tree, node, start, end, L, R):
    if R < start or L > end: return 0

    if start==end: return tree[node]
    if start >=L and end <= R: return tree[node]

    mid = start+(end-start)//2
    left_node = node*2+1
    right_node = node*2+2

    sum_left=query_tree(arr, tree, left_node, start, mid, L, R)
    sum_right=query_tree(arr, tree, right_node, mid+1, end, L, R)

    return sum_left+sum_right


def main():
    print("----- hello seg tree -----")
    arr=[1, 3, 5, 7, 9, 11]
    size = 6
    tree=[0]*MAX_LEN

    build_tree(arr, tree, 0, 0, size-1)
    print(tree)

    update_tree(arr, tree, 0, 0, size-1, 4, 6)
    print(tree)

    s=query_tree(arr, tree, 0, 0, size-1, 2, 5)

    print("query: ", s)
if __name__=='__main__':
    main()
