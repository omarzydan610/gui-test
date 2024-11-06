
def handel(arr):
    res = []
    for i in arr:
        x = 0
        for j in i:
            x += j
        res.append(x)
    return res


arr = [[1,2,3], [1,2,3], [1,2,3]]
print(handel(arr))