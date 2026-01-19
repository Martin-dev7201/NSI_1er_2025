# -*- coding: utf-8 -*-

def decrypteCle(message,cle):
    '''
    decrypte le message avec la cle
    
    Arguments :
    message : message crypte (string)
    cle : cle de cryptage (string)

    Retour
    message moins la cle et sans espace (string)
    '''
    messageDecrypt=''
    messageLst = message.split(' ')
    for bloc in messageLst :
        for i in range (len(bloc)):
            chiffre_message = int(bloc[i])
            chiffre_cle = int(cle[i])
            if chiffre_message>= chiffre_cle:
                resultat = chiffre_message - chiffre_cle
            else:
                resultat = 10+chiffre_message - chiffre_cle
            messageDecrypt += str(resultat)
    return messageDecrypt

def decoupeTexteCrypte(message,tableAlphabet):
    """
    Decoupe chaque caractere du message crypte MOINS LA CLE 
    en fonction de la table d'alphabet
    Arguments :
    message : message moins la cle (string)
    tableAlphabet : Liste des codes alphabétiques (liste de string)

    Retour
    Listes des valeurs codees decoupees selon l’alphabet (string)
    """

    messageDecoupe=[]
    while len(message)>0:
        if message[0] in tableAlphabet :
            messageDecoupe.append(message[0])
            message=message[1:]
        else :
            messageDecoupe.append(message[:2])
            message=message[2:]
    return messageDecoupe
    

        
def decrypteAlphabet(messageCoupe,tableAlphabet):
    """Decrypter le message selon l'alphabet
    Arguments d'entree : 
    message : message sous forme de liste de caracteres codes (type string)
    tableAlphabet : Alphabet sous la forme d une liste de lettre codees (type string)
    retour :
    message decrypte (type string)
    """

    alphabet='abcdefghijklmnopqrstuvwxyz'
    messageDecrypte=''
    for caractere in messageCoupe:
        positionDansTable=tableAlphabet.index(caractere)
        caractereDecode=alphabet[positionDansTable]
        messageDecrypte+=caractereDecode
    return messageDecrypte

tableAlphabet =['6','38','32','4','8','30','36','34','39','31','78','72','70','76','9','79','71','58','2','0','52','50','56','54','1','59']
cle = '12681'
message = "84403 79217 84583 84557 48829 37610 09878 74068 38101 09657 95453 94868 72380 88900 97839 57857 99848 75233 97839 82557 02557 98348 71344 30833 60167 55578 31345 60405 95853 99213 46257 19865 95446 99733 99668 72068 71168 18345 41435"
code = decrypteAlphabet(decoupeTexteCrypte(decrypteCle(message,cle),tableAlphabet),tableAlphabet)




