# streamlit_app.py
import streamlit as st
from story_teller import img2text, Generate_story
from PIL import Image
from io import BytesIO

st.title("Image to Story Generator")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Convert streamlit upload to PIL Image
    image = Image.open(uploaded_file).convert("RGB")

    with st.spinner("Generating story..."):
        try:
            scenario = img2text(image)
            story = Generate_story(scenario)

            # Display scenario
            st.subheader("Scenario:")
            st.write(scenario)

            # Display story
            st.subheader("Story:")
            st.write(story)

        except Exception as e:
            st.error(f"Failed: {e}")
