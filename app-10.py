import weaviate
import os
import weaviate.classes as wvc
import json,requests

## Python教程：https://weaviate.io/developers/weaviate/quickstart#connection-details

from dotenv import load_dotenv
load_dotenv()
# Set these environment variables
URL = os.getenv("WCS_URL")
APIKEY = os.getenv("WCS_API_KEY")

# Connect to a WCS instance
client = weaviate.connect_to_wcs(
    cluster_url=URL,
    auth_credentials=weaviate.auth.AuthApiKey(APIKEY),
        headers={'X-OpenAI-Api-key': os.getenv("OPENAI_APIKEY")}  # Replace with your OpenAI API key

    )

try:

    ## 创建表格
    # questions = client.collections.create(
    #     name="Question",
    #     vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai(),  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
    #     generative_config=wvc.config.Configure.Generative.openai()  # Ensure the `generative-openai` module is used for generative queries
    # )

    ## 添加数据
    # resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
    # data = json.loads(resp.text)  # Load data

    # question_objs = list()
    # for i, d in enumerate(data):
    #     question_objs.append({
    #         "answer": d["Answer"],
    #         "question": d["Question"],
    #         "category": d["Category"],
    #     })

    # questions = client.collections.get("Question")
    # questions.data.insert_many(question_objs)

    ## 查询数据 - 1
    # questions = client.collections.get("Question")

    # response = questions.query.near_text(
    #     query="biology",
    #     limit=2,
    #     filters=wvc.query.Filter.by_property("category").equal("ANIMALS")
    # )

    # print(response.objects[0].properties)  # Inspect the first object


    ## 查询数据 - 2 （ RAG ） 
    # response = questions.generate.near_text(
    #     query="biology",
    #     limit=2,
    #     single_prompt="Explain {answer} as you might to a five-year-old."
    # )

    # print(response.objects[0].generated)  # Inspect the generated text

    ## 分组查询 - 3 （ RAG ）
    questions = client.collections.get("Question")
    response = questions.generate.near_text(
        query="biology",
        limit=2,
        grouped_task="Write a tweet with emojis about these facts."
    )

    print(response.generated)  # Inspect the generated text



finally:
    client.close()  # Close client gracefully
