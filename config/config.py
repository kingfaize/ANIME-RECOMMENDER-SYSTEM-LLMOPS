
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys (do not hardcode sensitive values)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Provider/model configuration
PROVIDERS = ["Groq", "OpenAI"]

PROVIDER_MODELS = {
	"Groq": [
		"llama-3.1-8b-instant",
		"qwen/qwen3-32b",
		"llama-3.3-70b-versatile"
	],
	"OpenAI": [
		"gpt-5.1",
		"gpt-5-mini",
		"gpt-5-nano",
		"gpt-5-pro",
		"gpt-3.5-turbo",
		"gpt-4",
		"gpt-4-turbo"
	]
}