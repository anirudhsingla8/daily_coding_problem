"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def validParenthesis(elements):
    st = []
    n = len(elements)
    for i in range(0, n):
        if elements[i] in ["(", "[", "{"]:
            st.append(elements[i])
        elif elements[i] == ")":
            if len(st) == 0 or st[-1] != "(":
                return False
            else:
                st.pop()
        elif elements[i] == "]":
            if len(st) == 0 or st[-1] != "[":
                return False
            else:
                st.pop()
        elif elements[i] == "}":
            if len(st) == 0 or st[-1] != "{":
                return False
            else:
                st.pop()
    if len(st) == 0:
        return True
    return False


elements = "([])[]({})"
ans = validParenthesis(elements)
print(ans)
