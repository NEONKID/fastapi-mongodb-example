from typing import Optional

from mongoex.sources.models.mixin import TimestampMixin


class MemoBase(TimestampMixin):
    id: Optional[int] = None
    title: str
    body: str
