from fastapi import APIRouter, Depends

#from database import SessionLocal
from database import get_db
from models import Question

router = APIRouter(
    prefix="/api/question",
)


#@router.get("/list")
#def question_list():
#1
#    db = SessionLocal()
#    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#    db.close()
#2
#    with get_db() as db:
#        _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#    return _question_list

@router.get("/list")
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list
