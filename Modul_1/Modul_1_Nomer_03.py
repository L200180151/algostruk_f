def jumlahHurufVokal(kata):
    vokal = ['a', 'i', 'u', 'e', 'o']
    kata2 = kata.lower()
    list_kata = []
    list_kata.append(len(kata2))
    count = 0
    for i in kata2:
        if i in vokal:
            count += 1
    list_kata.append(count)
    return list_kata

def jumlahHurufKonsonan(kata):
    vokal = ['a', 'i', 'u', 'e', 'o']
    kata2 = kata.lower()
    list_kata = []
    list_kata.append(len(kata2))
    count = 0
    for i in kata2:
        if i in vokal:
            continue
        count += 1
    list_kata.append(count)
    return list_kata

print(jumlahHurufVokal('Surakarta'))
print(jumlahHurufKonsonan('Surakarta'))