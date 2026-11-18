from typing import Protocol

class Harness(Protocol):
    async def run(self, action: str, prompt: str) -> str: ...