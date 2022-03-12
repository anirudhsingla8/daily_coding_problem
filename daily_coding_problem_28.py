"""
This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
 Pad extra spaces when necessary so that each line has exactly length k.
 Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16,
 you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""


def fullJustify(words, maxWidth):
    j = 0
    ans = []
    n = len(words)
    while j < n:
        curr_str = ""
        i = j
        curr_sum = 0
        space = 0
        while j < n and curr_sum + len(words[j]) + space <= maxWidth:
            curr_sum += len(words[j])
            j += 1
            space += 1
        total_spaces = maxWidth - curr_sum
        if j >= n:
            flag = "first"
            for x in range(i, j):
                if flag == "first":
                    curr_str = curr_str + words[x]
                    flag = "last"
                else:
                    curr_str = curr_str + " " +words[x]
        else:

            mandatory_spaces = total_spaces // (j - i - 1 or 1)
            extra_spaces = total_spaces % (j - i - 1 or 1)
            for x in range(i, j):
                curr_str = curr_str + words[x]
                s = 0
                while s < mandatory_spaces and x < j - 1:
                    curr_str = curr_str + " "
                    s += 1
                if extra_spaces > 0:
                    extra_spaces -= 1
                    curr_str = curr_str + " "
        while len(curr_str) < maxWidth:
            curr_str = curr_str + " "
        ans.append(curr_str)
    return ans


words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
ans = fullJustify(words, maxWidth)
print(ans)
