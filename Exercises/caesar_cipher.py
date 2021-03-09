#PROGRAMA BÁSICO: NOS TIRARÁ ERROR DE ÍNDICE CUANDO SUPEREMOS EL ALFABETO COMPLETO

#alphabet='abcdefghijklmnopqrstuvwxyz'
#input_text=str(input("Ingrese su texto aquí: "))

#output=''
#for char in input_text:
#    alpha_index=alphabet.find(char)
#    output=output+alphabet[alpha_index+3]
#print("Su mensaje encriptado es: ", output)

#Funcion:


alphabet='abcdefghijklmnopqrstuvwxyz'

def shift_amount(i):
    '''Will determine the shift, taking into account the lenght of the alphabet. Takes integer'''
    return i%26

def encrypt(text,required_shift):
    out_string=''
    text = text.lower()
    for char in text:
        if char not in alphabet:
            out_string=out_string+char
        else: 
            alpha_index=alphabet.find(char)
            out_string = out_string + alphabet[shift_amount(alpha_index+required_shift)]
    return out_string

 
print(encrypt("que tal",5))


x='Holaaaa'
encrypt_x=encrypt(x,5)
print("El mensaje encriptado es: ", encrypt_x)