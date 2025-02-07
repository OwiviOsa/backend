import functools
import operator
from typing import List

import crud
import models
import schemas
from sqlalchemy.orm import Session


def create_club(db: Session, club: schemas.ClubCreate):
    db_club = models.Club(**club.dict())
    db.add(db_club)
    db.commit()
    db.refresh(db_club)
    return db_club


def update_club(db: Session, club_id: int, attri: dict):
    db_club: models.Club = db.query(models.Club).filter(models.Club.id == club_id).first()
    for key, value in attri.items():
        setattr(db_club, key, value)
    db.commit()
    return db_club


def get_club_by_id(db: Session, club_id: int) -> models.Club:
    db_club: models.Club = db.query(models.Club).filter(models.Club.id == club_id).first()
    return db_club


def get_clubs_by_save(db: Session, save_id: int) -> List[models.Club]:
    """
    获取存档中所有俱乐部的db实例
    """
    db_leagues = crud.get_save_by_id(db=db, save_id=save_id).leagues
    return list(functools.reduce(operator.concat, [league.clubs for league in db_leagues]))  # 这个函数好高级，我好强


"""
def get_club_by_name(db: Session, club_name: str, save_id: int):
    db_club = db.query(models.Club).filter(
        and_(models.Club.name == club_name, models.Club.league.save_id == save_id)).first()
    return db_club
"""
