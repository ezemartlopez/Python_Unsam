#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:56:24 2020

@author: mcerdeiro
"""

# generala.py
# ejercicio 4.7
import random

def es_generala(tirada):
    return len(set(tirada)) == 1

def tirar(n):
    tirada=[]
    for i in range(n):
        tirada.append(random.randint(1,6)) 
    return tirada

def repes(tirada):
    lista = []
    for i in range(1,7):
        lista.append(tirada.count(i))
    for j, e in enumerate(lista):
        if e == max(lista):
            res = [j+1]*e
    return res        

def mejorar_tirada(tirada):
    rep = repes(tirada)
    l = tirar(5-len(rep))
    t = rep + l
    return t
        
def jugar_generala():
    t = tirar(5)
    t = mejorar_tirada(t)
    t = mejorar_tirada(t)
    return es_generala(t)

#%%
N = 100000
G = sum([jugar_generala() for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} pude hacer generala.')
print(f'Podemos estimar la probabilidad de hacer generala mediante {prob:.6f}.')   