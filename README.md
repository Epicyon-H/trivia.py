# trivia.py

An easy to use python api wrapper for [Open Trivia DB](https://opentdb.com/api_config.php)




# Installing

Python 3.6 or higher is required

```
pip install trivia.py
```




# Usage

```python
question(parameters)
```

**Parameters:**
- amount (*int*):
    The amount of questions you wish to request, defaults to 10

- category (*int*):
    The category you wish to request from (refer to table below for which number correlates to which category), defaults to `None` returning all categories.

| Int | Category                              |
| --- |:------------------------------------- |
| 0   | All categories                        |
| 1   | General Knowledge                     |
| 2   | Entertainment: Books                  |
| 3   | Entertainment: Film                   |
| 4   | Entertainment: Music                  |
| 5   | Entertainment: Musicals & Theatres    |
| 6   | Entertainment: Television             |
| 7   | Entertainment: Video Games            |
| 8   | Entertainment: Board Games            |
| 9   | Science & Nature                      |
| 10  | Science: Computers                    |
| 11  | Science: Mathematics                  |
| 12  | Mythology                             |
| 13  | Sports                                |
| 14  | Geography                             |
| 15  | History                               |
| 16  | Politics                              |
| 17  | Art                                   |
| 18  | Celebrities                           |
| 19  | Animals                               |
| 20  | Vehicles                              |
| 21  | Entertainment: Comics                 |
| 22  | Science: Gadgets                      |
| 23  | Entertainment: Japanese Anime & Manga |
| 24  | Entertainment: Cartoon & Animations   |

- difficulty (*str*):
    The difficulty of the questions, can be `easy`, `medium`, or `hard`. Defaults to `None` returning all difficulties. 

- quizType (*str*):
    The type of questions, can be `multiple` (multiple choice questions), or `boolean` (true/false questions). Defaults to `None` returning all questions types. 


**Return:**

Return a list of dicts which contains the keys below
- category (*str*):
    The category the question comes from.

- type (*str*):
    The type of question (multiple, or boolean).

- difficulty (*str*):
    The difficulty of the question.

- question (*str*):
    The text of the question.

- correct_answer (*str*):
    The correct answer.

- incorrect_answer (*list*):
    List of strings of all the incorrect answers.




# Examples

**Basic code example**
```python
from trivia import Trivia

questions = Trivia.question(amount=1, category=2, difficulty='easy', quizType='boolean')
```


**An example of the return**
```python
[{
    'category': 'Science: Computers', 
    'type': 'boolean', 
    'difficulty': 'easy', 
    'question': 'Ada Lovelace is often considered the first computer programmer.', 
    'correct_answer': 'True', 
    'incorrect_answers': ['False']
    }]
```
