import weaviate
import weaviate.classes as wvc
import os
import json,requests
from dotenv import load_dotenv
load_dotenv()

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
    fname = "jeopardy_tiny_with_vectors_all-OpenAI-ada-002.json"  # This file includes pre-generated vectors
    url = f"https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/{fname}"
    resp = requests.get(url)
    data = json.loads(resp.text)  # Load data

    question_objs = list()
    for i, d in enumerate(data):
        question_objs.append(wvc.data.DataObject(
            properties={
                "answer": d["Answer"],
                "question": d["Question"],
                "category": d["Category"],
            },
            vector=d["vector"]
        ))

    questions = client.collections.get("Question")
    questions.data.insert_many(question_objs)    # This uses batching under the hood

finally:
    client.close()  # Close client gracefully