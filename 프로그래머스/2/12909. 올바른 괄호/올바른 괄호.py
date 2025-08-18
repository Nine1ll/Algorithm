def solution(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return True if not stack else False