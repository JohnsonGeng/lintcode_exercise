'''
问题描述：
余弦相似性是内积空间的两个矢量之间的相似性的度量，
其测量它们之间的角度的余弦。
0度的余弦为1，对于任何其他角度，余弦小于1。
公式不打了。
示例：
输入：A = [1,4,0], B = [1,2,3]
输出：0.5834
思路：分别计算A·B、A的二范数、B的二范数带入公式即可
'''

def cosineSimilarity(A, B):
    # write your code here
    # 思路：分别计算A·B、A的二范数、B的二范数即可
    product_A_B = 0
    norm_A = 0
    norm_B = 0
    for i, j in zip(A, B):
        product_A_B += i * j
        norm_A += i * i
        norm_B += j * j
        # 判断以下是否符合条件
    if norm_A == 0 or norm_B == 0:
        return 2.0000
    else:
        return product_A_B / ((norm_A ** 0.5) * (norm_B ** 0.5))

if __name__ == '__main__':
    A = [1,4,0]
    B = [1,2,3]
    print(cosineSimilarity(A, B))