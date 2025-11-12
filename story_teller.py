# story_teller.py
from transformers import pipeline, VitsModel, VitsTokenizer
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from kokoro import KPipeline
import soundfile as sf
from dotenv import load_dotenv
from PIL import Image
import os



load_dotenv()

# ---------------- Load models/pipelines once ----------------
pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large",use_fast=True)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
kokoro_tts = KPipeline(lang_code='a')

model = VitsModel.from_pretrained("facebook/mms-tts-eng")
tokenizer = VitsTokenizer.from_pretrained("facebook/mms-tts-eng")

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

# ---------------- Text to speech ----------------
def text2speech(
    message: str,
    voice: str = 'af_heart',
    output_path: str = 'uploads/output.wav',
    rate: int = 24000
):
    generator = kokoro_tts(message, voice=voice)
    saved_files = []

    for i, (gs, ps, audio) in enumerate(generator):
        filename = f"{output_path.rsplit('.',1)[0]}_{i}.wav"
        sf.write(filename, audio, rate)
        saved_files.append(filename)
        print(f"[text2speech] Saved: {filename}")

    return saved_files



"""scenario = img2text("D:/Story teller/OIP.jpeg")
story = Generate_story(scenario)
text2speech(story)"""