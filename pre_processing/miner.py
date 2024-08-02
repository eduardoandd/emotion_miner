import unicodedata
import nltk

base=[
    ('eu sou admirada por muitos','alegria'),
    ('me sinto completamente amado','alegria'),
    ('amar é maravilhoso','alegria'),
    ('estou me sentindo muito animado novamente', 'alegria'),
    ('eu estou muito bem hoje','alegria'),
    ('que belo dia para dirigir um carro novo','alegria'),
    ('o dia está muito bonito','alegria'),
    ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
    ('o amor é lindo','alegria'),
    ('nossa amizade e amor vai durar para sempre', 'alegria'),
    ('estou amedrontado','medo'),
    ('ele está me ameacando a dias','medo'),
    ('este lugar é apavorante', 'medo'),
    ('isso me deixa apavorada', 'medo'),
    ('se perdemos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
   ('tome cuidado com o lobisomen','medo'),
   ('se eles descobrirem estamos encrencados','medo'),
   ('estou tremenedo de medo', 'medo'),
   ('eu tenho muito medo dele', 'medo'),
   ('estou com medo do resultado dos meus testes', 'medo')
]
def remover_acentos(texto):
    texto_normalizado=unicodedata.normalize('NFD', texto)

    texto_sem_acentos=''.join(char for char in texto_normalizado if unicodedata.category(char) !='Mn')

    return texto_sem_acentos
base=[(remover_acentos(texto),emocao) for texto,emocao in base]

# ====================== TRATAMENTO DE STOP WORDS ======================
stop_word_nltk=nltk.corpus.stopwords.words('portuguese')
def remove_stop_words(texto):
    frases=[]

    for palavra,emocao in texto:

        sem_stop_words= [p for p in palavra.split() if not p in stop_word_nltk]
        frases.append((sem_stop_words,emocao))

    return frases
remove_stop_words(base)

# ====================== EXTRAÇÃO DE RADICAL DAS PALAVRAS (STEMMING) ======================
def aplica_stremmer(texto):
    stemmer=nltk.stem.RSLPStemmer()
    frases_stemming=[]

    for (palavra,emocao) in texto:
        com_stemming=[str(stemmer.stem(p)) for p in palavra.split() if p not in stop_word_nltk]
        frases_stemming.append((com_stemming,emocao))
    return frases_stemming
frases_com_stemming=aplica_stremmer(base)

# ====================== LISTAGEM DAS PALAVRAS COM STEMMING ======================
def listagem_palavras_st(palavras):
    lista_palavras=[]
    for (palavra,emocao) in palavras:
        lista_palavras.extend(palavra)
    return lista_palavras
palavras=listagem_palavras_st(frases_com_stemming)

# ====================== EXTRAÇÃO DE PALAVRAS ÚNICAS ======================
def busca_freq(palavras):
    palavras=nltk.FreqDist(palavras)
    return palavras
frequencia=busca_freq(palavras)

def busca_palavra_unica(frequencia):
    palavras_unicas=frequencia.keys()
    return palavras_unicas
palavras_unicas=busca_palavra_unica(frequencia)

def extrator_palavras(palavras):
    doc=set(palavras)
    caracteristicas={}  
    for palavra in palavras_unicas:
        caracteristicas['%s' % palavra] = (palavra in doc)
    return caracteristicas
caracteristicas_frase=extrator_palavras(['am','nov','dia'])

basecompleta=nltk.classify.apply_features(extrator_palavras,frases_com_stemming)