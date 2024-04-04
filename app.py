import weaviate
import os

auth_config = weaviate.AuthApiKey(api_key="iQFPqI4Suud7Wc76dXD8pqkZKb0Btj4Jd96k")

client = weaviate.Client(
  url="https://my-sandbox-m5w2izwo.weaviate.network",
  auth_client_secret=auth_config
)

# schema = {
#     "classes": [
#         {
#             "class": "Person",
#             "description": "A person such as a user or a customer",
#             "properties": [
#                 {
#                     "name": "name",
#                     "dataType": ["string"],
#                     "description": "The name of the person",
#                 },
#                 {
#                     "name": "age",
#                     "dataType": ["int"],
#                     "description": "The age of the person",
#                 },
#             ],
#         },
#     ],
# }

# # 创建schema
# client.schema.create(schema)

# 添加一个Person对象
person_data = {
    "name": "John Doe",
    "age": 28,
}

# 使用add方法添加数据
client.data_object.create(person_data, "Person")

# 构建GraphQL查询
query = """
{
  Get {
    Person {
      name
      age
    }
  }
}
"""

# 执行查询
result = client.query.raw(query)

# 打印结果
print(result)