#!/usr/bin/python3
"""
This is the "5-text_indentation" module.

The example module supplies one function, text_indentation().
"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after each of
        these characters: ., ? and :
        Args:
            text (string): Paragraph.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for line in list_text:
            line = line.strip(" ")
            s = line + d if s is "" else s + "\n\n" + line + d

    print(s[:-3], end="")
