import weaviate

client = weaviate.Client(
    url="https://my-sandbox-m5w2izwo.weaviate.network",  # Replace with your endpoint
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=""),  # Replace w/ your Weaviate instance API key
)


# 如果您尚未创建schema，请取消以下注释并执行
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
# client.schema.create(schema)

# # 添加一个Person对象
# person_data = {
#     "name": "John Doe",
#     "age": 28,
# }

# try:
#     # 使用add方法添加数据
#     client.data_object.create(person_data, "Person")
# except Exception as e:
#     print(f"添加数据时发生错误：{e}")

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

try:
    # 执行查询
    result = client.query.raw(query)
    # 打印结果
    print(result)
except Exception as e:
    print(f"执行查询时发生错误：{e}")