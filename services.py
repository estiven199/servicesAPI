from typing import TYPE_CHECKING, List
from fastapi import HTTPException
import database as _database
import models as _models
import schemas as _schemas
from sqlalchemy.orm import aliased

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_service(service: _schemas.CreateService, db: "Session") -> _schemas.Service:
    service = _models.Service(**service.dict())
    db.add(service)
    db.commit()
    db.refresh(service)
    return _schemas.Service.from_orm(service)


async def create_package(package: _schemas.CreatePackage, db: "Session"):
    package = _models.Package(**package.dict())
    service_type = db.query(_models.Service).get(package.typeOfServiceID)
    if service_type is None:
        raise HTTPException(status_code=404, detail="Service type not found")
    db.add(package)
    db.commit()
    db.refresh(package)
    return _schemas.Package.from_orm(package)


async def create_deliverable(deliverable: _schemas.CreateDeliverable, db: "Session"):
    deliverable = _models.Deliverable(**deliverable.dict())
    package = db.query(_models.Package).get(deliverable.package_id)
    if package is None:
        raise HTTPException(status_code=404, detail="Package type not found")
    db.add(deliverable)
    db.commit()
    db.refresh(deliverable)
    return _schemas.Delivarable.from_orm(deliverable)


async def get_all_service(db: "Session") -> List[_schemas.Service]:
    Service = aliased(_models.Service)
    Package = aliased(_models.Package)
    Deliverable = aliased(_models.Deliverable)

    services = (
        db.query(Service, Package, Deliverable)
        .outerjoin(Package, Service.id == Package.typeOfServiceID)
        .outerjoin(Deliverable, Package.id == Deliverable.package_id)
        .all())

    services_list = []

    # Recorremos los resultados de la consulta
    for service, package, deliverable in services:
        # Si aún no tenemos un diccionario para el servicio, creamos uno
        if service.id not in [s["id"] for s in services_list]:
            services_list.append({
                "id": service.id,
                "name": service.name,
                "packages": []
            })

    # Si aún no tenemos un diccionario para el paquete, creamos uno
        if package and package.id not in [p["id"] for p in services_list[-1]["packages"]]:
            services_list[-1]["packages"].append({
                "id": package.id,
                "description": package.description,
                "price": package.price,
                "deliverables": []
            })
        # Si tenemos información del paquete, añadimos el entregable a la lista de entregables del paquete
        if deliverable:
            services_list[-1]["packages"][-1]["deliverables"].append({
                "id": deliverable.id,
                "name": deliverable.name
            })

    return services_list


async def get_service(service_id: int, db: "Session"):
    service = db.query(_models.Service).filter(
        _models.Service.id == service_id).first()
    return service
