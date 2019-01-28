x = int(input('Ketik angka: '))

def factor(a):
    factor=[]
    for i in range(1,a+1):
        if a%i == 0:
            factor.append(i)
    return factor

def categorize(x):
    list1 = []
    if isinstance(x, int) :
        list1.append('bulat')
    if x >= 0:
        list1.append('cacah')
    if x<0:
        list1.append('negatif')
    if x == 0:
        list1.append('nol')
    if x>0:
        list1.append('asli')
    if x%2 !=0:
        list1.append('ganjil')
    if x%2 == 0:
        list1.append('genap')
    if x != 1 and sum(factor(x))==x+1:
        list1.append('prima')
    if x >0 and sum(factor(x))!=x+1:
        list1.append('komposit')
        
    return list1
print(categorize(x))