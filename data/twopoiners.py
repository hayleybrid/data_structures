#valid palindrome
#given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    s = input().strip()
    result = is_palindrome(s)
    print("True" if result else "False")