# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 11:00:28 2016

@author: Nathalia Morales
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 21:11:16 2016

@author: Nathalia Morales
"""

# import
import random as rn

# variables para el dibujo
s1=("""       _________________________
     __________________________|
     |  |           ||   """)
  
s8="""       _________________________
     __________________________|
     |  |           ||          
     |  |           ||           
     |  |           ||          
     |  |         ///||\\\  
     |  |         | ' ' |
     |  |         |__O__|
     |  |           ||    
     |  |         /     \  
     |  |        //|   |\\
     |  |        0 |___| 0
     |  |          | | |
     |  |          | | |
     |  |          | | |
     |  |          |_|_|
     |  |         C__|__D  """

s9="""       _________________________
     __________________________|
     |  |           ||          
     |  |           ||           OH NO!!!
     |  |           ||          HAZ PERDIDO!!!
     |  |         ///||\\\  
     |  |         | ' ' |
     |  |         |__O__|
     |  |           ||
     |  |       -----------
     |  |         /     \  
     |  |        //|   |\\
     |  |        0 |___| 0
     |  |          | | |
     |  |          | | |
     |  |          | | |
     |  |          |_|_|
     |  |         C__|__D  """

s2=("""       _________________________
     __________________________|
     |  |           ||          
     |  |           ||      """)


s3=("""       _________________________
     __________________________|
     |  |           ||          
     |  |           ||
     |  |           ||     """)
    
s4=("""       _________________________
     __________________________|
     |  |           ||          
     |  |           ||          
     |  |           ||          
     |  |         ///||\\\   """ )
    
s5=(""""       _________________________
     __________________________|
     |  |           ||          
     |  |           ||           
     |  |           ||          
     |  |         ///||\\\  
     |  |         | ' ' |
     |  |         |__O__| """)
    
s6=("""       _________________________
     __________________________|
     |  |           ||          
     |  |           ||           
     |  |           ||          
     |  |         ///||\\\  
     |  |         | ' ' |
     |  |         |__O__|
     |  |           ||""" )    
    

s7=("""       _________________________
     __________________________|
     |  |           ||          
     |  |           ||           
     |  |           ||          
     |  |         ///||\\\  
     |  |         | ' ' |
     |  |         |__O__|
     |  |           ||
     |  |         /     \  
     |  |        //|   |\\
     |  |        0 |___| 0 """ )    
    
##### LISTAS - LISTAS - LISTAS - LISTAS
deportes = ['basquetball','volleyball','tennis','futbol','natacion']
carros = ['ferrari','bugatti','kia','honda','toyota']
ropa = ['gap','gucci','channel','zarah','guess']
nombres = ['pedro','maria','javier','nicole','adriana']
comida = ['brownies','tortilla','pan','sandwich','frijol']
 
#### Menu - Menu - Menu - Menu - Menu - Menu
def m_y_s(): #menu y seleccion de la palabra
    print  ('Dentro de las categorias disponibles estan las siguientes, por favor elegir una categoria dentro del menu para jugar ahorcado \n'
    '.\n'
    'Las categorias disponibles son: \n'
        '1. Tipos de deportes \n'
        '2. Marcas de carro\n'
        '3. Marcas de ropa \n'
        '4. Nombres \n'
        '5. Comida \n'
        '6. Salir \n')
    num = int(input('Ingrese un numero para poder escoger una categoria: '))
    n = 0
    while n == 0:
        if num != 6 and num > 0:
            if num == 1: # ps - palabra seleccionada
                ps = (rn.choice(deportes)) #rn siendo random toma una palabra aleatoria de la lista seleccionada
                n =1
            elif num == 2:
                ps = (rn.choice(carros))
                n = 1
            elif num == 3:
                ps = (rn.choice(ropa))
                n = 1
            elif num == 4:
                ps = (rn.choice(nombres))
                n = 1
            elif num == 5:
                ps = (rn.choice(comida))
                n = 1
        else:
            continue
    return ps

## Crear lista con guiones bajos para reemplazar los valores
def c_l_v(lenpalabra):
     s2 = ['_'] * lenpalabra
     return s2

###  Letra de ingreso del usuario - letra ingresada
def li():
    letra = str(input("Ingrese la letra para adivinar la palabra, recuerde ingresarlo entre dos '', ejemplo 'a': "))
    return letra
    
