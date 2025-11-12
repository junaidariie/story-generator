# story_teller.py
from transformers import pipeline
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from PIL import Image
import streamlit as st
import os

load_dotenv()
openai_key = st.secrets["OPENAI_API_KEY"]

# ---------------- Load models/pipelines once ----------------
pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large", use_fast=True)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Ensure uploads folder exists
os.makedirs("uploads", exist_ok=True)

# ---------------- Image to text ----------------
def img2text(pil_image: Image.Image):
    text = pipe(pil_image)[0]["generated_text"]
    print(f"[img2text] {text}")
    return text

# ---------------- Generate story ----------------
def Generate_story(scenario: str):
    template = """
You are a skilled storyteller who writes brief, realistic stories.
Your task is to create a natural, emotionally believable short story (no more than 40 words) inspired by the following image description.

Guidelines:
- Keep the story grounded in real life.
- Focus on genuine human emotions, thoughts, or small moments.
- Use natural language that sounds like everyday conversation.
- Add subtle sensory or environmental details.
- Avoid fantasy, exaggeration, or dramatic clichés.

IMAGE DESCRIPTION:
{scenario}

Now write the STORY:
"""

    prompt = PromptTemplate(template=template, input_variables=['scenario'])
    formatted_prompt = prompt.format(scenario=scenario)

    story = llm.invoke(formatted_prompt).content
    print(f"[Generate_story] {story}")
    return story

