import pydantic as _pydantic


class _BaseDeliverable(_pydantic.BaseModel):
    name: str
    package_id:int

class Delivarable(_BaseDeliverable):
    id: int

    class Config:
        orm_mode = True


class CreateDeliverable(_BaseDeliverable):
    pass



class _BasePackage(_pydantic.BaseModel):
    description: str
    price: int
    typeOfServiceID: int


class Package(_BasePackage):
    id: int
    deliverables: list = []

    class Config:
        orm_mode = True


class CreatePackage(_BasePackage):
    pass


class _BaseService(_pydantic.BaseModel):
    name: str


class Service(_BaseService):
    id: int
    packages: list = []


    class Config:
        orm_mode = True


class CreateService(_BaseService):
    pass
