"""
 This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
 You can assume the string to be decoded is valid.
"""

def encoding(elements):
    prev = None
    ans = ""
    n=len(elements)
    curr_sum = 0
    for i in range(0,n):
        if prev == None:
            prev = elements[i]
            curr_sum+=1
        elif prev != elements[i]:
            ans = ans + str(curr_sum) + prev
            prev = elements[i]
            curr_sum = 1
        else:
            curr_sum += 1
    ans = ans + str(curr_sum) + prev
    return ans

elements = "AABBBCCDAA"
ans = encoding(elements)
print(ans)