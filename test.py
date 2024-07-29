from dataclasses import dataclass
from typing import List

@dataclass
class QuizItem:
    Category: str
    Question: str
    Answer: str

@dataclass
class Quiz:
    items: List[QuizItem]

# 示例JSON字符串
json_string = '''
[
    {"Category":"SCIENCE","Question":"This organ removes excess glucose from the blood & stores it as glycogen","Answer":"Liver"},
    {"Category":"ANIMALS","Question":"It's the only living mammal in the order Proboseidea","Answer":"Elephant"},
    {"Category":"ANIMALS","Question":"The gavial looks very much like a crocodile except for this bodily feature","Answer":"the nose or snout"},
    {"Category":"ANIMALS","Question":"Weighing around a ton, the eland is the largest species of this animal in Africa","Answer":"Antelope"},
    {"Category":"ANIMALS","Question":"Heaviest of all poisonous snakes is this North American rattlesnake","Answer":"the diamondback rattler"},
    {"Category":"SCIENCE","Question":"2000 news: the Gunnison sage grouse isn't just another northern sage grouse, but a new one of this classification","Answer":"species"},
    {"Category":"SCIENCE","Question":"A metal that is ductile can be pulled into this while cold & under pressure","Answer":"wire"},
    {"Category":"SCIENCE","Question":"In 1953 Watson & Crick built a model of the molecular structure of this, the gene-carrying substance","Answer":"DNA"},
    {"Category":"SCIENCE","Question":"Changes in the tropospheric layer of this are what gives us weather","Answer":"the atmosphere"},
    {"Category":"SCIENCE","Question":"In 70-degree air, a plane traveling at about 1,130 feet per second breaks it","Answer":"Sound barrier"}
]
'''

import json

# 解析JSON字符串
data = json.loads(json_string)

# 将JSON数据转换为Quiz对象
quiz_items = [QuizItem(**item) for item in data]
quiz = Quiz(items=quiz_items)


# 添加一个新的QuizItem
new_item = QuizItem(Category="HISTORY", Question="Who was the first president of the United States?", Answer="George Washington")
quiz.items.append(new_item)



# 打印Quiz对象
print(quiz)
