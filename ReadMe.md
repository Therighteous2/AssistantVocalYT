# 🎤 ASSISTANT VOCAL EN PYTHON
## 📌 Description
Ce projet est un assistant vocal simple développé en Python. Il permet de:
✔ de parler
✔ d'écouter
✔ de reconnaître la parole et la convertir en texte
✔ d'exécuter des commandes basées sur la voix

## ⚙ Fonctionnalités
🔊 Synthèse vocale (text-to-speeech)
🎙 Reconnaissance vocale en temps réel
🌐 Utilisation de l'API Google pour la reconnaissance vocale
⚠  Gestion des erreurs (voix non reconnue, problème réseau)

## 🧰 Technologies utilisées
✔ Python 3.10/11 (version stable)
✔ speech_recognition (écoute et converit la parole en texte)
✔ pyttsx3 ("permet à l'ordinateur de parler (Synthèse vocale))
✔ PyAudio (accès au micro)
✔  YoutubeSearch (fait des recherches sur YT et retourne les resultats sous formes des dictionnaires)
## 📥 Installation
1. Cloner le projet
git clone "mon_repo"
cd "mon_projet"
2. pip install SpeechRecognition
   pip install pyttsx3
   pip install youtube-search
   pip install pyaudio
3. Installer aussi PyAudio (important)
Sur windows:
   pip install pipwin
   pipwin install pyaudio

## ▶ Utilisation
1. L'utilisateur demande au programme d'écouter
2. Le programme te demande de parler
3. Il écoute ce que tu as dit
4. Il peut répondre ou exécuter une commande

## 📂 Structure du code

----- Interface Utilisateur
|
|---- Parle(text): fait parler l'assistant
|---- Reconnaissance_parole: écoute et convertit la voix en texte
|---- Gestion des erreurs--- Parler clairement
|                         |__ Vérifier la connexion internet
|


## 🚀 Améliorations possibles

Mode offline
Support multilingue
Ajouter commandes (ouvrir apps, météo,etc.)

## 👩‍💻 Auteur

Projet dévéloppé par Abel M.



