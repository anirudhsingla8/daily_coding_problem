"""
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less.
You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words.
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10,
you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
"""


def wordWrap(elements, k):
    elements = elements.split(" ")
    n = len(elements)
    ans = []
    i=0
    while i<n:
        curr_len = 0
        space = 0
        j = i
        curr_str = ""
        while j < n and curr_len + len(elements[j]) + space <= k:
            curr_len += len(elements[j])
            j += 1
            space += 1
        first = False
        for x in range(i, j):
            if first:
                curr_str = curr_str + " "
            curr_str = curr_str + elements[x]
            first = True
        i = j
        ans.append(curr_str)
    return ans


k = 10
elements = "the quick brown fox jumps over the lazy dog"
ans = wordWrap(elements, k)
print(ans)
