'''
题目描述
给你一个长度为 N 的数组，一个长为 K 的滑动窗口从最左端移至最右端，你只能看到窗口中的 K 个数，每次窗口向右移动一位，如下图：

窗口位置	最小值	最大值
[ 1  3  -1] -3  5  3  6  7	-1	3
1 [3  -1  -3] 5  3  6  7	-3	3
1  3 [-1  -3   5] 3  6  7	-3	5
1  3  -1 [-3   5   3] 6  7	-3	5
1  3  -1  -3 [5   3   6] 7	3	6
1  3  -1  -3   5 [3   6   7]	3	7
你的任务是找出滑动窗口在各个位置的最大值和最小值。

输入格式
第 1 行：两个整数 N 和 K，分别表示数组的长度和滑动窗口的大小。
第 2 行：N 个整数，表示数组的 N 个元素（每个元素的值 ≤ 2 × 10⁹）。
输出格式
第 1 行：滑动窗口从左向右移动到每个位置时的最小值，每个数之间用一个空格分开。
第 2 行：滑动窗口从左向右移动到每个位置时的最大值，每个数之间用一个空格分开。

8 3
1 3 -1 -3 5 3 6 7

-1 -3 -3 -3 3 3
3 3 5 5 6 7
'''
def bite_biteme(l):
    ll=[]
    new_head=head
    while new_head!=tail:
        ll.append(l[new_head])
        new_head=(new_head+1+M)%M
    return ll
n,k=map(int,input().split())
arr=list(map(int,input().split()))
que=['bite me']*(k+1)
for i in range(k):
    que[i]=arr[i]
head=0;tail=k;M=k+1
arr_min=[min(bite_biteme(que))];arr_max=[max(bite_biteme(que))]
for _ in range(n-k):
    head=(head+1+M)%M
    que[tail]=arr[k]
    tail=(tail+1+M)%M
    k+=1
    arr_min.append(min(bite_biteme(que)));arr_max.append(max(bite_biteme(que)))
for j in range(len(arr_min)):
    print(arr_min[j],end=' ')
print()
for j in range(len(arr_max)):
    print(arr_max[j],end=' ')