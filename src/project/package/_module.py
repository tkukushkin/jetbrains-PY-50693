from typing import Generic, Type, TypeVar


_RequestT = TypeVar('_RequestT')
_ResponseT = TypeVar('_ResponseT')


class Client(Generic[_RequestT, _ResponseT]):

    def __init__(self, request_type: Type[_RequestT], response_type: Type[_ResponseT]):
        pass

    async def __call__(self, request: _RequestT) -> _ResponseT:
        raise NotImplementedError()


foo = Client(int, str)
