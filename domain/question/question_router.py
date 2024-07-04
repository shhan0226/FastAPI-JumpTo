from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

#1번 방법
#from database import SessionLocal

#2번 방법
from database import get_db
from models import Question

from domain.question import question_schema
from typing import List

router = APIRouter(
    prefix="/api/question",
)

# 1번 방법
# @router.get("/list")
# def question_list():
#     db = SessionLocal()
#     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     db.close()
#     return _question_list

# 2번 방법
# @router.get("/list")
# def question_list():
#     with get_db() as db:
#         _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     return _question_list

# 3번 방법
# @router.get("/list")
# def question_list(db: Session = Depends(get_db)):
#     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     return _question_list


# 4번 방법
@router.get("/list", response_model=List[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list

