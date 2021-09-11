from typing import Generic, Type, TypeVar


_RequestT = TypeVar('_RequestT')
_ResponseT = TypeVar('_ResponseT')


class AsyncClient(Generic[_RequestT, _ResponseT]):

    def __init__(self, request_type: Type[_RequestT], response_type: Type[_ResponseT]):
        pass

    async def __call__(self, request: _RequestT) -> _ResponseT:
        raise NotImplementedError()

    async def call(self, request: _RequestT) -> _ResponseT:  # other methods OK
        raise NotImplementedError()


class SyncClient(Generic[_RequestT, _ResponseT]):

    def __init__(self, request_type: Type[_RequestT], response_type: Type[_ResponseT]):
        pass

    def __call__(self, request: _RequestT) -> _ResponseT:
        raise NotImplementedError()


foo_async = AsyncClient(int, str)
foo_sync = SyncClient(int, str)
