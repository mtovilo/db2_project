from msilib import Table
from tkinter import INSERT
from sqlalchemy import DateTime
from sqlalchemy import Column, VARCHAR, ForeignKey, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import DDL, event

eng_str = 'mssql+pymssql://sa:Lozinka123.@localhost/e-ticket'
engine = create_engine(eng_str)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Booking_Ticket(Base):
    __tablename__="booking_ticket"

    ticket_id=Column(Integer, primary_key = True)
    movie_name_id=Column(Integer, ForeignKey("movie_show.movie_id"), nullable=False)
    movie_date_id=Column(DateTime())
    venue = Column(Integer, nullable=False)
    payment_id=Column(Integer, ForeignKey("payment.payment_id"), nullable=False)

class Movie_Show(Base):
    __tablename__="movie_show"

    movie_id=Column(Integer, primary_key = True)
    movie_name=Column(VARCHAR(length=50), nullable=False)
    movie_language=Column(VARCHAR(length=50), nullable=False)
    movie_type=Column(VARCHAR(length=64), nullable=False)
    movie_date=Column(DateTime())

class Employee(Base):
    __tablename__="employee"

    employee_id=Column(Integer, primary_key = True)
    employee_name=Column(VARCHAR(length=30), nullable=False)
    employee_lastname=Column(VARCHAR(length=30), nullable=False)
    employee_email=Column(VARCHAR(length=64), nullable=False)
    employee_phonenumber=Column(String(length=9), nullable=False)

class Customer(Base):
    __tablename__="customer"

    customer_id=Column(Integer, primary_key = True)
    customer_name=Column(VARCHAR(length=30), nullable=False)
    customer_lastname=Column(VARCHAR(length=30), nullable=False)
    customer_mobile=Column(Integer)
    customer_email=Column(VARCHAR(length=30), nullable=False)

class Payment(Base):
    __tablename__="payment"

    payment_id=Column(Integer, primary_key = True)
    amount=Column(Float)
    date=Column(DateTime())
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable=False)

trigger = DDL('''\
CREATE TRIGGER payment_bi AFTER INSERT ON payment FOR EACH ROW
    BEGIN
        SET NEW.amount=NEW.amount*0.17
    END;''')
event.listen(payment.__table__,'after_create', trigger)



session = Session()
Base.metadata.create_all(engine)
'''session.add(Movie_Show(movie_name='Pirati s Kariba', movie_date=datetime.datetime(2022,7,22), movie_language='Engleski', movie_type='Komedija'))
session.add(Movie_Show(movie_name='Deadpool', movie_date=datetime.datetime(2022,7,22), movie_language='Engleski', movie_type='Akcija'))
session.add(Movie_Show(movie_name='Sam u kući', movie_date=datetime.datetime(2022,7,22), movie_language='Engleski', movie_type='Obiteljski film'))
session.add(Movie_Show(movie_name='Shutter Island', movie_date=datetime.datetime(2022,7,22), movie_language='Engleski', movie_type='Thriller'))

session.add(Customer(customer_name='Marija', customer_lastname='Marić', customer_mobile='063085730', customer_email='marija.maric@fpmoz.sum.ba'))
session.add(Customer(customer_name='Mihaela', customer_lastname='Tovilo', customer_mobile='063239485', customer_email='mihaela.tovilo@fpmoz.sum.ba'))
session.add(Customer(customer_name='Marija', customer_lastname='Hrkać', customer_mobile='063147852', customer_email='marija.hrkac@fpmoz.sum.ba'))
session.add(Customer(customer_name='Marina', customer_lastname='Jolić', customer_mobile='063123654', customer_email='marina.jolic@fpmoz.sum.ba'))

session.add(Payment(amount=7, date=datetime.datetime(2022,6,7), customer_id=1))
session.add(Payment(amount=3.5, date=datetime.datetime(2022,7,12), customer_id=2))
session.add(Payment(amount=5, date=datetime.datetime(2022,7,3), customer_id=3))
session.add(Payment(amount=8, date=datetime.datetime(2022,7,14), customer_id=4))

session.add(Booking_Ticket(movie_name_id=1, movie_date_id=datetime.datetime(2022,6,6), venue=2, payment_id=1))
session.add(Booking_Ticket(movie_name_id=2, movie_date_id=datetime.datetime(2022,7,10), venue=1, payment_id=2))
session.add(Booking_Ticket(movie_name_id=3, movie_date_id=datetime.datetime(2022,7,1), venue=4, payment_id=3))
session.add(Booking_Ticket(movie_name_id=4, movie_date_id=datetime.datetime(2022,6,22), venue=2, payment_id=4))'''

session.commit()