
from backend.contracts import ActionRequest, ActionResponse, JobStatus
from backend.interfaces import Harness


class Brain:
    def __init__(self , harness: Harness):
        self.harness = harness

    async def handle(self , request_id:str , request: ActionRequest) -> ActionResponse:
        result = await self.harness.run(request.action, request.input)
        return ActionResponse(
            request_id=request_id,
            status=JobStatus.SUCCEEDED,
            result=result
        )