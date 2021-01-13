from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')
text="""The New York Times is an American daily newspaper based in New York City with a worldwide readership. Founded in 1851, the Times has since won 130 Pulitzer Prizes, and has long been regarded within the industry as a national "newspaper of record". It is ranked 18th in the world by circulation and 3rd in the U.S"""
tokenized_text=sent_tokenize(text)
print(tokenized_text)
