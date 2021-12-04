# The most important part is to deal with "*"
#   if there is a match for char in "*":
#       we have three choice: 1: don't use the match: move p 2: use match (move s) but keep p 3: use match (move s) but finish using p
#   if there is not a match:
#       The only choice is to move p and keep s
# There are three edge case: 1: s and p are both used up: Match! 2: p use up but s is not: Not Match! 
#                            3. s use up and p remain: This depends on if p has a "*". If p have * then is similar to the unmatch case above: move p
#                               if not: Not Match!

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def match(sidx, pidx):
            if (sidx, pidx) in dp:
                return dp[(sidx, pidx)]
            if sidx >= len(s) and pidx >= len(p):
                return True
            if pidx >= len(p):
                return False
            isMatch = sidx < len(s) and (s[sidx] == p[pidx] or p[pidx] == '.') #check if there is a match can be used later
            if pidx + 1 < len(p) and p[pidx + 1] == "*":
                if isMatch: #if a match is reached, we have three choice
                    dp[(sidx, pidx)] =  match(sidx, pidx + 2) or match(sidx + 1, pidx + 2) or match(sidx + 1, pidx)
                    return dp[(sidx, pidx)]
                else: #no match, give up p char before *
                    dp[(sidx, pidx)] = match(sidx, pidx + 2)
                    return dp[(sidx, pidx)]
            if isMatch: #no star
                dp[(sidx, pidx)] = match(sidx + 1, pidx + 1)
                return dp[(sidx, pidx)]
            else:
                dp[(sidx, pidx)] = False
                return dp[(sidx, pidx)]
        return match(0, 0)
                    