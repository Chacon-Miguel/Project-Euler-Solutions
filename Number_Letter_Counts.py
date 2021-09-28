def n2words(n):
    if n==0: return 'Zero'
    units = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    teens = ['','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen', \
             'Seventeen','Eighteen','Nineteen']
    tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy', \
            'Eighty','Ninety']
    thousands = ['','Thousand','Million','Billion','Trillion','Quadrillion']
    words = []
    number = map(''.join, zip(*[iter(str(n).zfill(18))]*3))
    for nx, g in enumerate(number, 1):
        if g=='000': continue
        h,t,u = map(int, g)
        if h>0: words+= [units[h], 'Hundred']
        if t==1:
            words+= [teens[u]] if u>0 else [tens[t]]
        else:
            if t>0: words+= [tens[t]]
            if u>0: words+= [units[u]]
        words+= [thousands[6-nx]]
    return ''.join(words)

count = 0
for numb in range(1, 1001):
    count += len(n2words(numb))
print(count+(99*9*3))