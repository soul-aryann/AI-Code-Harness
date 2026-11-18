
from dataclasses import dataclass
from enum import Enum


class JobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELED = "canceled"

@dataclass(frozen=True)
class ActionRequest:
    action: str
    input: str
    conversation_id: str | None = None
    repository_id: str | None = None

@dataclass(frozen=True)
class ActionResponse:
    request_id: str
    status: JobStatus
    result: str | None = None
    error: str | None = None