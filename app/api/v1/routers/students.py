from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.schemas.student import StudentCreate, StudentUpdate, StudentOut
from app.crud import student as crud_student
from app.api import deps

router = APIRouter()

@router.get("/", response_model=dict)
def read_students(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(deps.get_db)
):
    skip = (page - 1) * page_size
    total = crud_student.count_students(db)
    students = crud_student.get_students_paginated(db, skip=skip, limit=page_size)
    
    students_out = [StudentOut.from_orm(s) for s in students]
    
    total_pages = (total + page_size - 1)
    
    return {
        "data": students_out,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
        "total_items": total,
    }


@router.get("/{student_id}", response_model=StudentOut)
def read_student(student_id: int, db: Session = Depends(deps.get_db)):
    student = crud_student.get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/", response_model=StudentOut, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db: Session = Depends(deps.get_db)):
    return crud_student.create_student(db, student)

@router.put("/{student_id}", response_model=StudentOut)
def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(deps.get_db)):
    updated_student = crud_student.update_student(db, student_id, student)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@router.delete("/{student_id}", response_model=StudentOut)
def delete_student(student_id: int, db: Session = Depends(deps.get_db)):
    deleted_student = crud_student.delete_student(db, student_id)
    if not deleted_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return deleted_student
