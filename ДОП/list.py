from pymystem3.mystem import Mystem
import re


def mystem(text):
    obj = Mystem()
    result_list = Mystem.analyze(obj, text)
    return result_list


def t_text(word, gram, lex):
    text = ''
    ...
    return text
    
    
def long(text):
    word_list = mystem_text(text)
    translited_list = []
    for word in word_list:
        if 'analysis' in word:
            t = t_text(word['text'], word['analysis']['gr'], word['analysis']['lex'])
            ...
        else:
            t = word['text']
        text_list.append(t)
    text = ''.join(translited_list)
    return text
