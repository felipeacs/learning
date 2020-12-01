# Check if the parentheses are balanced

list_parentheses = ['()', '((', '(Hello,(World))',
                    ')Yello(', 'Right)', 'Le()ft',
                    'par(en)the)ses'
                    ]


def is_balanced(str):
    count = 0
    for ch in str:
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1
        if count < 0:
            return False  # first goes ')'
    return count == 0  # balanced


for value in list_parentheses:
    print('Value: {}, is balanced: {}'.format(value, is_balanced(value)))
