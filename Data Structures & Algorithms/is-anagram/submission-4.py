class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        all_chars_s = []
        for c in s:
            all_chars_s.append(c)
        for c in t:
            if c in all_chars_s:
                i = all_chars_s.index(c)
                all_chars_s_pre = all_chars_s[0:i]
                all_chars_s_post = all_chars_s[i+1:]
                all_chars_s = all_chars_s_pre + all_chars_s_post
                continue
            return False

        if all_chars_s == []: return True
        return False       