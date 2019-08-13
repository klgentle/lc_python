import pandas as pd
import re

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
lemma = WordNetLemmatizer()
# lda model
import gensim
from gensim import corpora
 
print("reading file...")
rawdata = pd.read_csv('disney.csv',header=None, encoding='utf8') # no header provided


# def removePrefix(_x): # extract the string
#     x = re.sub(r"[\\]+", "", _x)
#     return re.match('^b[\'\"](.+)[\'\"]$', str(x)).group(1)

def removePrefix(_x): # extract the string 
	try:
		return _x[2:-1]
	except:
		print(_x) 
        

cols = rawdata.shape[1]
rows = rawdata.shape[0]
for i in range(0, cols): # remove nan columns
#     print(rawdata[i].isna().sum())
    if (rawdata[i].isna().sum() == rows):
        rawdata=rawdata.drop(columns=(i))

rawdata = rawdata.applymap(removePrefix)
rawdata = rawdata.rename(columns={0:'author', 1:'text'})
rawtext = rawdata['text'].tolist()


def cleansymbols(x):
    cleanx = re.sub('(http(s)?://)?[0-9A-Za-z]+\.[0-9A-Za-z]+[0-9A-Za-z/.-]+', '', x) # remove hyperlink
    cleanx = re.sub("(\[[0-9]\])|[\"/–,;\\:.©£•!\?\-\+~@#›￥%……&*\(\)\|“>”/\']|(\\n)", " ", cleanx) # remove punctuation
    return cleanx


# sentence slice
print("sentence tokenize...")

sentences = []
for t in rawtext:
    sentences.extend(sent_tokenize(t))
# clean data
for i,sen in enumerate(sentences):
    try:
        sentences[i] = cleansymbols(sen)
    except:
        print(sentences[i])
        
# tokenize
print("word tokenize...")

doc_tokens = [word_tokenize(sen) for sen in sentences]

# remove stop words and short words
print("cleaning data...")
custom_stopwors = ['the']
doc_tokens_removed = []
for j, token_li in enumerate(doc_tokens):
    new_token_li = []
    for i, token in enumerate(token_li):
        lt = token.lower()
        if not(lt in stopwords.words('english') or lt in custom_stopwors or len(lt)<3):
            lemma_token = lemma.lemmatize(lt) # lemmatize
            if (len(lemma_token)>=3):
                new_token_li.append(lemma_token)
    doc_tokens_removed.append(new_token_li)


dictionary = corpora.Dictionary(doc_tokens_removed)

# transform into dt-matrix
dtmat = [dictionary.doc2bow(doc) for doc in doc_tokens_removed]
Lda = gensim.models.ldamodel.LdaModel

print("modeling...")


# multiple sets of params
# for i in range(3,8):
#     print('-------------',"num_topics = ", i,'--------------------')
#     ldamodel = Lda(dtmat, num_topics=i, id2word = dictionary, passes=50)
#     for j in range(3, 7):
#         print("num_words = ", j)
#         print(ldamodel.show_topics(num_words=j) )
#         print('---')

# single output
lda_passes = 50 
lda_num_topics = 4
ldamodel = Lda(dtmat, num_topics=lda_num_topics, id2word = dictionary, passes=lda_passes)
print(ldamodel.show_topics())