def fun(x):
    for k in dct1:
        if x in k:
            return dct1.get(k)


dct1 = {
    'AEIOULNSTR' : 1, 'DG' : 2, 'BCMP' : 3,
    'FHVWY' : 4, 'K' : 5, 'JX' : 8, 'QZ' :10, 
    'АВЕИНОРСТ' : 1, 'ДКЛМПУ': 2, 'БГЁЬЯ' : 3,
    'ЙЫ' : 4, 'ЖЗХЦЧ' : 5, 'ШЭЮ' : 8, 'ФЩЪ' :10
    }


print("введите слово:")            
print(sum(map(fun, input())))