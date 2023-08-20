from pydantic import BaseModel, ConfigDict, Extra
from pydantic.alias_generators import to_camel


class BaseResponseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )


class BasePostModel(BaseResponseModel):
    model_config = ConfigDict(
        extra=Extra.forbid,
    )


class BasePatchModel(BasePostModel):
    pass