#### Dibujo

def dbs(ar):
    if ar == 8:
        print s1
    if ar == 7:
        print s2
    if ar == 6:
        print s3
    if ar == 5:
        print s4
    if ar == 4:
        print s5
    if ar == 3:
        print s6
    if ar == 2:
        print s7                
    if ar == 1:
        print s8
    if ar == 0:
        print s9

# variables dentro del juego
ing = """

Instrucciones generales:
    Por favor no introduzca ningun simbolo,
    Solamente letras UNA a la vez
    Todas las letras deben ser en minuscula
    La letra tiene que ir entre dos comillas: ''
    """    
nott = ["+/ 1234567890*-_?.,"]
bnvd = ("""
╲╭━━━━╮╲╲╭━━━━━━━━╮
╲┃╭╮╭╮┃╲╲┃..Bienvenido!
┗┫┏━━┓┣┛╲╰┳╮ .....┃
╲┃╰━━╯┃━━━╯╰━━━━━━╯
╲╰┳━━┳╯╲╲╲╲╲╲╲
\n ¸,ø¤º°`°º¤ø,¸¸,ø¤º° Listo para Hang-Man? °º¤ø,¸¸,ø¤º°`°º¤ø,¸ 

                ▀▄▀▄▀▄    Tu palabra es    ▄▀▄▀▄▀ 
                                                                   """)
pdd = ("""Lo siento, has perdido...
░░▄▀░░░░░░░░░░░░░░░▀▀▄▄░░░░░ 
░░▄▀░░░░░░░░░░░░░░░░░░░░▀▄░░░ 
░▄▀░░░░░░░░░░░░░░░░░░░░░░░█░░ 
░█░░░░░░░░░░░░░░░░░░░░░░░░░█░ 
▐░░░░░░░░░░░░░░░░░░░░░░░░░░░█ 
█░░░░▀▀▄▄▄▄░░░▄▌░░░░░░░░░░░░▐ 
▌░░░░░▌░░▀▀█▀▀░░░▄▄░░░░░░░▌░▐ 
▌░░░░░░▀▀▀▀░░░░░░▌░▀██▄▄▄▀░░▐ 
▌░░░░░░░░░░░░░░░░░▀▄▄▄▄▀░░░▄▌ 
▐░░░░▐░░░░░░░░░░░░░░░░░░░░▄▀░ 
░█░░░▌░░▌▀▀▀▄▄▄▄░░░░░░░░░▄▀░░ 
░░█░░▀░░░░░░░░░░▀▌░░▌░░░█░░░░ 
░░░▀▄░░░░░░░░░░░░░▄▀░░▄▀░░░░░ 
░░░░░▀▄▄▄░░░░░░░░░▄▄▀▀░░░░░░░ 
░░░░░░░░▐▌▀▀▀▀▀▀▀▀░░░░░░░░░░░ 
░░░░░░░░█░░░░░░░░░░░░░░░░░░░░ """)
ul = ("\n ERROR, Solo puedes ingresar UNA letra..")
np = ("\n (-_-) Esa letra no esta permitida (-_-) ")
alu = ("\n °·.¸.·°¯°·.¸.·°¯°·.¸.-> Ya usaste esa letra <-.¸.·°¯°·.¸.·°¯°·.¸.·° ")
sps = ("""
        
                            . \n""")
