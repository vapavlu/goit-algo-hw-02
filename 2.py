from collections import deque

def is_palindrome(s):
    # Видалити пробіли та зробити всі символи нижнім регістром
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Створити двосторонню чергу
    d = deque(s)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Приклади використання
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("dad"))