import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv

def query_weaviate():
    """
    Connect to Weaviate cloud instance, query the Question collection for items related to biology,
    and print the properties of the first object in the result.
    """
    load_dotenv()

    # Connect to Weaviate cloud instance
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.getenv("WCD_URL"),
        auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_API_KEY")),
        headers={
            "X-OpenAI-Api-Key": os.environ.get("OPENAI_APIKEY")
        }
    )

    try:
        # Query the collection "Question"
        questions = client.collections.get("Question")

        response = questions.query.near_text(
            query="biology",
            limit=2,
            filters=wvc.query.Filter.by_property("category").equal("ANIMALS")
        )

        # Print the properties of the first object
        if response.objects:
            print(response.objects[0].properties)
        else:
            print("No objects found.")

    finally:
        # Close client gracefully
        client.close()

# Usage
if __name__ == "__main__":
    query_weaviate()