bnn = """
╔══╗╔╗╔╗╔╗╔══╗╔══╗╔══╗╔╗╔╗╔══╗
║╔╗║║╚╝╚╝║║║═╣║══╣║╔╗║║╚╝║║║═╣
║╔╗║╚╗╔╗╔╝║║═╣╠══║║╚╝║║║║║║║═╣
╚╝╚╝─╚╝╚╝─╚══╝╚══╝╚══╝╚╩╩╝╚══╝
"""
bni = """
░░█▀░░░░░░░░░░░▀▀███████░░░░ 
░░█▌░░░░░░░░░░░░░░░▀██████░░░ 
░█▌░░░░░░░░░░░░░░░░███████▌░░ 
░█░░░░░░░░░░░░░░░░░████████░░ 
▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ 
░▌▄███▌░░░░▀████▄░░░░▀████▌░░ 
▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ 
▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ 
▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ 
▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ 
░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ 
░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ 
░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ 
░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ 
░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ 
░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ 
░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ 
░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ 
░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ 
▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ 
░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ 
░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ 
░░▄▌████████▄▄▄███████▌░░░░░▄ 
░▄▀░██████████████████▌▀▄░░░░ 
▀░░░█████▀▀░░░▀███████░░░▀▄░░ 
░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ 
░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ 
░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ 
░╔╗║░╔═╗░═╦═░░░░░╔╗░░╔═╗░╦═╗░ 
░║║║░║░║░░║░░░░░░╠╩╗░╠═╣░║░║░ 
░║╚╝░╚═╝░░║░░░░░░╚═╝░║░║░╩═╝░

──────────────╔╗───────╔╗╔╗────╔═╗
╔═╦═╦═╦╦═╦╦╦═╗║╚╦╦╦╗╔═╗║╚╬╬═╦═╦╣═╣
║═╣╬║║║║╬║╔╣╬╚╣╔╣║║╚╣╬╚╣╔╣║╬║║║╠═║
╚═╩═╩╩═╬╗╠╝╚══╩═╩═╩═╩══╩═╩╩═╩╩═╩═╝
───────╚═╝
"""
gb = ("""\n ★·.·´¯`·.·★·.·´¯`·.·★    ★·.·´¯`·.·★·.·´¯`·.·★    ★·.·´¯`·.·★·.·´¯`·.·★""")
gby = ("""๑۞๑,¸¸,ø¤º°`°๑۩    Gracias por jugar     ๑۩ ,¸¸,ø¤º°`°๑۞๑""")
#valor de verdad
yes = 1

while yes == 1:
    ps  = m_y_s()
    lps = len(ps)
    bksp = c_l_v(lps)
    print bnvd
    print bksp
    print ing
    print"\n La palabra seleccionada tiene %d letras en total."%lps 
    l_b = ""
    l_2 = ""
    espacios = []
    a = len(l_b)
    c = 9 #chances que tiene para ganar, oportunidades de fallo
    while True:
        word = ''.join(bksp)
        if  ps == word: 
            print("Has Ganado! Felicitaciones! La palabra a adivinar era: %s."%ps)
            print sps
            print bni
            ans = input("Ingrese enter para volver a jugar, para salir ingrese 'salir' entre comillas para salir del juego:  ")            
            if ans == 'salir':
                print gby
                False
                yes = 0
            if ans == 'ok':
                break
            else:
                break
        if c == 0:
            print pdd
            print ("La palabra que no lograste adivinar era: %s"%ps)
            ans = input("Ingrese 'ok' para volver a jugar, para salir ingrese 'salir' entre comillas para salir del juego:  ")            
            print sps            
            if ans == 'salir':
                print gby 
                False
                yes = 0
            if ans == 'ok':
                break
            else:
                break
       
        letra=li()
        
        if 1<len(letra):
            print ul
            continue
        if letra in nott:
            print np
            continue
        if letra in l_b or letra in l_2:
            print alu
            continue
        if letra in ps and not letra in l_b:
            print sps
            print("La Letra %s, aparece en %d de los espacios de la palabra."%(letra,ps.count(letra)))
            for cn, i in enumerate(ps):
                if 2 <=ps.count(i) and letra==i:
                    l_b += letra
                    a += ps.count(i)
                    if bksp[cn] == ("_"):
                        bksp[cn] = letra
                        print ("         En el espacio %d"%(cn+1))
                        print sps
                if ps.count(i)==1 and letra==i:
                    l_b+=letra
                    a+=ps.count(i)
                    if bksp[cn] == "_":
                        bksp[cn] = letra
                        print ("         En el espacio %d"%(cn+1))
                        print sps
            print("\n Palabra:",' '.join(bksp))
            print bnn
        else:
            l_2 += letra
            c -= 1
            print dbs(c)
            print("\n La Letra %s, NO aparece dentro de la palabra SORRY."%(letra))
            print '\n Te quedan las siguientes oportunidades:     %d'% c
            print '\n Palabra:         %s'% bksp
        try:
            print gb
        except SyntaxError:
            pass
        v = raw_input("Ingrese enter para continuar")
        continue
        