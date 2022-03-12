"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def encode(message):
    n = len(message)
    count = [0] * (n + 1)
    count[0] = 1
    count[1] = 1 if int(message[0]) >= 1 else 0
    for i in range(2, n + 1):
        if int(message[i - 1]) >= 1:
            count[i] = count[i - 1]
        if 1 <= int(message[i - 2]) <= 2 and int(message[i - 1]) <= 6:
            count[i] = count[i - 2] + count[i]
    return count[n]


def encode1(message):
    n = len(message)
    count = [0] * (n + 1)
    count[0] = 1
    count[1] = 1 if int(message[0]) >= 1 else 0
    for i in range(2, n + 1):
        onedigit = int(message[i - 1])
        twodigit = int(message[i - 2:i])

        if onedigit >= 1:
            count[i] += count[i - 1]

        if twodigit >= 10 and twodigit <= 26:
            count[i] += count[i - 2]
    return count[n]


message = "12023"
ans = encode1(message)
print(ans)
