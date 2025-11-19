# Anime Recommender

A multi-provider, LLM-powered anime recommendation system with a Streamlit frontend and modular backend.

## Features
- **Dynamic LLM Provider Selection:** Choose between Groq and OpenAI from the sidebar.
- **Vector Search:** Uses ChromaDB and Sentence Transformers for semantic search over anime data.
- **Retrieval-Augmented Generation (RAG):** Combines vector search with LLMs for context-aware recommendations.
- **API Key Management:** Supports both `.env`-based API key configuration and operator input via the sidebar for all providers.
- **Temperature Control:** Adjust LLM creativity with a temperature slider.
- **Extensible Pipeline:** Modular backend for easy provider/model updates.

## Project Structure
```
app/
  app.py                # Streamlit frontend
pipeline/
  pipeline.py           # Orchestrates vector store and LLM pipeline
src/
  recommender.py        # LLM instantiation and RAG logic
  vector_store.py       # Vector store and embedding logic
utils/
  custom_exception.py   # Custom error handling
  logger.py             # Logging utilities
config/
  config.py             # API key and model config
requirements.txt        # Dependency management
.env                    # API keys (not committed)
```

## Setup
1. **Clone the repository**
2. **Create and activate a virtual environment (recommended name: `venv311`)**
   ```
   python -m venv venv311
   .\venv311\Scripts\activate
   ```
3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
4. **Add your API keys to a `.env` file** (see `.env.example` if available), or enter them in the Streamlit sidebar when prompted.
5. **Run the app:**
   ```
   streamlit run app/app.py
   ```

## Usage
- Select your preferred LLM provider and model from the sidebar.
- Enter your anime preferences or questions.
- Adjust the temperature slider to control LLM creativity.
- Enter API keys in the sidebar if not set in `.env`.
- Get recommendations powered by the selected LLM and vector search.

## Troubleshooting
- Ensure all dependencies are installed and versions are pinned as in `requirements.txt`.
- If you see import errors, delete and recreate your virtual environment, then reinstall dependencies.
- For provider/model errors, check your API keys and model availability.
- Make sure you are using the correct virtual environment (`venv311`).

## License
MIT License
