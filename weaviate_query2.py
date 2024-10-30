import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv

def fetch_biology_related_tweets():
    """
    Connects to a Weaviate cloud instance, queries biology-related information,
    and generates a tweet with facts using OpenAI's API.

    Returns:
        str: Generated response from the query.
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
        # Replace with your code if needed
        questions = client.collections.get("Question")

        response = questions.generate.near_text(
            query="biology",
            limit=2,
            grouped_task="Write a tweet with emojis about these facts."
        )

        return response.generated

    finally:
        client.close()  # Close client gracefully

# Example usage:
if __name__ == "__main__":
    generated_response = fetch_biology_related_tweets()
    print(generated_response)
