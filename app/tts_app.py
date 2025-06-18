import streamlit as st
from TTS.api import TTS
import tempfile
import os

# Load your custom voice model
VOICE_PATH = "voice_model/pulse_of_png_clone_voice.wav"

# Initialize the TTS model (Fastest option)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

st.set_page_config(page_title="Voice News PNG", layout="centered")
st.title("🗣️ Voice News PNG - TTS App")

text = st.text_area("Enter news text below:", height=200)

if st.button("🎙️ Generate Voice"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Synthesizing..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as fp:
                tts.tts_to_file(text=text, file_path=fp.name, speaker_wav=VOICE_PATH)
                audio_bytes = open(fp.name, "rb").read()
                st.audio(audio_bytes, format="audio/wav")
                st.download_button("⬇️ Download Audio", audio_bytes, file_name="voice_news.wav")
