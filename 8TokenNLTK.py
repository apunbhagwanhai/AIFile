print("EKANSH JAIN A2305218211 7CSE-4X")
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
text = "Tokenization is the process by which a large quantity of text is divided into smaller parts called tokens!."
print("\nOUTPUT OF SENETENCE TOKENIZER\n\n",sent_tokenize(text))
print("\nOUTPUT OF WORD TOKENIZER\n\n",word_tokenize(text))
print("\nOUTPUT OF Punctuation  TOKENIZER\n\n",WordPunctTokenizer().tokenize(text))
