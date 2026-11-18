
class AgentLoop:
    def __init__(self,agent):
        self.agent = agent

    async def run(self, action:str, prompt:str) -> str:
        return await self.agent.run(action, prompt)