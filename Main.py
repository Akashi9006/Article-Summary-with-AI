import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# Download necessary NLTK data

nltk.download('punkt')

url = 'https://www.bbc.co.uk/news/live/c5yep0l5545t'

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Author: {article.authors}')
print(f'Publish date: {article.publish_date}')
print(f'Summary: {article.summary}')