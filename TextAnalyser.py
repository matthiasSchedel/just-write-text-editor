from collections import defaultdict
import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
import tkFont


def count_monkeypatch(self, index1, index2, *args):
            args = [self._w, "count"] + ["-" + arg for arg in args] + [index1, index2]

            result = self.tk.call(*args)
            return result

Text.count = count_monkeypatch
ScrolledText.count = count_monkeypatch


class TextAnalyser():
    def __init__(self,input_text):
                self.text = input_text
    def set_text(input_text):
                text = text
    def get_line_count():
                words_last_file = 0
      
    """
      with open(file,'r') as file_stream:
        for line in file_stream:
          words_in_line = line.split()
          self.total_words += len(words_in_line)
          for word in words_in_line:
            self.words[word] += 1
            words_last_file += 1
                #return line count of given text
    """



