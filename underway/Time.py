# import asyncio
# from typing import Callable, Any, List
#
#
# async def slow_down(func: Callable, seconds: int) -> Any:
#     await asyncio.sleep(seconds)
#
#
# @asyncio
# def counting() -> List:
#     return [x ** 5 for x in range(50)]
#