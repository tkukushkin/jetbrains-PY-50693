from project import package
from project.package import foo


async def main() -> None:
    res1 = await foo(1)
    res2 = await package.foo(2)
    res3 = await foo()
    res4 = await package.foo()
