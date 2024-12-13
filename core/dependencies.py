from typing import TypeVar, Type
from fastapi import Request, Depends
from pydantic import BaseModel
from core.exceptions.http import CustomHttpException

_TModel = TypeVar("_TModel", bound=BaseModel)

def formOrJson(model: Type[_TModel]) -> _TModel:
    async def formOrJsonInner(request: Request) -> _TModel:
        type_ = request.headers["Content-Type"].split(";", 1)[0]
        if type_ == "application/json":
            data = await request.json()
        elif type_ == "multipart/form-data":
            data = await request.form()
        else:
            raise CustomHttpException(status_code=415, message="Unsupported Media Type")
        return model.model_validate(data)
    return Depends(formOrJsonInner)