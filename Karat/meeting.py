def canArrange(arr, meeting):
    start, end = meeting
    for s, e in arr:
        if (start > s and start < e) or (end > s and end < e) or (start < s and end > e):
            return False
    return True
def mergeInterval(arr):
    arr.sort(key = lambda x: int(x))
    res = []
    start, end = arr[0]
    for s, e in arr:
        if s <= end:
            end = max(end, e)
        else:
            res.append(start, end)
            start = s
            end = e


        
