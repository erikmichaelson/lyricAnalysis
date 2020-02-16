import Tkinter, tkFileDialog
import wordCount as wc
import numpy as np

# setup for the file selection box
root = Tkinter.Tk()
root.withdraw()

if __name__ == '__main__':

    # prompt the user to choose a text file of
    file_path = tkFileDialog.askopenfilename()
    with open(file_path, 'r') as file:
        data = file.read()#.replace('\n', '')

    counts = dict()
    wc.word_count(data, counts)

    counts = sorted(counts.items(), key=lambda item: item[1])

    # print the top 10 words in the song
    top10 = counts[-10:]
    for word, count in top10:
        print(word + ": " + str(count))
