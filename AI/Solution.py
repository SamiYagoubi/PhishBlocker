import random
import streamlit as st
from google.cloud import vision
from transformers import pipeline
import os

# Set environment variable for Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/chaibikenza/Desktop/WorkShop3/tidal-fusion-430213-q6-85160951abed.json'

# Function to extract text from an image using Google Cloud Vision API
def extract_text_from_image(image_path):
    client = vision.ImageAnnotatorClient()
    content = image_path.read()  # Use the uploaded image file directly
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description if texts else "Aucun texte détecté"

# Function to classify extracted text using BERT phishing detection model
def classify_text(text):
    classifier = pipeline("text-classification", model="ealvaradob/bert-finetuned-phishing")
    result = classifier(text)
    return result

# Function to display phishing quiz
def phishing_quiz():
    questions = [
        {"question": "Qu'est-ce que le phishing ?", "options": ["Un type de malware", "Une attaque d'ingénierie sociale", "Une erreur de codage"], "answer": "Une attaque d'ingénierie sociale"},
        {"question": "Que devez-vous faire si vous recevez un e-mail suspect ?", "options": ["Cliquer sur le lien", "L'ignorer", "Le signaler"], "answer": "Le signaler"},
        {"question": "Laquelle des techniques suivantes est courante dans les attaques de phishing ?", "options": ["Usurpation d'adresses e-mail", "Utilisation de mots de passe forts", "Activation de l'authentification à deux facteurs"], "answer": "Usurpation d'adresses e-mail"},
        {"question": "Quelles informations sont souvent ciblées dans les escroqueries par phishing ?", "options": ["Nom d'utilisateur et mot de passe", "Date de naissance", "Couleur préférée"], "answer": "Nom d'utilisateur et mot de passe"},
        {"question": "Comment pouvez-vous vérifier si un e-mail est légitime ?", "options": ["Vérifiez l'adresse e-mail de l'expéditeur", "Répondez à l'e-mail", "Cliquez sur tous les liens"], "answer": "Vérifiez l'adresse e-mail de l'expéditeur"},
        {"question": "Que devez-vous faire si vous avez accidentellement cliqué sur un lien de phishing ?", "options": ["Rien", "Changez immédiatement vos mots de passe", "Partagez-le avec des amis"], "answer": "Changez immédiatement vos mots de passe"},
        {"question": "Quel est l'objectif principal des attaques de phishing ?", "options": ["Divertir les utilisateurs", "Voler des informations personnelles", "Diffuser des logiciels malveillants"], "answer": "Voler des informations personnelles"},
        {"question": "Lequel des e-mails suivants est probablement une tentative de phishing ?", "options": ["De votre banque demandant des détails de compte", "D'un ami", "D'une entreprise connue"], "answer": "De votre banque demandant des détails de compte"},
        {"question": "Que devez-vous faire avec des e-mails non sollicités d'expéditeurs inconnus ?", "options": ["Les ouvrir", "Les supprimer", "Y répondre"], "answer": "Les supprimer"},
        {"question": "Est-il sûr de télécharger des pièces jointes provenant de sources inconnues ?", "options": ["Oui", "Non", "Seulement si cela semble sûr"], "answer": "Non"},
    ]

    # Shuffle questions for randomness
    random.shuffle(questions)

    st.subheader("Quiz de Sensibilisation au Phishing")

    # Initialize session state for answered questions
    if 'answers' not in st.session_state:
        st.session_state.answers = [None] * len(questions)

    # Initialize session state for score
    if 'score' not in st.session_state:
        st.session_state.score = 0

    # Display each question with buttons for options
    for idx, question in enumerate(questions):
        st.write(f"**Question {idx + 1}:** {question['question']}")

        # If the question hasn't been answered yet, show the options
        if st.session_state.answers[idx] is None:
            selected_option = st.radio(
                f"Choisissez votre réponse pour la question {idx + 1} :", 
                question['options'], 
                key=f"question_{idx}"
            )

            # Button to submit the answer for each question
            if st.button(f"Valider la réponse {idx + 1}", key=f"submit_{idx}"):
                st.session_state.answers[idx] = selected_option  # Save the selected answer
                if selected_option == question['answer']:
                    st.success("✅ Bonne réponse !")
                    st.balloons()  # Show balloons for correct answer
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Mauvaise réponse. La bonne réponse est : {question['answer']}.")

        # If already answered, show the selected answer
        else:
            st.write(f"Vous avez déjà répondu : **{st.session_state.answers[idx]}**")

    # Show the final score if all questions are answered
    if None not in st.session_state.answers:
        st.write(f"Quiz terminé ! Votre score est de {st.session_state.score}/{len(questions)}.")
        if st.session_state.score >= 7:
            st.balloons()
            st.success("🎉 Félicitations, vous avez réussi le quiz !")
        else:
            st.error("⚠️ Faites attention, vous êtes susceptible d’être victime d'une escroquerie sur les réseaux sociaux.")

# Streamlit page configuration
st.set_page_config(page_title="PhishBlocker", page_icon="🛡️", layout="wide")

# Sidebar navigation links
st.sidebar.title("Navigation")
page_options = ["Accueil", "À propos", "Quiz", "Sécurité des Données"]
selection = st.sidebar.selectbox("Choisissez une page:", page_options)

# Navigation logic
if selection == "À propos":
    st.title("À propos de PhishBlocker")
    st.write("""
    **PhishBlocker** est un outil de protection contre le phishing dissimulé dans les images. Utilisez notre plateforme pour analyser du texte dans des images et identifier des tentatives de phishing.
    """)
    st.image("https://path/to/phishblocker_logo.png", width=300)

elif selection == "Quiz":
    phishing_quiz()

elif selection == "Sécurité des Données":
    st.title("Sécurité des Données")
    st.write("""
    Chez **PhishBlocker**, nous prenons très au sérieux la sécurité de vos données. Nous ne stockons pas les images que vous téléchargez ni les données extraites. 
    Toutes les informations sont traitées en mémoire et ne sont pas sauvegardées sur nos serveurs. 

    Pour plus d'informations, veuillez consulter notre [Politique de Confidentialité](#).
    """)
    st.write("Nous vous recommandons de ne pas télécharger d'images contenant des informations sensibles ou personnelles.")

else:
    st.title("PhishBlocker")
    uploaded_image = st.file_uploader("Télécharger une image", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Image téléchargée", use_column_width=True)
        extracted_text = extract_text_from_image(uploaded_image)
        st.subheader("Texte extrait :")
        st.write(extracted_text)
        if extracted_text:
            result = classify_text(extracted_text)
            label = result[0]['label']

            if label == "phishing":
                st.warning("⚠️ Ceci semble être une tentative de phishing.")
            else:
                st.success("✅ Aucun contenu suspect détecté.")
                st.balloons()

# Footer with GDPR and ergonomic information
st.markdown("---")
st.write("""
**© 2024 PhishBlocker** | Tous droits réservés.
- [Politique de Confidentialité](#)
- [Conditions d'Utilisation](#)

Ce site respecte les normes RGPD et s'engage à protéger vos données personnelles. 
Si vous avez des questions concernant notre politique de confidentialité, n'hésitez pas à nous contacter.
""")
