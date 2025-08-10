import streamlit as st
from transformers import pipeline

# Cache the model loading to improve performance
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

# --- UI Config ---
st.set_page_config(page_title="🪄 DreamText Forge", layout="centered")
st.title("✨ DreamText Forge")
st.write("Shape your ideas into text magic with AI. Choose a suggested prompt or create your own.")

# Prompt suggestions
prompt_suggestions = [
    "Once upon a time, in a city where dreams walked among people...",
    "The scientist's latest invention would change the world forever, but...",
    "On the edge of the galaxy, a lone explorer discovered a signal...",
    "The forest was silent, except for the whisper of the ancient trees...",
    "In the year 2150, humans had finally mastered time travel, but..."
]

# Dropdown for selecting a prompt
selected_prompt = st.selectbox(
    "Choose a prompt suggestion:",
    ["(Write my own)"] + prompt_suggestions
)

# Text area for custom or editable prompt
if selected_prompt == "(Write my own)":
    prompt = st.text_area("Enter your prompt:", height=150)
else:
    prompt = st.text_area("Edit or extend the chosen prompt:", value=selected_prompt, height=150)

# Max length setting
max_length = st.slider("Max length of output", min_value=50, max_value=500, value=150, step=10)

# Generate button
if st.button("Generate"):
    if prompt.strip() != "":
        with st.spinner("Weaving your story..."):
            result = generator(
                prompt,
                max_length=max_length,
                num_return_sequences=1,
                temperature=0.7,
                repetition_penalty=1.2,
                eos_token_id=50256  # End-of-sequence token for GPT-2
            )
        st.subheader("✨ Generated Output:")
        st.write(result[0]['generated_text'])
    else:
        st.warning("Please enter or select a prompt before generating.")
