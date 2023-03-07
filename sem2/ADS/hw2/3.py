from random import randint, uniform
def hash_multi(table, key, const, text):
    result = ''
    n = key * const
    for t in text:
        hash_key = int(len(table.items()) * n)
        if hash_key not in table.keys():
            table[hash_key] = []
        table[hash_key].append(t)
        result += str(hash_key)
    return result

def dehash_multi(table, hash_text):
    result = ''
    i, curr_i = -1, 0
    while i < len(hash_text):
        i += 1
        if i == curr_i:
            if int(hash_text[i]) in table.keys() and table[int(hash_text[i])]:
                result += table[int(hash_text[i])].pop(0)
                curr_i = i
        else:
            if int(hash_text[curr_i:i]) in table.keys() and table[int(hash_text[curr_i:i])]:
                result += table[int(hash_text[curr_i:i])].pop(0)
                curr_i = i
    return result


s = input('Введите текст, который нужно хэшировать: ')
hash_table = {}
k, c = randint(1, 50), uniform(0, 1)
print('Ключ:', str(k), 'Константа:', str(c))
hash_s = hash_multi(hash_table, k, c, s)
print('Хэшированный текст (умножение):', hash_s)
print('Исходный текст (умножение):', dehash_multi(hash_table, hash_s))