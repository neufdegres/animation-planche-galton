# Animation Planche Galton

Programme montrant une animation du fonctionnement de la
planche de Galton à l'aide d'une vidéo automatiquement
générée.

Projet réalisé dans le cadre du projet de MD5 de la
licence Informatique générale à l'Université Paris Cité
en tant qu'illustration.

## Requirements :
- python >= 3.8.10
- modules python :
    Pillow (PIL) [9.2.0]
    tkVideoPlayer [2.3]
    opencv-python (cv2) [4.6.0.66]

## Lancement du programme :

Ouvrir un terminal, se déplacer à l'emplacement du
dossier du programme, puis exécuter la commande
suivante :   `python3 gui.py`

Si l'interface graphique ne fonctionne pas chez vous,
vous pouvez générer votre animation à l'aide du terminal
grâce à la commande suivante :    `python3 terminal.py`

## Fonctionnement de l'interface graphique :

Une fois l'animation générée, elle sera jouée en boucle
jusqu'a la fermeture de l'interface graphique ou 
l'actionnement du bouton "stop".

- Bouton play (▶) : 
    génère puis lance une nouvelle animation à chaque
    fois le bouton est activé. Si le bouton pause a été
    enclenché juste avant, appuyer sur le bouton play va
    reprendre l'animation en cours.

- Bouton pause (||) :
    met en pause l'animation en cours.

- Bouton stop (■) : 
    arrète l'animation en cours et "supprime" 
    l'animation créée. 

- choix de nombre de billes (de 20 à 70) : 
    le nombre est modifiable via les flèches, et sera 
    effectif pour la prochaine génération de
    l'animation.

## Fonctionnement de la version "terminal" :

Le programme va vous demande de saisir un nombre entre
20 et 70, puis va générer une vidéo, qui sera ensuite
ouverte sur votre navigateur internet par défaut.

Attention ! Relancer la commande `python3 ternimal.py`
va supprimer la vidéo "video.avi" créée dans le dossier
du programme si elle existe.
