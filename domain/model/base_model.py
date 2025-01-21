from bson.int64 import Int64
from pydantic import BaseModel, PrivateAttr
from pydantic.fields import ModelPrivateAttr


class MyBaseModel(BaseModel):
    _coll_name: ModelPrivateAttr = PrivateAttr("")
    _default_indexes: list[] = []
    _custom_indexes: list[] = []

    @classmethod
    def getCollName(cls) -> str:
        return cls._coll_name.get_default()

    @classmethod
    def getDefaultIndexes(cls):
        return cls._default_indexes.get_default()

    @classmethod
    def getCustomIndexes(cls):
        return cls._custom_indexes.get_default()
