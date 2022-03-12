"""
This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content "Hello world", three read7() returns "Hello w", "orld" and then "".
"""


def read(read_len, elements):
    n = len(elements)
    if n <= read_len:
        return elements
    ans = []
    i = 0
    while i < n:
        count = 0
        curr_str = ""
        while count < read_len:
            if i < n:
                curr_str = curr_str + elements[i]
            else:
                ans.append(curr_str)
                return ans
            count += 1
            i += 1
        ans.append(curr_str)
    return ans


ans = read(5, "anirudh singla")
print ans
