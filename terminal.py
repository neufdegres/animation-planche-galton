import sys
import webbrowser 

try:
    from video import *
except:
    print("Erreur: veuillez vous placer dans le dossier contenant \"gui.py\" et \"video.py\"")
    sys.exit(1)

def main() :
    billes = 0
    
    if os.path.exists("./video.avi"):
        os.remove("./video.avi")
        
    print("Bienvenue dans le programme générant automatiquement",
          "une animation du fonctionnement de la planche de Galton.")
    print("Celui-ci, après l'avoir crée, va l'ouvrir sur votre navigateur",
          "par default.\n")
    
    while(billes < 20 or billes > 70):
        billes = int(input("Combien de billes voulez-vous (min:20, max:70) ? "))
        
    print("Création de la vidéo en cours...")
    creer_anim(billes)
    print("Animation créée !")
    
    webbrowser.open("./video.avi")
    
try:
    main()
except:
    if os.path.exists("./video.avi"):
        os.remove("./video.avi")