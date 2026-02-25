from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.sql import func

from .database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(String(64), unique=True, index=True, nullable=False)
    company_name = Column(String(255), nullable=False)
    sector = Column(String(100), nullable=False)
    category_tags = Column(JSON, nullable=False)
    business_model_tags = Column(JSON, nullable=False)
    tickers = Column(JSON, nullable=False)
    primary_geographies = Column(JSON, nullable=False)


class DataSourceDocument(Base):
    __tablename__ = "data_source_documents"

    id = Column(Integer, primary_key=True)
    doc_id = Column(String(100), unique=True, index=True, nullable=False)
    company_id = Column(String(64), ForeignKey("companies.company_id"), nullable=False)
    doc_type = Column(String(64), nullable=False)
    exchange = Column(String(10), nullable=False)
    period_end = Column(Date, nullable=True)
    published_at = Column(Date, nullable=False)
    title = Column(String(500), nullable=False)
    url = Column(Text, nullable=False)
    hash = Column(String(128), nullable=True)


class Extraction(Base):
    __tablename__ = "extractions"

    id = Column(Integer, primary_key=True)
    extract_id = Column(String(100), unique=True, index=True, nullable=False)
    company_id = Column(String(64), ForeignKey("companies.company_id"), nullable=False)
    doc_id = Column(String(100), nullable=False)
    field_path = Column(String(255), nullable=False)
    value = Column(JSON, nullable=False)
    page_or_section = Column(String(255), nullable=True)
    confidence = Column(Float, nullable=False)
    notes = Column(Text, nullable=True)


class CompanySnapshot(Base):
    __tablename__ = "company_snapshots"

    id = Column(Integer, primary_key=True)
    company_id = Column(String(64), ForeignKey("companies.company_id"), unique=True, nullable=False)
    payload = Column(JSON, nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
