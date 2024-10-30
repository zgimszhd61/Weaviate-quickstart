import weaviate
import json
import requests
import os
import weaviate.classes as wvc
from dotenv import load_dotenv

def import_questions_to_weaviate():
    load_dotenv()
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.getenv("WCD_URL"),
        auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_API_KEY")),
        headers={
            "X-OpenAI-Api-Key": os.environ.get("OPENAI_APIKEY")
        }
    )

    try:
        questions = client.collections.create(
            name="Question",
            vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai(),  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
            generative_config=wvc.config.Configure.Generative.openai()  # Ensure the `generative-openai` module is used for generative queries
        )

        # Fetch data from URL
        resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
        data = json.loads(resp.text)  # Load data

        # Prepare data objects for Weaviate
        question_objs = [{
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"]
        } for d in data]

        # Insert data into Weaviate
        questions = client.collections.get("Question")
        questions.data.insert_many(question_objs)

    finally:
        client.close()  # Gracefully close the client

# Usage example
if __name__ == "__main__":
    import_questions_to_weaviate()
