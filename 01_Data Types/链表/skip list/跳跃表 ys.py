import random
MAX_LEVEL, P = 16, 0.5
nodes, cur_level = [[None, None, [None] * MAX_LEVEL]], 0

def random_level():
    lv = 0
    while lv < MAX_LEVEL - 1 and random.random() < P: 
        lv += 1
    return lv

def search(key):
    cur = 0
    for i in range(cur_level, -1, -1):
        while True:
            nxt = nodes[cur][2][i]
            if nxt is None or nodes[nxt][0] >= key: 
                break
            cur = nxt
    nxt = nodes[cur][2][0]
    return nodes[nxt][1] if nxt is not None and nodes[nxt][0] == key else None

def insert(key, val):
    global cur_level, nodes
    update, cur = [None] * MAX_LEVEL, 0
    for i in range(cur_level, -1, -1):
        while True:
            nxt = nodes[cur][2][i]
            if nxt is None or nodes[nxt][0] >= key: break
            cur = nxt
        update[i] = cur
    nxt = nodes[cur][2][0]
    if nxt is not None and nodes[nxt][0] == key:
        nodes[nxt][1] = val; return
    new_level = random_level()
    if new_level > cur_level:
        for i in range(cur_level + 1, new_level + 1): update[i] = 0
        cur_level = new_level
    new_node = [key, val, [None] * (new_level + 1)]
    new_idx = len(nodes)
    nodes.append(new_node)
    for i in range(new_level + 1):
        new_node[2][i] = nodes[update[i]][2][i]
        nodes[update[i]][2][i] = new_idx

def remove(key):
    global cur_level, nodes
    update, cur = [None] * MAX_LEVEL, 0
    for i in range(cur_level, -1, -1):
        while True:
            nxt = nodes[cur][2][i]
            if nxt is None or nodes[nxt][0] >= key: break
            cur = nxt
        update[i] = cur
    target = nodes[cur][2][0]
    if target is None or nodes[target][0] != key: return None
    for i in range(cur_level + 1):
        if nodes[update[i]][2][i] != target: break
        nodes[update[i]][2][i] = nodes[target][2][i]
    while cur_level > 0 and nodes[0][2][cur_level] is None: cur_level -= 1
    return nodes[target][1]

# main
insert(1, 'a'); insert(2, 'b'); insert(3, 'c'); insert(4, 'd'); insert(5, 'e')
def print_list():
    print(f"\n层数:{cur_level} 节点:{len(nodes)}")
    for i in range(cur_level, -1, -1):
        s, cur = [], nodes[0][2][i]
        while cur is not None: s.append(str(nodes[cur][0])); cur = nodes[cur][2][i]
        print(f"L{i}: {'->'.join(s)}")
print_list()
print(f"search(3)={search(3)}")
remove(3)
print(f"remove后 search(3)={search(3)}")
print_list()
