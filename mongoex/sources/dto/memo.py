from datetime import datetime, timezone
from pydantic import BaseConfig, BaseModel, Field
from typing import List, Optional

from . import PyObjectId, ObjectId


class MemoRequest(BaseModel):
    title: str = Field(title="메모 제목")
    body: str = Field(title="메모 내용")


class MemoUpdateRequest(BaseModel):
    title: Optional[str] = Field(title="메모 제목")
    body: Optional[str] = Field(title="메모 내용")


class MemoCreated(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, title="메모 고유번호", alias="_id")
    uri: str = Field(title="메모 접근 주소")

    class Config:
        json_encoders = {ObjectId: str}


class MemoResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, title="메모 고유 번호", alias="_id")
    title: str = Field(title="메모 제목")
    body: str = Field(title="메모 내용")

    class Config:
        allow_population_by_alias = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")
        }


class MemoList(BaseModel):
    results: List[MemoResponse] = Field(title="메모 리스트")
    total: int = Field(title="리스트 갯수")

    class Config:
        allow_population_by_alias = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")
        }
