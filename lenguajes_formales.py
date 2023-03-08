# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 02:06:16 2023

@author: SARA CARRANZA
""" 
import random
from potencia import pw
class Alphabeth():
    simbology=""
    NEUTRAL_ELEMENT="#"
    
    def __init__(self,simbology):
         self.simbology=simbology    
    def union (self,alphabet):
        lista= self.simbology.split(",") + alphabet.simbology.split(",")
        return lista
    def intersection(self,alphabet):
        lista=self.simbology.split(",")+alphabet.simbology.split(",")
        return lista
    def diference(self, alphabet):
       lista=self.simbology.split(",")-alphabet.simbology.split(",")
       return lista
    def start_loock(string,limit):
        lista=[]
        if limit <=6:  
           lista.append(pw(string,limit))
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