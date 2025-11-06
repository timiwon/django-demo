from typing import TypedDict, NotRequired

class User(TypedDict):
    username: str
    email: str

class Article(TypedDict):
    title: str
    content: str
    owner: NotRequired[User]