class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        if len(s) == 0: return True

        mapping = {")": "(", "}": "{", "]": "["}
        ls = list(s)
        o = []
        for i,n in enumerate(s):
            if n not in mapping.keys():
                o.append(n)
            else:
                t = mapping[n]
                if len(o) == 0: return False
                if o[-1] == t:
                    o.pop()
                else:
                    return False
        return len(o) == 0