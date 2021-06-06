from fastapi import APIRouter, Depends, Path

from mongoex.sources.dao.memo import MemoService
from mongoex.sources.dto.memo import MemoRequest, MemoUpdateRequest, MemoCreated, MemoResponse, MemoList


router_memo = APIRouter(
    prefix='/memos'
)


@router_memo.get(path='', response_model=MemoList)
async def get_memos(svc: MemoService = Depends(MemoService)):
    res = await svc.find_all()
    return {"results": res, "total": len(res)}


@router_memo.get(path='/{item_id}', response_model=MemoResponse)
async def get_memo_by_id(item_id: str = Path(None, title="메모 고유 번호"),
                         svc: MemoService = Depends(MemoService)):
    return await svc.find_by_id(item_id)


@router_memo.post(path='', response_model=MemoCreated)
async def register_memo(req: MemoRequest, svc: MemoService = Depends(MemoService)):
    row = await svc.save(req.dict())
    return {'id': row.inserted_id, 'uri': '/memos/{}'.format(row.inserted_id)}


@router_memo.patch(path='/{item_id}', response_model=MemoResponse)
async def update_memo(req: MemoUpdateRequest,
                      item_id: str = Path(None, title="메모 고유 번호"),
                      svc: MemoService = Depends(MemoService)):
    row = await svc.update(item_id, req.dict(exclude_unset=True))
    return row


@router_memo.delete(path='/{item_id}', status_code=204)
async def delete_memo(item_id: str = Path(None, title="메모 고유 번호"),
                      svc: MemoService = Depends(MemoService)):
    await svc.delete_by_id(item_id)
