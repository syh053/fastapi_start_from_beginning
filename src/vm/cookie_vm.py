from uuid import UUID

from pydantic import BaseModel


class Cookies(BaseModel):
    model_config = {"extra": "forbid"}

    session_id: UUID
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None
