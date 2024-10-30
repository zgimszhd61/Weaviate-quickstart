import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv

load_dotenv()

def generate_weaviate_response(query, limit=2, single_prompt=None):
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.getenv("WCD_URL"),
        auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_API_KEY")),
        headers={
            "X-OpenAI-Api-Key": os.environ.get("OPENAI_APIKEY")
        }
    )
    
    try:
        questions = client.collections.get("Question")
        
        response = questions.generate.near_text(
            query=query,
            limit=limit,
            single_prompt=single_prompt
        )
        
        return response.objects[0].generated
    
    finally:
        client.close()

if __name__ == "__main__":
    result = generate_weaviate_response(
        query="what is love?",
        limit=2,
        single_prompt="Explain {answer} as you might to a five-year-old."
    )
    print(result)