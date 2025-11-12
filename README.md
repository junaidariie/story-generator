Story Teller
A FastAPI-based application that transforms images into engaging audio stories using AI. Upload an image, and the system generates a descriptive scenario, creates a short story, and converts it into speech.

🌟 Features
Image-to-Text: Extracts descriptive scenarios from uploaded images using BLIP model

AI Story Generation: Creates natural, emotionally resonant short stories using Google Gemini

Text-to-Speech: Converts generated stories into audio using Kokoro TTS

RESTful API: Clean FastAPI endpoints with proper error handling

File Management: Automatic organization of uploaded audio files

🛠️ Tech Stack
Backend: FastAPI

AI Models:

BLIP Image Captioning (Salesforce)

Google Gemini 2.5 Flash

Kokoro TTS & Facebook MMS-TTS

Audio Processing: SoundFile

Image Processing: PIL (Pillow)
