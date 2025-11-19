

import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv
import os
from config.config import PROVIDERS, PROVIDER_MODELS



st.set_page_config(page_title="Anime Recommnder", layout="wide")
load_dotenv()

# Sidebar for provider/model selection


st.sidebar.header("Model Provider Settings")
provider = st.sidebar.selectbox("Select API Provider", PROVIDERS)


# Embedding key input (always visible, operator can override env)
embedding_env_key = os.getenv("HUGGINGFACE_API_KEY", "")
embedding_input = st.sidebar.text_input(
    "HuggingFace Embedding API Key (leave blank to use .env)",
    value="",
    type="password"
)
embedding_key = embedding_input if embedding_input else embedding_env_key
if not embedding_key:
    st.sidebar.warning("Please provide a HuggingFace API key for embeddings.")

# LLM key and model selection

if provider == "Groq":
    groq_env_key = os.getenv("GROQ_API_KEY", "")
    groq_input = st.sidebar.text_input(
        "Groq API Key (leave blank to use .env)",
        value="",
        type="password"
    )
    api_key = groq_input if groq_input else groq_env_key
    if not api_key:
        st.sidebar.warning("Please provide a Groq API key.")
    model = st.sidebar.selectbox(
        "Model",
        PROVIDER_MODELS[provider]
    )
    temperature = st.sidebar.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.0,
        step=0.1,
        help="Controls randomness. 0 = deterministic, 2 = most random."
    )
elif provider == "OpenAI":
    openai_env_key = os.getenv("OPENAI_API_KEY", "")
    openai_input = st.sidebar.text_input(
        "OpenAI API Key (leave blank to use .env)",
        value="",
        type="password"
    )
    api_key = openai_input if openai_input else openai_env_key
    if not api_key:
        st.sidebar.warning("Please provide an OpenAI API key.")
    model = st.sidebar.selectbox(
        "Model",
        PROVIDER_MODELS[provider]
    )
    temperature = st.sidebar.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.0,
        step=1.0,
        help="Controls randomness. 0 = deterministic, 1 = most random."
    )
else:
    api_key = ""
    model = ""
    temperature = 0.0


@st.cache_resource
def init_pipeline(provider, api_key, model, temperature, embedding_key):
    return AnimeRecommendationPipeline(provider=provider, api_key=api_key, model_name=model, temperature=temperature, embedding_key=embedding_key)

pipeline = init_pipeline(provider, api_key, model, temperature, embedding_key)


st.title("Anime Recommender System")

query = st.text_input("Enter your anime prefernces eg. : light hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you....."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)


