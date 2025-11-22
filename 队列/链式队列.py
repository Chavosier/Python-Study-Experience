'''
Description
链表指的是将需要处理的数据对象以节点的形式，通过指针串联在一起的一种数据结构。链表中的每个节点一般由数据区域和指针区域两部分构成，其中数据区域用于保存实际需要处理的数据元素，指针区域用来保存该节点后继节点的存储地址。 
img 下面我们用循环单链表来模拟队列的操作，如图a、图b所示：

（1）初始时循环单链表为空队列：data[[0,0]], 此时：head=tail=0

（2）用循环单链表模拟元素入队操作，无需考虑溢出情况。

（3）在循环单链表中实现删除队列表头元素，实际上删除的是head的后继节点。

（4）在循环单链表中添加新元素，新元素追加在tail指针后面、head指针前面。

（5）在循环单链表中，实际上仅用tail指针也可实现上述操作（因为head可表示为data[tail][1]）。

给出一组有关队列的操作，输出相关队列出队信息。

请从循环单链表表头开始，依次输出单链表中各个节点的数据信息。

说明：

（1）若队列为空(head==tail)，此时执行出队操作"O"，则给出报错信息"ERR empty!"，直接结束后续操作。

（2）可将head指向的节点看作是一个虚点，因此链表中第一个节点数据是head后面节点。

Format
Input
给出对链式队列的一组操作（I x:将元素x追加在链式队列表尾；O:删除链式队列队首元素）。

Output
第1行，若存在出队信息，则根据链式队列操作，输出队列中出队的各个节点值（用","间隔）。

若存在链式队列，接下来若干行，按单链表的逻辑次序，队首节点节点开始，依次输出链式队列中各节点的数据信息(数据值、指针域)。

Samples
输入数据 1
I,3,I,5,I,7,O,I,11,O,I,4,I,9
输出数据 1
3,5
7 4
11 5
4 6
9 0'''
l=list(input().split(','))
data=[[0,0]]
head=tail=0
for i in range(len(l)):
    if l[i]=='I':
        data.append([int(l[i+1]),0])
        data[tail][1]=len(data)-1
        tail=len(data)-1
    elif l[i]=='O':
        if head==tail:
            print("ERR empty!")
            break
        else:
            head=data[head][1]
            print(data[head][0],end=',' if i<len(l)-1 and 'O' in l[i+1:] else '\n')#出队
while head!=tail:
    head=data[head][1]
    print(data[head][0],data[head][1])