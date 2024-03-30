class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_in_t = set([])
        looking_for = {}
        extras = {}
        for char in t:
            if char not in chars_in_t:
                chars_in_t.add(char)
                looking_for[char] = 0
            looking_for[char] += 1
        window_left = 0
        window_right = 0
        current_min_len = len(s) + 1
        current_min = ""
        while window_right <= len(s):
            if looking_for:
                if window_right < len(s) and s[window_right] in chars_in_t:
                    if s[window_right] in looking_for:
                        looking_for[s[window_right]] -= 1
                        if looking_for[s[window_right]] == 0:
                            looking_for.pop(s[window_right])
                    else:
                        if s[window_right] not in extras:
                            extras[s[window_right]] = 0
                        extras[s[window_right]] += 1
                window_right += 1
            else:
                if window_right - window_left < current_min_len:
                    current_min_len = window_right - window_left
                    current_min = s[window_left: window_right]
                if s[window_left] in chars_in_t:
                    if s[window_left] in extras:
                        extras[s[window_left]] -= 1
                        if extras[s[window_left]] == 0:
                            extras.pop(s[window_left])
                    else:
                        if s[window_left] not in looking_for:
                            looking_for[s[window_left]] = 0
                        looking_for[s[window_left]] += 1
                window_left += 1
        return current_min
