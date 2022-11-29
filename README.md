# Ransomware-Python-IPSSI

![CAPTURE](https://zupimages.net/up/22/48/v9hz.png)

**Ce ransomware à été réalisé dans le cadre pédagogique de l'IPSSI sur un projet d'1,5 jours.**

Si vous n'utilisez pas d'interpréteur de Markdown, ce README est disponible sur GITHUB à cette adresse : https://github.com/IPSSI-Jean/Ransomware-Python-IPSSI


# Prérequis
- Visual studio code

- Python3

- Dépendances Python : pycryptodomex et pycryptodome

- Connaissances basique / intermédiaire en Python

  # Fonctionnement du projet
  
- Générer une paire de clés
- Chiffrer les fichiers / répertoires à l'aide des clés générées
- Supprimer les fichiers originaux à la fin de ce chiffrement
- Afficher un compte à rebourd qui, si il arrive à la fin détruit les fichiers / répertoires chiffrés
- Un bouton " envoyer l'argent " est disponible, suite au clic de ce dernier, cela débloque un bouton déchiffrer
- Ce bouton déchiffrer va déchiffrer les données et fermer le compte à rebourd

# Environnement de travail

Il est recommandé d'exécuter ce programme dans un environnement virtuel tel que : 
- Virtualbox
- VMWare workstation pro

Installation des dépendances :

```pip install pycryptodomex pycryptodome```

L'exécution du script peut se faire de plusieurs manières, via un interpréteur de commandes, dans visual studio code etc...

# Auteur

Auteur du projet : Jean O.

# Version du projet

Version stable : 1.0

# Licence

Ce projet est à but éducatif, il n'est sous aucune licences.
