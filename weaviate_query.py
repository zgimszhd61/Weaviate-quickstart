import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv

def query_near_text_in_weaviate(query_text, limit=2):
    """
    Connect to a Weaviate cloud instance and query for objects using near text.
    
    Args:
        query_text (str): The text to use for the near text query.
        limit (int): The maximum number of results to return.
    
    Returns:
        list: List of properties from the objects returned by the query.
    """
    load_dotenv()

    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.getenv("WCD_URL"),
        auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_API_KEY")),
        headers={
            "X-OpenAI-Api-Key": os.environ.get("OPENAI_APIKEY")
        }
    )

    try:
        # Get the "Question" collection and perform a near text query.
        questions = client.collections.get("Question")
        response = questions.query.near_text(
            query=query_text,
            limit=limit
        )

        return [obj.properties for obj in response.objects]

    finally:
        # Close client gracefully.
        client.close()

# Example usage
if __name__ == "__main__":
    result = query_near_text_in_weaviate("biology", limit=2)
    if result:
        print(result[0])  # Inspect the first object's properties
