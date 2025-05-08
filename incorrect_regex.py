# Output: True if the string is a valid regex, False otherwise.
"""
To check if a regular expression pattern is valid in Python before using it for matching, the re.compile() function can be used within a try-except block. If the pattern is invalid, it will raise a re.error exception, which can be caught and handled.
"""
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