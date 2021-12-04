# The same approach as word search 1. Except the memo store the path that have gone through. 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}
        memo[len(s)] = [[]]
        def help(idx):
            if idx in memo:
                return memo[idx]
            res = []
            for j in range(idx + 1, len(s) + 1):
                if s[idx:j] in wordDict:
                    if j not in memo:
                        memo[j] = help(j)
                    prefix = s[idx:j]
                    suffixs = memo[j]
                    for suffix in suffixs:
                        newres = suffix.copy()
                        newres.insert(0, prefix)
                        res.append(newres)
            memo[idx] = res
            return memo[idx]
        help(0)
        output = []
        for res in memo[0]:
            output.append(" ".join(res))
        return output