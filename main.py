from fastapi import FastAPI, Depends
import models
from database import engine, Base ,get_db
import schemas
from sqlalchemy.orm import session


app = FastAPI()

#Create table from models
models.Base.metadata.create_all(engine)

# home page
@app.get("/home")
def root():
    return 'welcom to ESG Data et IA FastAPI Workshop'

#Add new book
@app.post("/book")
def add_book(request:schemas.book, db: session = Depends(get_db)):

    new_book = models.book (title = request.title,
                           author =  request.author,
                           description = request.description,
                           published_year = request.published_year,
                           publisher = request.publisher
                        )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book
# Retrieve a list of all books
@app.get("/books")
def get_books(db:session = Depends(get_db)):
    return db.query(models.book).all()


#Add new user
@app.post("/user")
def add_user(request:schemas.User, db: session = Depends(get_db)):

    new_user = models.User (name = request.name,
                           birthday =  request.birthday,
                           gender = request.gender,
                           email = request.email,
                           
                        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
# Retrieve a list of all user
@app.get("/user")
def get_user(db:session = Depends(get_db)):
    return db.query(models.user).all()