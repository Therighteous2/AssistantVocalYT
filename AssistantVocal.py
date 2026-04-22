import customtkinter as ctk   # Bibliothèque pour l'interface graphique
import speech_recognition as sr
import pyttsx3
from youtube_search import YoutubeSearch
import webbrowser                       # bibliothèque de la navigation sur internet - standard


# Initialisation de la synthèse vocale et la reconnaissance vocale

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Fonction pour parler (Synthèse vocale)
def parle(text):
    engine.say(text)
    engine.runAndWait()
# Fonction pour écouter et reconnaitre la voix
def reconnaissance_parole():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source) #Ajuster la sensibilité de notre micro pour réduire les bruits
        print("Parlez maintenant")

        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="fr-FR") # Ici, il s'agit d'un essai, la voix sera 
            print(f"Abel, Vous avez dit: {command}")                             # écouter via les services google et doit 
            return command.lower()                                         # etre retourner en minuscule pour faciliter la comparaison avec le reste du programme
        except sr.UnknownValueError:
            parle("Je n'ai pas compris, Abel")
            return ""
        except sr.RequestError:
            parle("Erreur de connexion, Abel!")
            return ""
        
# Fonction pour exécuter des commandes vocales

def execute_command():
    command = reconnaissance_parole()

    if "joue" in command:
        song_name = command.replace ("joue", "").strip() # On se focalise sur le "joue" et on enleve tous les superflus
        parle(f"Recherche de {song_name} sur YouTube.")

        # Recherche sur YT
        resultat = YoutubeSearch(song_name, max_results=1).to_dict()
        if resultat:
            video_url = f"https://www.youtube.com/watch?v={resultat[0]['id']}"
            parle(f"Lecture de {resultat[0]['id']}.")
            webbrowser.open(video_url)

        else:
            parle("Aucune vidéo trouvée")

    elif "Ouvre Youtube" in command:
        parle("Ouverture de Youtube.")
        webbrowser.open("https://www.youtube.com/")

    elif "ferme" in command:
        parle("Fermeture de Youtube")
        app.quit()

    else:
        parle("Commande non reconnue")



# Initialisation de l'application
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

app = ctk.CTk()              # Création de l'objet (fenetre)
app.title("Assistant Vocal - Abel M.") # Titre de la fenetre
app.geometry("500x400")

#Label d'instructions

label = ctk.CTkLabel(app, text="Cliquer sur le bouton pour écouter une commande", font=("Helvetica", 16))
label.pack(pady=30) # Marge en Y de 30

#Bouton pour activer la reconnaissance vocale

ecoute_bouton = ctk.CTkButton(app, text="ECOUTER",command=execute_command, font=("Helvetica", 16),height=50,width=200)
ecoute_bouton.pack(pady=20) # Marge verticale

#Bouton pour quitter l'application

quitter_bouton = ctk.CTkButton(app, text="QUITTER", command= app.quit, font=("Helvetica", 16),height=50,width=200,fg_color='red')
quitter_bouton.pack(pady=20) # Marge verticale



app.mainloop()               # Boucler notre app





