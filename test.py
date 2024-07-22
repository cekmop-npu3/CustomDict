from javascript import Object


class ServiceToken(Object):
    access_token: str


class ServiceTokenResponse(Object):
    response: ServiceToken


a = {"response": {"access_token": "0542896863dc7b7505428968a6051fbdc8005420542896863dc14d54905530079736583"}}

b = ServiceTokenResponse(a)

print(b)

print(b.response)

print(b.get('response'))

print(b.response.values())

