## Início: [10].[0].[0].[1]
## Final: [255].[255].[255].[255]
## Diff: [245].[255].[255].[254]

def CalucularIPs(ipIni, ipFim):
    ipIni = SepararClasses(ipIni)
    ipFim = SepararClasses(ipFim)
    ipDif = []
    for i in range(len(ipIni)):
        ipDif.append(ipFim[i] - ipIni[i])
    qtdIps = MultiplicarPosterior(ipDif)
    return qtdIps

def MultiplicarPosterior(array):
    total = 0
    for i in range(1, len(array)):
        if array[i] == 0 or array[i] == 0:
            total *= 1
        else:
            total += array[i - 1] * array[i]
    return total

def SepararClasses(ip): 
    return list(map(lambda x: int(x), (ip.strip()).split('.')))

print(CalucularIPs('192.168.1.200', '192.168.1.255'))