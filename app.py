#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv

print('##############################')
print('# CALCULO DE DPI / DISTÂNCIA #')
print('##############################')
print('')

prompt = "> Digite a distância (em centímetros) em que a imagem será vista: "
distance = input(prompt)


def calcDPI(distance):
    distance = int(distance) / 2.54
    ppi = 1/((distance * 0.000291) / 2)
    ppi = 'A DPI mínima para a arte é de: ' + str(int(ppi)) + str(" dpi")
    print(ppi)
    return


calcDPI(distance)
k = input()
