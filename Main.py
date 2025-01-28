import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def Summarise():

    #Summarising Logics
    url = URLText.get('1.0',"end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    Publish.config(state='normal')
    Summary.config(state='normal')
    Sentiment.config(state='normal')

    title.delete('1.0', tk.END)
    title.insert('1.0', article.title)

    author.delete('1.0', tk.END)
    author.insert('1.0', article.authors)

    Publish.delete('1.0', tk.END)
    Publish.insert('1.0', article.publish_date)

    Summary.delete('1.0', tk.END)
    Summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    Sentiment.delete('1.0', tk.END)
    Sentiment.insert('1.0' ,f'Polarity: {analysis.polarity} ,Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    Publish.config(state='disabled')
    Summary.config(state='disabled')
    Sentiment.config(state='disabled')


#gui creation
root = tk.Tk()
root.title("News Summariser")
root.geometry('1200x600')

titlelabel = tk.Label(root,text="Title")
titlelabel.pack()

title = tk.Text(root,height=1,width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

authorlabel = tk.Label(root,text="Author")
authorlabel.pack()

author = tk.Text(root,height=1,width=140)
author.config(state='disabled', bg='#dddddd')
authorlabel.pack()

PDlabel = tk.Label(root,text="Publish Date")
PDlabel.pack()

Publish = tk.Text(root,height=1,width=140)
Publish.config(state='disabled', bg='#dddddd')
Publish.pack()

Summarylabel = tk.Label(root,text="Summary")
Summarylabel.pack()

Summary = tk.Text(root,height=20,width=140)
Summary.config(state='disabled', bg='#dddddd')
Summary.pack()

Sentimentlabel = tk.Label(root,text="Sentiment")
Sentimentlabel.pack()

Sentiment = tk.Text(root,height=1,width=140)
Sentiment.config(state='disabled', bg='#dddddd')
Sentiment.pack()

URLlabel = tk.Label(root,text="URL")
URLlabel.pack()
URLText = tk.Text(root,height=1,width=140)
URLText.pack()

btn = tk.Button(root, text="Summarise",command = Summarise)
btn.pack()

root.mainloop()