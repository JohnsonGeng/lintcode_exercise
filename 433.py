'''


'''


def numIslands(grid):
    # write your code here
    # 思路：遍历数组，每个元素只需要和其前面（除每行最后一个外）和下面（最后一行除外）的元素
    # 每次碰到1才计数，如果其前面的元素或者上面的元素为1的话，也不计数
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # 第一行的情况
            if i == 0:
                # 第一行第一列的情况
                if j == 0:
                    if grid[i][j] == 1:
                        count += 1
                # 第一行其他列的情况
                else:
                    if grid[i][j] == 1:
                        if grid[i][j-1] == 0:
                            count += 1
                        else:
                            continue
            # 其他行的情况
            else:
                # 其他行第一列的情况
                if j == 0:
                    if grid[i][j] == 1 and grid[i - 1][j] == 0:
                        count += 1
                    else:
                        continue
                #其他行其他列情况
                else:
                    if grid[i][j] == 1:
                        if grid[i-1][j] == 0 and grid[i][j-1] == 0:
                            count += 1
                        else:
                            continue
                    else:
                        continue
    return count


if __name__ == '__main__':
    grid = [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]
    print(numIslands(grid))