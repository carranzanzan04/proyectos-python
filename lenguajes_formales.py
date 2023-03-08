# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 02:06:16 2023

@author: SARA CARRANZA
""" 
import random
from potencia import pw,concatenadora
class Alphabeth():
    simbology=""
    NEUTRAL_ELEMENT="#"
    
    def __init__(self,simbology):
         self.simbology=simbology  
         
         
    def union (self,alphabet):
        lista= self.simbology.split(",") 
        lista2=alphabet.simbology.split(",")
        return list(set(lista) | set(lista2))
    
    def intersection(self,alphabet):
        lista=self.simbology.split(",")
        lista2=alphabet.simbology.split(",")
        return list(set(lista) & set(lista2))
    
    def diference(self, alphabet):
       lista=self.simbology.split(",")
       lista2=alphabet.simbology.split(",")
       return set(lista)-set(lista2)
       return lista
    def start_loock(self,limit):
        lista=[]
        if limit <=6:
            lista.append(self.simbology.split(","))
            for i in range(limit):
                   print(i)
                   if i!=1:
                       lista.append(pw(self.simbology,i+1))
            lista.append("#")
        return lista
class language (Alphabeth) :  
    lista_palabras=[]
    
    def __init__(self, simbology):
        self.simbology=simbology
        
    def generate_words(self,n):
        lista=[]
        lista=self.start_loock(self.simbology,5)
        lista=random.SystemRandom().sample(lista, n)
        return lista
a1=Alphabeth("a,c,m")
a2=Alphabeth("c,g,m")
print(a1.start_loock(4))