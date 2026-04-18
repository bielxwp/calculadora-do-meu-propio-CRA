def media(*listas):
    total = sum(len(lista) for lista in listas)
    soma_total = sum(sum(lista) for lista in listas)

    media = soma_total / total
    return media



#p3
c3 = []
al1 = []
series_edo = []
fg3 = []
fcomp = []
pesq_apl = []
prob_estat = []


# p2
c2 = [10, 10, 10]
fexp = [9, 9.1, 9.8]
fg2 = [8, 9, 5.5]
ic = [10, 9, 10]
al = [10, 10, 10]
elem = [9.4,10,9.7]

# p1
c1 = [6.3, 9.8, 10]
ga = [9.3, 8.7, 8.7]
fg1 = [10, 8.7, 10]
mtc = [9.3, 9.8, 7.8]
qfnd = [10, 10, 8]


resultado = media(c3,al1,series_edo,fg3,fcomp,pesq_apl,prob_estat,c2, fexp, fg2, ic, al, elem, c1, ga, fg1, mtc, qfnd)

print(f"o CRA é: {resultado:.2f}")
