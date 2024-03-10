from textblob import TextBlob
from newspaper import Article

with open('mytext.txt' , 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)

# url = 'https://en.wikipedia.org/wiki/Mathematics'
# The download() method is called to fetch the HTML content of the article from the given URL.
# The parse() method is then used to extract relevant information from the downloaded HTML, including the article's text.
# article = Article(url)
# article.download()
# article.parse()
# article.nlp()

# text = article.text
# text = article.summary
# print(text)

# blob = TextBlob(text)
# sentiment = blob.sentiment.polarity  # -1 to 1
# print(sentiment)

