import random

# 打开文档
# ＋－×÷  □★……≠▲◆●☆
# math_add math_sub math_mul math_div

def math_add(n, d):
    number_a = random.randint(10, 199)
    number_b = random.randint(10, 199)
    result_a = number_a + number_b
    while result_a % 10 != 0:
        number_a = random.randint(10, 199)
        number_b = random.randint(10, 199)
        result_a = number_a + number_b
    math_add_str = str(number_a) + ' ＋ ' + str(number_b)
    return math_add_str

def math_sub(n, d):
    number_a = random.randint(10, 199)
    number_b = random.randint(10, 199)
    result_a = number_a - number_b
    while result_a <= 0:
        number_a = random.randint(10, 199)
        number_b = random.randint(10, 199)
        result_a = number_a - number_b
    math_sub_str = str(number_a + number_b) + ' － ' + str(number_a)
    return math_sub_str

def math_mul():
    number_a = random.randint(2, 9)
    number_b = random.randint(2, 9)
    result_a = number_a * number_b
    while result_a <= 10:
        number_a = random.randint(2, 9)
        number_b = random.randint(2, 9)
        result_a = number_a * number_b
    math_mul_str = str(number_a) + ' × ' + str(number_b)
    return math_mul_str

def math_div():
    number_a = random.randint(2, 9)
    number_b = random.randint(2, 9)
    result_a = number_a * number_b
    while result_a <= 10:
        number_a = random.randint(2, 9)
        number_b = random.randint(2, 9)
        result_a = number_a * number_b
    math_div_str = str(result_a) + ' ÷ ' + str(number_a)
    return math_div_str

print('□  %s = （    ）' % (math_add(2, 1)))
print('□  %s = （    ）' % (math_sub(2, 1)))

print('□  %s = （    ）' % (math_mul()))
print('□  %s = （    ）' % (math_div()))

#print('□  %s = （    ）' % (math_add()))

