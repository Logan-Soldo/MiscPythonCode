###############################################################################
# Project #04 
# This program is used for encrypting and decrypting a string that is input
# The program first asks for a 'rotation' or 'N' as an integer for the cipher
#   Then prompts for an encryption, decryption, or quit
#      if 'e' input, encryption loop starts
#      if 'd' input, decryption loop starts
#      if 'q' input, program will quit
# Once an encryption or decryption is complete, the program will prompt for another
# encryption decryption or quit, the rotation remains the same.
# Encryption and Decryption loops call functions for calculations
###############################################################################
import math,string
PUNCTUATION = string.punctuation
ALPHA_NUM = string.ascii_lowercase + string.digits

def multiplicative_inverse(A,M):
    '''Return the multiplicative inverse for A given M.
       Find it by trying possibilities until one is found.'''
       
    for x in range(M):
        if (A*x)%M == 1:
            return x
  
def check_co_prime(num, M):
    '''Insert a doc string here.'''
    return math.gcd(num,M) == 1            # checking if numbers are co_prime
        
def get_smallest_co_prime(M):
    '''Insert a doc string here.'''
    for i in range(2,M):
        if check_co_prime(i,M):            # if check_co_prime is true, returns i.
            return i
   
def caesar_cipher_encryption(ch,N,alphabet):   #This is the encryption function    
    '''Insert a doc string here.'''
    M= len(alphabet)                       # finds length of alphabet depending on character
    x=alphabet.find(ch)                    # x is equal to the character's position in the alphabet  
    caesar_E=(int(x) + N) % M              # Caesar Encrypt formula
    return alphabet[caesar_E]

def caesar_cipher_decryption(ch,N,alphabet):
    '''Insert a doc string here.'''
    M=len(alphabet)                       # finds length of alphabet depending on character
    x=alphabet.find(ch)                   # x is equal to he character's position in the alphabet
    caesar_D=(int(x)-N) % M               # Caesar Decrypt formula
    return alphabet[caesar_D]  
        
def affine_cipher_encryption(ch,N,alphabet):   #This is the affine encryption function
    '''Insert a doc string here.'''
    M=len(alphabet)                       # finds length of alphabet depending on character
    A= get_smallest_co_prime(M)           # called in from get_smallest_co_prime    
    x=alphabet.find(ch)                   # x is equal to the character's position in the alphabet
    Affine_E=(A*int(x)+N)%M               # Affine Encrypt formula
    return alphabet[Affine_E]

def affine_cipher_decryption(ch,N,alphabet):   #This is the affine decryption function
    '''Insert a doc string here.'''
    M=len(alphabet)                       # finds length of alphabet depending on character
    A=get_smallest_co_prime(M)            # called in from get_smallest_co_prime
    A_inv=multiplicative_inverse(A,M)     # called in from multiplicative_inverse
    x=alphabet.find(ch)                   # x is equal to the character's position in the alphabet
    Affine_D= A_inv*(int(x)-N)%M          # Affine Decrypt formula 
    return alphabet[Affine_D]
    
def main():
    pass
    Input=''
    Encrypt_str=''
    Decrypt_str=''
    while Input == "q" or True:
        
        if Input== "q":
            break
        
        N=input("Input a rotation (int): ")   
        while Input=="q" or ' ' in Encrypt_str or ' ' in Decrypt_str or N.isdigit() :  
            N=int(N)
           
            if Input == "q":
                break
            
            Input= input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
        
            while Input != "q":                         # if the Input is not 'q' the program continues
                if Input== "e":                         # Input of 'e' will start the encryption loop
                    Encrypt_str=input("Input a string to encrypt: ")
                    Orig_Plaintext=Encrypt_str
                    Encrypt_str=Encrypt_str.lower()
                    if ' ' in Encrypt_str:              # if space is in input, the program will reprompt for a command.
                        print("Error with character: ")
                        print("Cannot encrypt this string.")
                        break
                    CipherText=''                       # Building cipher text
                    for ch in Encrypt_str:
                        if ch in PUNCTUATION:            # if character is punctuation caesar cipher used
                            alphabet=PUNCTUATION
                            CipherText += caesar_cipher_encryption(ch,N,alphabet)
                        elif ch in ALPHA_NUM:           # if character is a letter or number affine cipher used
                            alphabet=ALPHA_NUM
                            CipherText += affine_cipher_encryption(ch,N,alphabet)
                    print("Plain text:",Orig_Plaintext)        
                    print("Cipher text:",CipherText)

                if Input == "d":
                    Decrypt_str=input("Input a string to decrypt: ")
                    Orig_Plaintext=Decrypt_str                    
                    Decrypt_str=Decrypt_str.lower()
                    if ' ' in Decrypt_str:          # if space is in input, the program will reprompt for a command.
                        print("Error with character: ")
                        print("Cannot decrypt this string.")
                        break
                    CipherText=''                   # Building cipher text
                    for ch in Decrypt_str:
                        if ch in PUNCTUATION:       # if character is punctuation caesar cipher used
                            alphabet=PUNCTUATION
                            CipherText += caesar_cipher_decryption(ch,N,alphabet)
                        elif ch in ALPHA_NUM:       # if character is a letter or number affine cipher used
                            alphabet=ALPHA_NUM
                            CipherText += affine_cipher_decryption(ch,N,alphabet)
                    print("Cipher text:",Orig_Plaintext)                        
                    print("Plain text:",CipherText)
                Input= input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
            
               
        
        else:
            print("Error; rotation must be an integer.")  #if rotation is not an integer, try again until integer is input
        continue
    
        
if __name__ == "__main__":
    main()


   