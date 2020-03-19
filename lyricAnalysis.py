from tkinter import filedialog
from tkinter import *
import wordCount as wc
import numpy as np
import plotly.graph_objects as go

# setup for the file selection box
root = Tk()
root.withdraw()

if __name__ == '__main__':

    # prompt the user to choose a text file of
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        data = file.read()

    counts = dict()
    wc.word_count(data, counts)

    counts = sorted(counts.items(), key=lambda item: item[1])

    # print the top 10 words in the song
    top10 = counts[-10:]
    for word, count in top10:
        print(word + ": " + str(count))

    fig = go.Figure(data=go.Bar(y=[x[1] for x in top10], x=[x[0] for x in top10]))
    fig.show()
