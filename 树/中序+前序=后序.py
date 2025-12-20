'''
说明
树和二叉树基本上都有先序、中序、后序、按层遍历等遍历顺序，给定中序和其它一种遍历的序列就可以确定一棵二叉树的结构。
假定一棵二叉树一个结点用一个字符描述，现在给出中序和前序遍历的字符串，求该树的后序遍历字符串。
输入格式
输入文件flist.in共两行，每行是由字母组成的字符串（一行的每个字符都是唯一的），分别表示二叉树的中序遍历和前序遍历的序列。
输出格式
输出文件flist.out就一行，表示二叉树的后序序列。
输入数据 1
DBGEHACIJF
ABDEGHCFIJ
输出数据 1
DGHEBJIFCA
'''
s1=input()
s2=input()
def reconstruct_postorder(s1, s2):
    if len(s1) == 1:
        print(s1, end='')
        return
    root = s2[0]
    k = s1.find(root)
    if len(s1[:k]) >= 1:
        reconstruct_postorder(s1[:k], s2[1:k+1])
    if len(s1[k+1:]) >= 1:
        reconstruct_postorder(s1[k+1:], s2[k+1:])
    print(root, end='')
reconstruct_postorder(s1, s2)