# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:23:11 2022

@author: yildirim.akbal
"""


def preprocess(string:str) -> str:
    str_ = string
    while True:
        try:
            beg = str_.index("<")
            end = str_.index(">")
            str_ = str_.replace(str_[beg:end+1], "")
        except:
            print("we are done")
            break
    return str_
