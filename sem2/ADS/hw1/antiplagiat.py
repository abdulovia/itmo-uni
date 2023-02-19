import wikipedia
import docx

language = "ru"
wikipedia.set_lang(language)
corp = wikipedia.page("Корпоративные ценности")

# print(corp.summary)
wiki_contents = corp.content

doc_contents = ""
doc = docx.Document("Корпоративные ценности.docx")
for docpar in doc.paragraphs:
    doc_contents += docpar.text



