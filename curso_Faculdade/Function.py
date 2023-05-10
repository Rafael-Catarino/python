def soma(*num):  # function tradicional.
    resp = 0
    for n in num:
        resp += n
    return resp


print(soma(9, 4, 7, 2))


soma = lambda *num: sum(num)  # function lambda
print(soma(3, 4))
