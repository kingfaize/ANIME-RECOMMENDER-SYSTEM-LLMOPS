from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)



class AnimeRecommendationPipeline:
    def __init__(self, provider, api_key, model_name, temperature=0.0, embedding_key=None, persist_dir="chroma_db"):
        try:
            logger.info("Intializing Recommdation Pipeline")

            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir, embedding_key=embedding_key)
            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(
                retriever=retriever,
                api_key=api_key,
                model_name=model_name,
                provider=provider,
                temperature=temperature
            )

            logger.info("Pipleine intialized sucesfully...")

        except Exception as e:
            logger.error(f"Failed to intialize pipeline {str(e)}")
            raise CustomException("Error during pipeline intialization", e)

    def recommend(self, query: str) -> str:
        try:
            logger.info(f"Recived a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated sucesfulyy...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation", e)
        


        