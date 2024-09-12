import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.data import find
#Enshure the necessary files are downloaded
def download_nltk_data():
    try:
        find('corpora/stopwords.zip')
        find('tokenizers/punkt.zip')
    except LookupError:
        nltk.download('stopwords')
        nltk.download('punkt')
#Tokenization
def tokenize(text):
    return word_tokenize(text)
#Filteration
def filter_text(tokens):
    return [re.sub(r'[^a-zA-Z0-9]', '', token) for token in tokens if token]
#Validation
def validate_script(tokens):
    return [token for token in tokens if re.match(r'^[a-zA-Z]+$', token)]
#Stop Removal words
def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token.lower() not in stop_words]
#Stemming
def stem_tokens(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]
#Main processing function
def preprocess_text(text):
    #download data
    download_nltk_data()
    #tokenisation
    tokens = tokenize(text)
    #filteration
    tokens = filter_text(tokens)
    #script validation
    tokens = validate_script(tokens)
    #stop words removal
    tokens = remove_stop_words(tokens)
    #stemming
    tokens = stem_tokens(tokens)
    return tokens
#Example Usage
if __name__ == "__main__":
    sample_text = "Neural Language Processing (NLP) is a field of artificial intelligence that focuses on Artificial intelligence"
   
    processed_tokens = preprocess_text(sample_text)
    print("Processed Tokens:", processed_tokens)
