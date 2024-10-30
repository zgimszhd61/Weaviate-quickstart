import weaviate
import weaviate.classes as wvc
import os
import json
import requests
from dotenv import load_dotenv


def insert_questions_with_vectors():
    load_dotenv()

    # Connect to Weaviate cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.getenv("WCD_URL"),
        auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_API_KEY")),
        headers={
            "X-OpenAI-Api-Key": os.environ.get("OPENAI_APIKEY")
        },
        additional_config=weaviate.config.AdditionalConfig(
            timeout=weaviate.config.Timeout(init=60)  # 设置初始化超时时间为60秒
        )
    )

    try:
        # Load data from URL
        fname = "jeopardy_tiny_with_vectors_all-OpenAI-ada-002.json"  # This file includes pre-generated vectors
        url = f"https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/{fname}"
        resp = requests.get(url)
        data = json.loads(resp.text)

        # Create data objects
        question_objs = [
            wvc.data.DataObject(
                properties={
                    "answer": d["Answer"],
                    "question": d["Question"],
                    "category": d["Category"],
                },
                vector=d["vector"]
            ) for d in data
        ]

        # Insert data objects into Weaviate
        questions = client.collections.get("Question")
        questions.data.insert_many(question_objs)  # This uses batching under the hood

    finally:
        client.close()  # Close client gracefully


if __name__ == "__main__":
    insert_questions_with_vectors()