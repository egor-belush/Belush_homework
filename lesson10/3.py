"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""

def check_parentheses(s):
    balance = 0
    
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
    
    return balance == 0


test_cases = [
    "(()())",
    "(()()()",
    "(hello(2)ver()(33)python)",
    "(hello(2()ver(33)python))",
    "(hello(2()ver(33)python)"
]

for test_str in test_cases:
    result = check_parentheses(test_str)
    print(result)