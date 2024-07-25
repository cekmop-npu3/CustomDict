from javascript import Object

from typing import Union


class TestDict(Object):
    name: str
    id: int


class ServiceToken(Object):
    access_token: str


class ServiceTokenResponse(Object):
    response: list[Union[TestDict, ServiceToken]]  # Union[obj1, obj2] is better for annotations than obj1 | obj2


a = ServiceTokenResponse({"response": [TestDict(name=12), {"access_token": "99fd1ce0ff62b2c399fd1ce05699a02840999fd99fd1ce0ff624523f16b8c9049487efd"}]})

a.update({'value': {'smth': 34}})

a.value = {'newValue': 34}

c = ServiceTokenResponse.fromkeys(['s', 'v'], TestDict(name=12)(surname=14)) | a

print(c)  # {'s': {'name': 12, 'surname': 14}, 'v': {'name': 12, 'surname': 14}, 'response': [{'name': 12}, {'access_token': '99fd1ce0ff62b2c399fd1ce05699a02840999fd99fd1ce0ff624523f16b8c9049487efd'}], 'value': {'newValue': 34}}
