from project import package
from project.package import foo_async, foo_sync


async def main() -> None:
    res1 = await foo_async(1)  # OK
    res2 = await package.foo_async(1)  # NOT OK
    res3 = await foo_async()  # OK
    res4 = await package.foo_async()  # NOT OK

    res5 = await foo_async.call(1)  # OK
    res6 = await package.foo_async.call(1)  # OK

    res7 = foo_sync(1)  # OK
    res8 = package.foo_sync(1)  # NOT OK
