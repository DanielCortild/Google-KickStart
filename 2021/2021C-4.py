"""
Google Kick Start - Round C 2021 - Q4 [SOLVED]
Daniel Cortild - 23/05/2021
"""

f1 = lambda a, b : hash((a, b)) % 65537 + 1
f2 = lambda a, b : hash((a, b)) % 2 + 1
f3 = lambda a, b : a & b + 1
f4 = lambda a, b : a ^ b + 1

def precedence(op):
    if op == '+': return 1
    if op == '*': return 2
    if op == '#': return 3
    return 0
 
def applyOp(a, b, op, f):
    if op == '+': return a + b
    if op == '*': return a * b
    if op == '#': return f(a, b)

def evaluate(tokens, f):
    values = []
    ops = []
    i = 0
    while i < len(tokens):
        if tokens[i] == ' ':
            i += 1
            continue
        elif tokens[i] == '(':
            ops.append(tokens[i])
        elif tokens[i].isdigit():
            val = 0
            while (i < len(tokens) and
                tokens[i].isdigit()):
                val = (val * 10) + int(tokens[i])
                i += 1
            values.append(val)
            i-=1
        elif tokens[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                values.append(applyOp(values.pop(), values.pop(), ops.pop(), f))             
            ops.pop()         
        else:
            while (len(ops) != 0 and precedence(ops[-1]) >= precedence(tokens[i])):
                values.append(applyOp(values.pop(), values.pop(), ops.pop(), f))
            ops.append(tokens[i])
        i += 1
     
    while len(ops) != 0:
        values.append(applyOp(values.pop(), values.pop(), ops.pop(), f))
    return values[-1]

for T in range(int(input())):
    vals1 = []
    vals2 = []
    vals3 = []
    vals4 = []
    equi_class = 1
    equi_classes = []

    for i in range(int(input())):
        S = input()
        v1 = evaluate(S, f1)
        v2 = evaluate(S, f2)
        v3 = evaluate(S, f3)
        v4 = evaluate(S, f4)
        if vals1.count(v1) != 0 and vals2.count(v2) != 0 and vals3.count(v3) != 0 and vals4.count(v4) != 0:
            for j in range(len(vals1)):
                if vals1[j] == v1 and vals2[j] == v2 and vals3[j] == v3 and vals4[j] == v4:
                    equi_classes.append(equi_classes[j])
                    break
            else:
                equi_classes.append(equi_class)
                equi_class += 1
        else:
            equi_classes.append(equi_class)
            equi_class += 1
        vals1.append(v1)
        vals2.append(v2)
        vals3.append(v3)
        vals4.append(v4)

    print(f"Case #{T+1}: {' '.join([str(v) for v in equi_classes])}")