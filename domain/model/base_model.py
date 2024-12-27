from bson.int64 import Int64
from pydantic import BaseModel, PrivateAttr
from pydantic.fields import ModelPrivateAttr


class _MyBaseModel_Index(BaseModel):
    """
    this attributes is same as pymongo.collection.Collection.create_index() args
    """

    keys: list[tuple] = []
    unique: bool = False


class MyBaseModel(BaseModel):
    """
    id field already indexed by default, but it need to be indexed manually if you set the _indexes field.
    """

    _coll_name: ModelPrivateAttr = PrivateAttr("")

    _default_indexes: list[_MyBaseModel_Index] = [
        _MyBaseModel_Index(keys=[("id", 1)], unique=True)
    ]
    _custom_indexes: list[_MyBaseModel_Index] = []

    @classmethod
    def getCollName(cls) -> str:
        return cls._coll_name.get_default()

    @classmethod
    def getDefaultIndexes(cls):
        return cls._default_indexes.get_default()

    @classmethod
    def getCustomIndexes(cls):
        return cls._custom_indexes.get_default()