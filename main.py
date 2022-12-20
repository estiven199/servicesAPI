from typing import TYPE_CHECKING
import fastapi as _fastapi
import schemas as _schemas
import services as _services
from fastapi import Depends
from sqlalchemy.orm import Session
import fastapi as _fastapi
import sqlalchemy.orm as _orm



if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.post("/servicies", response_model=_schemas.Service)
async def create_service(
        service: _schemas.CreateService,
        db=_fastapi.Depends(_services.get_db)):
    return await _services.create_service(service=service, db=db)


@app.post("/packages")
async def create_package(package: _schemas.CreatePackage, db: "Session" = Depends(_services.get_db)):
    print(package)
    return await _services.create_package(package=package, db=db)


@app.post("/deliverables", response_model=_schemas.Delivarable)
async def create_deliverable(
        deliverable: _schemas.CreateDeliverable,
        db =_fastapi.Depends(_services.get_db)):
    return await _services.create_deliverable(deliverable=deliverable, db=db)


@app.get("/servicies")
async def get_all_service(db: "Session" = Depends(_services.get_db)):
    return await _services.get_all_service(db=db)


@app.get("/services/{service_id}/", response_model=_schemas.Service)
async def get_service(
    service_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    service = await _services.get_service(db=db, service_id=service_id)
    if service is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="Service does not exist")

    return service
