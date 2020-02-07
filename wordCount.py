import Tkinter, tkFileDialog

# setup for the file selection box
root = Tkinter.Tk()
root.withdraw()

#
# This code is an example ripped from w3resource, so props to them
# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php
#
# I'm going to take it and pass it the whole file which is about 50% of the work for this part
#
def word_count(str, counts):
    words = str.split()

    for word in words:
        word = word.lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
# end w3resource code

if __name__ == '__main__':

    # prompt the user to choose a text file of
    file_path = tkFileDialog.askopenfilename()
    with open(file_path, 'r') as file:
        data = file.read()#.replace('\n', '')

    counts = dict()
    word_count(data, counts)

    counts = sorted(counts.items(), key=lambda item: item[1])
