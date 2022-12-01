# Ransomware-Python-IPSSI

<!-- Image centrée -->

<div align="center">

![CAPTURE](https://www.zupimages.net/up/22/48/8coe.png)

</div>

<!-- --------------------------- -->

**Ransomware-Python-IPSSI** a été réalisé dans le cadre pédagogique de l'IPSSI avec un projet sur 1,5 jours. 

>Un ransomware est logiciel de rançon ou logiciel d'extorsion, est un logiciel malveillant qui prend en otage des données personnelles, le déchiffrement de ces dernières sont possible moyennant un paiement

# Prérequis
- Visual studio code

- Python3

- Dépendances Python : pycryptodomex et pycryptodome

Il est recommandé d'exécuter ce programme dans un environnement virtuel, il est possible d'en mettre un en place à l'aide des logiciels suivants : 
- Virtualbox --> Sur une VM Windows / Linux
- VMWare workstation pro --> Sur une VM Windows / Linux
- ...

# Description du projet et axes d'améliorations

Le projet est centralisé sur un seul fichier ```ransomware.py```, il utilise un fichier ```test.txt``` contenant du texte. Ce dernier sert de test pour l'exécution du Ransomware.
  
1) Génère une **paire de clés**
2) **Chiffre les fichiers / répertoires** à l'aide des clés générées
3) **Supprime les fichiers originaux à la fin de ce chiffrement**
4) Affiche un compte à rebours qui, **s'il arrive à la fin détruit les fichiers / répertoires chiffrés**
5) Un bouton " envoyer l'argent " est disponible, suite au clic de ce dernier, **cela débloque un bouton déchiffrer**
6) Ce bouton "déchiffre" **va déchiffrer les données et fermer le compte à rebourd**

# Environnement de travail

Installation des dépendances :

```
pip install pycryptodomex pycryptodome
```

L'exécution du script peut se faire de plusieurs manières, via un interpréteur de commandes, dans visual studio code etc...

### Mise en réseau
Ce projet se déroule entièrement en **local**.

# Auteur

Auteur du projet : Jean O.

Version stable : ```1.0```

# Licence

Ce projet est à but éducatif, il n'est soumis à aucune licences.
