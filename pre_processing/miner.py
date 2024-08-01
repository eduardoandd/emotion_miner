import unicodedata
import nltk

# ====================== TRATAMENTO DE STOP WORDS ======================
def remover_acentos(texto):
    texto_normalizado=unicodedata.normalize('NFD', texto)

    texto_sem_acentos=''.join(char for char in texto_normalizado if unicodedata.category(char) !='Mn')

    return texto_sem_acentos

def remove_stop_words(texto):
    frases=[]

    for palavra,emocao in texto:

        sem_stop_words= [p for p in palavra.split() if not p in stop_word_nltk]
        frases.append((sem_stop_words,emocao))

    return frases

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
base=[(remover_acentos(texto),emocao) for texto,emocao in base]

stop_words = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']
stop_word_nltk=nltk.corpus.stopwords.words('portuguese')

remove_stop_words(base)

# ====================== EXTRAÇÃO DE RADICAL DAS PALAVRAS (STEMMING) ======================

def aplica_stremmer(texto):
    stemmer=nltk.stem.RSLPStemmer()
    frases_stemming=[]

    for (palavra,emocao) in texto:
        com_stemming=[str(stemmer.stem(p)) for p in palavra.split() if p not in stop_word_nltk]
        frases_stemming.append((com_stemming,emocao))
    return frases_stemming

frases_com_stemmer=aplica_stremmer(base)