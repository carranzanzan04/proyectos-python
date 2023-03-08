# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
lista1=[]
lista2=[]
lista3=[]
control1=False 
control2=False
contador1=0
contador2=0
contador3=0
contador4=0
r=0
r2=0

def concatenadora(string,n):
    global lista1,lista2,lista3,control1,contador1,contador2,r
    lista1=string.split(",")
    lista2=string.split(",")
    if control1== False:
       r=len(lista1)
       n=r
       n=n*n    
       control1=True
     
    if n>=1:
        if contador1==r:
            contador1=0
            contador2+=1
        lista3.append(lista1[contador2]+lista2[contador1])
        contador1+=1
        return concatenadora(string, n-1)
    return lista3

def potencia(string,p):
    global lista3,lista1,control2,contador3,contador4,r2,control2
    if control2==False:
        lista1=lista3
        r2=len(lista3)
        lista3=[]
        p=r2*len(lista2)
        control2=True
        
    if p>0:
        if contador4==(len(lista2)):
            contador4=0
            contador3+=1
        lista3.append(lista1[contador3-r2]+lista2[contador4])
        contador4+=1
        return potencia(string,p-1)
    return lista3
    
def pw(string,k):
        global control2
        if k==2 and control1==False:
           concatenadora(string, (len(string)-1)/2)
        if k>2:
            if control1==False:
                concatenadora(string, (len(string)-1)/2)
            potencia(string,len(string)-1)
            control2=False
            return pw(string,k-1)
        return lista3
          

    
#print(pw("a,b,c", 6))
