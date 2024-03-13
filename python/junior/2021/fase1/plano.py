quotaMensal = int(input())
meses = int(input())

for x in range(meses):
    megaGasto = int(input())
    if x == 0:
        quotaResto = quotaMensal - megaGasto
        proxQuota = quotaResto + quotaMensal
    else:
        proxQuota = (proxQuota - megaGasto) + quotaMensal

print(proxQuota)
