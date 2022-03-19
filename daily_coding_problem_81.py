"""
This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string,
return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {"2": ["a", "b", "c"], "3": ["d", "e", "f"],...} then "23" should
return ["ad", "ae", "af", "bd, "be", "bf", "cd", "ce", "cf"].
'digits' must consist of values from 2 to 9 only
"""

def mapping(digits):
    n = len(digits)
    if n == 0:
        return []
    mapp = {
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    ans = []
    ans2 = []
    for i in range(0, n):
        if i == 0:
            for x in mapp[digits[i]]:
                ans.append(x)
            continue
        for j in range(0, len(ans)):
            for x in mapp[digits[i]]:
                curr_str = ans[j] + x
                ans2.append(curr_str)
        ans = ans2
        ans2 = []
    return ans


ans = mapping("295856")
print(ans)