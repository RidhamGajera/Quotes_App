from sqlalchemy.orm import Session
from app import models, schemas
from app.core.security import get_password_hash, verify_password

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(name=user.name, email=user.email, quotes=user.quotes, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = get_user(db, user_id)
    if db_user:
        db_user.name = user_update.name
        db_user.email = user_update.email
        db_user.quotes = user_update.quotes
        if user_update.password:
            db_user.hashed_password = get_password_hash(user_update.password)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def filter_users(db: Session, name: str = None, quotes: str = None, order_by: str = None):
    query = db.query(models.User)
    if name:
        query = query.filter(models.User.name.contains(name))
    if quotes:
        query = query.filter(models.User.quotes.contains(quotes))
    if order_by == 'asc':
        query = query.order_by(models.User.name.asc())
    elif order_by == 'desc':
        query = query.order_by(models.User.name.desc())
    return query.all()
