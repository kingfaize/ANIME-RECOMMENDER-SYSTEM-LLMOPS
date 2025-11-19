

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap, RunnablePassthrough
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str, provider: str, temperature: float = 0.0):
        # Dynamically select LLM provider
        provider = provider.lower()
        if provider == "groq":
            from langchain_groq import ChatGroq
            self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=temperature)
        elif provider == "openai":
            from langchain_openai import ChatOpenAI
            self.llm = ChatOpenAI(api_key=api_key, model=model_name, temperature=temperature)
        elif provider == "huggingface":
            from langchain_community.llms.huggingface_hub import HuggingFaceHub
            self.llm = HuggingFaceHub(repo_id=model_name, huggingfacehub_api_token=api_key)
        # ...existing code...
        else:
            raise ValueError(f"Unsupported provider: {provider}")

        prompt_template = get_anime_prompt()
        if isinstance(prompt_template, PromptTemplate):
            self.prompt = prompt_template
        else:
            self.prompt = PromptTemplate(
                input_variables=["context", "question"],
                template=prompt_template
            )
        self.rag_chain = (
            RunnableMap({
                "context": retriever,
                "question": RunnablePassthrough()
            })
            | self.prompt
            | self.llm
        )

    def get_recommendation(self, query: str):
        return self.rag_chain.invoke(query)