import lyricsgenius as lg
import wordCount as wc
import numpy as np
import plotly.graph_objects as go

if __name__ == '__main__':

    # setup for lyricsgenius
    genius = lg.Genius("kP20XYcDVeFwyQWN3o0BASGUoxYQFaTY5_0SNsBrkwSGzkqY8zU2_yU1w5TNv5qm")
    # this sets data to a discography holding 1 album & 1 song, confusingly
    data = genius.search_song("Lost in Yesterday", "Tame Impala")
    # this resets data to the actual lyrics of the songs in the pseudo-discography
    data = data.lyrics
    # I made this program weirdly work only for songs I'm going to come back
    # so ideally the user will be able to choose any number of songs to compare

    counts = dict()
    wc.word_count(data, counts)

    counts = sorted(counts.items(), key=lambda item: item[1])

    # print the top 10 words in the song
    top10 = counts[-10:]
    for word, count in top10:
        print(word + ": " + str(count))

    fig = go.Figure(data=go.Bar(y=[x[1] for x in top10], x=[x[0] for x in top10]))
    fig.show()
