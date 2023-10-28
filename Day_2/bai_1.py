a = 10
b = 5

result = f'''
{a} + {b} = {a + b}
{a} - {b} = {a - b}
{a} * {b} = {a * b}
{a} // {b} = {a // b}
{a} ^ {b} = {a ** b}
{a} % {b} = {a % b}
{a} > {b} = {a > b}
{a} < {b} = {a < b}
{a} == {b} = {a == b}
{a} & {b} = {a & b}
{a} | {b} = {a | b}
{a} XOR {b} = {a ^ b}
{a} != {b} = {a != b}
{a} dịch phải 5 bit = {a >> 5} 
{a} dịch trái 6 bit = {a << 6}
in hệ cơ số 2 đảo ngược của a {bin(a)[2:][::-1]}
'''
print(result)