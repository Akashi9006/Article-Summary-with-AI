import tkinter as tk
import nltk
import textblob as TextBlob
import newsport as Article

# Download necessary NLTK data

url = 'https://www.bbc.co.uk/news/live/c5yep0l5545t'

article = Article(url)

article.download()

article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Author: {article.author}')
print(f'Publish date: {article.publish_date}')
print(f'Summary: {article.summary}')