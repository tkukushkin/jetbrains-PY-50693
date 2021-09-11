from project import module
from project.module import foo_async, foo_sync, foo_without_generics


async def main() -> None:
    res1 = await foo_async(1)  # OK
    res2 = await module.foo_async(1)  # NOT OK
    res3 = await foo_async()  # OK
    res4 = await module.foo_async()  # OK

    res5 = await foo_async.call(1)  # OK
    res6 = await module.foo_async.call(1)  # OK

    res7 = foo_sync(1)  # OK
    res8 = module.foo_sync(1)  # NOT OK

    res9 = await foo_without_generics(1)  # OK
    res10 = await module.foo_without_generics(1)  # OK
