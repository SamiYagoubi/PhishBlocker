import io
import os
import streamlit as st
from google.cloud import vision
from transformers import pipeline

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/chaibikenza/Desktop/Work shop /tidal-fusion-430213-q6-85160951abed.json'

def extract_text_from_image(image_path):
    client = vision.ImageAnnotatorClient()
    content = image_path.read()  # Use the uploaded image file directly
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description if texts else "Aucun texte détecté"

def classify_text(text):
    classifier = pipeline("text-classification", model="ealvaradob/bert-finetuned-phishing")
    result = classifier(text)
    return result

st.title("Phishing Detection from Image")

uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    extracted_text = extract_text_from_image(uploaded_image)

    st.subheader("Extracted Text:")
    st.write(extracted_text)

    # Classify the extracted text for phishing
    if extracted_text:
        result = classify_text(extracted_text)
        st.subheader("Phishing Detection Result:")
        st.write(result)
