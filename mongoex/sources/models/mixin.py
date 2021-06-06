from datetime import datetime
from pydantic import BaseModel, Field


class TimestampMixin(BaseModel):
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
