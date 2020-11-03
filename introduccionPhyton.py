
print ("Ola Phyton")

print ("Remato o programa")

'''
/*Exemplo de codigo java*/

int numero;
'''
# Comentario dunha liña en python
# Exemplo de declaración dunha variable en python
# O tipado en python é dinámico

numero = 1
print (type (numero))

print ("O tipo resultante entre un real e un enteiro é "+str (type(5.0/3)))

# Tipos básicos
# Números

enteiro = 2
enteiroLongo = 2
octal = 0o26
hex = 0x24A

comaFlotante = 15.09
notacionCientifica = 9.1e-3

print (type (comaFlotante))

complexos = 5 + 3j

print (complexos)
print (type (complexos))

#Cadeas
cadea = "Un texto calquera"
print(type (cadea))

booleano = True
print(type (booleano))

# + - * ** / // %

print (5//3)
print (5%3)

# Operadors a nivel de bit: & anb | or ^ xor ~ not << desprazamento a esquerda >> desprazamento a dereita
print (3 & 2)

print (3>>1)

# 00000011 >> 00000001

print (3<<1)

# 00000011 << 00000110

cadea = 'Texto con "comillas" dobres'
print(cadea)
cadea2 = "Texto multilinea \n mediante caracteres de escape"
cadea3 = """ E escribir texto de
        forma mais natural,
        e permite a documentación do código
        equivalente o comentario en Java /* */
        """
print (cadea2 + "\n" + cadea3)

print ("abe"*3)

# Operadores Booleanos and or not
print (True and False)

# == != < > <= >=

if booleano == False :
        print ("Boleando e falso")
        print ("Poño tantas instrucións")
        print ("como precise")

print ("Xa estou fora do bloque de código do if")
