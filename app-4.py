import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv
load_dotenv()

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_API_KEY")),
    headers={
        "X-OpenAI-Api-Key": os.environ.get("OPENAI_APIKEY")
    }
)

try:
    pass # Replace with your code. Close client gracefully in the finally block.
    questions = client.collections.get("Question")

    response = questions.query.near_text(
        query="biology",
        limit=2
    )

    print(response.objects[0].properties)  # Inspect the first object

finally:
    client.close()  # Close client gracefully