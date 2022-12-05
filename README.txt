Programme montrant une animation du fonctionnement de la
planche de Galton à l'aide d'une interface graphique.


Requirements :
- python >= 3.8.10
- modules python :
    Pillow (PIL)
    tkVideoPlayer
    opencv-python (cv2)


Lancement du programme :

Ouvrir un terminal, se déplacer à l'emplacement du
dossier du programme, puis exécuter la commande
suivante:   `python3 gui.py`


Fonctionnement de l'interface graphique :

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

- choix de nombre de billes (de 20 à 80) : 
    le nombre est modifiable via les flèches, et sera 
    effectif pour la prochaine génération de
    l'animation.