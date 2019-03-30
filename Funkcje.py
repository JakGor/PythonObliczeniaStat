# -*- coding: utf-8 -*-
import sys

##################################
def koniec ():
    sys.exit()

###########################################
def is_number(a): #Obsługa wyjątków, czyli gdy ktos wprowadzi w ciąg znaków litery, dodatkowe przecinki lub spacje
    try:
        float(a)
        return True
    except ValueError:
        return False



