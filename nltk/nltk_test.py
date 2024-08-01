import nltk
nltk.download()

texto='Eduardo is funny. Eduardo is a clown.'
texto.split(' ')

frases=nltk.tokenize.sent_tokenize(texto)

tokens=nltk.word_tokenize(texto)

classes=nltk.pos_tag(tokens)

entidades=nltk.chunk.ne_chunk(classes)