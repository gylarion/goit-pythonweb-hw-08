from datetime import date, timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session

import models
import schemas


def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.Contact(**contact.model_dump())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def get_contacts(
    db: Session,
    first_name: str | None = None,
    last_name: str | None = None,
    email: str | None = None,
):
    query = select(models.Contact)

    if first_name:
        query = query.where(models.Contact.first_name.ilike(f"%{first_name}%"))
    if last_name:
        query = query.where(models.Contact.last_name.ilike(f"%{last_name}%"))
    if email:
        query = query.where(models.Contact.email.ilike(f"%{email}%"))

    return db.scalars(query.order_by(models.Contact.id)).all()


def get_contact(db: Session, contact_id: int):
    return db.get(models.Contact, contact_id)


def update_contact(
    db: Session, db_contact: models.Contact, contact: schemas.ContactUpdate
):
    for field, value in contact.model_dump().items():
        setattr(db_contact, field, value)

    db.commit()
    db.refresh(db_contact)
    return db_contact


def delete_contact(db: Session, db_contact: models.Contact):
    db.delete(db_contact)
    db.commit()
    return db_contact


def get_upcoming_birthdays(db: Session):
    today = date.today()
    last_day = today + timedelta(days=7)
    contacts = db.scalars(select(models.Contact)).all()
    upcoming_contacts = []

    for contact in contacts:
        try:
            birthday = date(
                today.year, contact.birthday.month, contact.birthday.day
            )
        except ValueError:
            birthday = date(today.year, 2, 28)

        if birthday < today:
            try:
                birthday = date(
                    today.year + 1,
                    contact.birthday.month,
                    contact.birthday.day,
                )
            except ValueError:
                birthday = date(today.year + 1, 2, 28)

        if today <= birthday <= last_day:
            upcoming_contacts.append(contact)

    return upcoming_contacts
