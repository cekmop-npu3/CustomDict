from javascript import Object


class TestDict(Object):
    name: str
    id: int


class ServiceToken(Object):
    access_token: str


class ServiceTokenResponse(Object):
    response: list[int | ServiceToken]


a = ServiceTokenResponse({"response": [179, {"access_token": "99fd1ce0ff62b2c399fd1ce05699a02840999fd99fd1ce0ff624523f16b8c9049487efd"}]})

b = TestDict({'name': 'nameless', 'id': 1337})

c = a | b  # "c" object now has attributes of both "a" and "b"

print(c.name)

print(a.some_key)  # Syntax highlighting. Returns None

print(a.response[1].access_token)

print(b.id)
