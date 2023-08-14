from pydantic import BaseModel, ConfigDict, Extra


class BasePostModel(BaseModel):
    model_config = ConfigDict(extra=Extra.forbid)


class BasePatchModel(BasePostModel):
    pass
