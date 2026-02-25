from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Company, CompanySnapshot
from .seed_data import SAMPLE_COMPANY_ID, SAMPLE_DASHBOARD

app = FastAPI(title="Sector Analysis API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event() -> None:
    Base.metadata.create_all(bind=engine)
    db = next(get_db())
    try:
        company = db.query(Company).filter(Company.company_id == SAMPLE_COMPANY_ID).first()
        if company is None:
            cm = SAMPLE_DASHBOARD["company_master"]
            company = Company(
                company_id=cm["company_id"],
                company_name=cm["company_name"],
                sector=cm["sector"],
                category_tags=cm["category_tags"],
                business_model_tags=cm["business_model_tags"],
                tickers=cm["tickers"],
                primary_geographies=cm["primary_geographies"],
            )
            db.add(company)
            db.add(CompanySnapshot(company_id=SAMPLE_COMPANY_ID, payload=SAMPLE_DASHBOARD))
            db.commit()
    finally:
        db.close()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/api/companies")
def list_companies(db: Session = Depends(get_db)) -> list[dict]:
    rows = db.query(Company).all()
    return [
        {
            "company_id": row.company_id,
            "company_name": row.company_name,
            "sector": row.sector,
            "category_tags": row.category_tags,
            "tickers": row.tickers,
        }
        for row in rows
    ]


@app.get("/api/companies/{company_id}/dashboard")
def get_company_dashboard(company_id: str, db: Session = Depends(get_db)) -> dict:
    snapshot = db.query(CompanySnapshot).filter(CompanySnapshot.company_id == company_id).first()
    if snapshot is None:
        raise HTTPException(status_code=404, detail="Company snapshot not found")
    return snapshot.payload
