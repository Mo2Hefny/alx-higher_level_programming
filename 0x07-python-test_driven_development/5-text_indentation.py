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
    s = ""
    sub = ""
    for c in text:
        if c == ' ' and sub == "":
            continue
        sub = sub + c
        if c in ('.', '?', ':'):
          s = s + sub.strip() + "\n\n"
          sub = ""
    print((s+sub).strip(), end="")
