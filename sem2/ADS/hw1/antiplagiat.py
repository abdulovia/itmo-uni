import wikipedia
import docx
import string

language = "ru"
wikipedia.set_lang(language)
corp = wikipedia.page("Корпоративные ценности")

# print(corp.summary)
wiki_contents = [word.lower().strip(string.punctuation) for word in corp.content.split()]
# print(wiki_contents)

doc_contents = []
doc = docx.Document("Корпоративные ценности.docx")
# number_of_symbols = 0 # количество символов в реферате
for docpar in doc.paragraphs:
    # number_of_symbols += len(docpar.text)
    doc_contents += [word.lower().strip(string.punctuation) for word in docpar.text.split()]

# print(doc_contents)

# Используя алгоритм Рабина-Карпа
X = 37 # ближайшее простое к размеру алфавита
MOD = int(10**9)+7
def hash(s):
    '''
    Функция возвращает hash (число) от произвольной строки
    :param s:
    :return H:
    '''
    H = 0
    M = len(s)
    for i in range(len(s)):
        c = ord(s[i])-ord('0') # значение от 0 до 9 – порядковый номер символа
        H = (H + (c*X**(M-i)) % MOD) % MOD
    return H


plagiat_words = 0
wiki_contents_hash = [hash(word) for word in wiki_contents]
doc_contents_hash = [hash(word) for word in doc_contents]
for i in range(len(doc_contents_hash)):
    doc_word_hash = doc_contents_hash[i]
    for j in range(len(wiki_contents_hash)):
        wiki_word_hash = wiki_contents_hash[j]
        if doc_word_hash == wiki_word_hash and doc_contents[i:i+3] == wiki_contents[j:j+3]:
            plagiat_words += 3
            # print(doc_contents[i:i+3])
plagiat_percentage = int(plagiat_words / len(doc_contents) * 100)
print(f'Количество плагиата в % от общего количества слов в реферате: {plagiat_percentage}%')