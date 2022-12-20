import sqlalchemy as _sql
from sqlalchemy.orm import relationship
import database as _database


class Deliverable(_database.Base):
    __tablename__ = 'deliverables'
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, index=True)
    package_id = _sql.Column(_sql.Integer,_sql.ForeignKey('packages.id'))
    delivarable  = relationship("Package", back_populates="deliverables")

class Package(_database.Base):
    __tablename__ = 'packages'
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    typeOfServiceID = _sql.Column(_sql.Integer,_sql.ForeignKey('services.id'))
    description = _sql.Column(_sql.String, index=True)
    price = _sql.Column(_sql.Integer, index=True)
    service  = relationship("Service", back_populates="packages")
    deliverables = relationship("Deliverable", back_populates="delivarable",foreign_keys=[Deliverable.package_id])

class Service(_database.Base):
    __tablename__ = "services"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, index=True)
    packages = relationship("Package", back_populates="service",foreign_keys=[Package.typeOfServiceID])

