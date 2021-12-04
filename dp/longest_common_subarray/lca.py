#similar to LCS but this time our dp store the longest subarray start at the given position, so list1 and list2 should match at this posiition.
def lcsa(list1, list2):
    dp = [[0 for j in range(len(list2) + 1)] for i in range(len(list1) + 1)]
    maxlen = 0
    idx = (-1, -1)
    for i in range(len(list1)-1, -1, -1):
        for j in range(len(list2) - 1, -1, -1):
            if list1[i] == list2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
                if dp[i][j] > maxlen:
                    maxlen = dp[i][j]
                    idx = (i, j)
    if idx[0] < 0:
        return []
    i, j = idx
    return list1[i: i + dp[i][j]]
arr1 = [1, 2, 8, 2, 1]
arr2 = [8, 2, 1, 4, 7]
print(lcsa(arr1, arr2))

