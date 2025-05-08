# Output: True if the string is a valid regex, False otherwise.
import re
def is_valid_regex(s):
    try:
        re.compile(s)
        return True
    except re.error:
        return False

n = int(input())
for i in range(n):
    str = input()
    print(is_valid_regex(str))