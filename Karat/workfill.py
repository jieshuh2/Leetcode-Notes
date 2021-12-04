def wordWratp(words, maxLen):
    if (words == None or len(words) == 0):
        return
    res = []
    start = 0
    while(start < len(words)):
        remain = maxLen
        end = start
        while(end < len(words) and remain - len(words[end])>= 0):
            remain -= len(words[end]) + 1
            end += 1
        res.append("-".join(words[start: end]))
        start = end
    return res
words = ["h", "e", "l", "o"]
print(wordWratp(words, 7))
