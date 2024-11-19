# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Artist(Base):
    """description: Represents artists whose works and classes are featured"""
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    bio = Column(Text)
    birth_date = Column(Date)


class Item(Base):
    """description: Represents handmade items sold in the store"""
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Numeric, nullable=False)
    artist_id = Column(Integer, ForeignKey('artist.id'), nullable=True)


class Class(Base):
    """description: Represents pottery classes offered by the store"""
    __tablename__ = 'class'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Numeric, nullable=False)
    date = Column(DateTime, nullable=False)
    artist_id = Column(Integer, ForeignKey('artist.id'), nullable=True)


class Customer(Base):
    """description: Represents customers who purchase items and classes"""
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    balance = Column(Numeric, default=0)
    credit_limit = Column(Numeric, default=1000)


class Order(Base):
    """description: Represents orders made by customers"""
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    amount_total = Column(Numeric, default=0)


class OrderDetail(Base):
    """description: Represents details of each order, including purchased items"""
    __tablename__ = 'order_detail'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    amount = Column(Numeric, default=0)


class Student(Base):
    """description: Represents students enrolled in pottery classes"""
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    is_honor_student = Column(Boolean, default=False)


class Enrollment(Base):
    """description: Represents the enrollment of students to classes"""
    __tablename__ = 'enrollment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(Integer, ForeignKey('class.id'), nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    enrolment_date = Column(DateTime, nullable=False)


class Activity(Base):
    """description: Represents extra-curricular activities students can participate in"""
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    is_service_activity = Column(Boolean, default=False)


class StudentActivity(Base):
    """description: Represents participation of students in activities"""
    __tablename__ = 'student_activity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    participation_date = Column(DateTime, nullable=False)


class OrderReport(Base):
    """description: View or report for orders, to keep track of total amounts"""
    __tablename__ = 'order_report'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    total_amount = Column(Numeric)


class ClassReport(Base):
    """description: View or report for classes, summarizing events and participation"""
    __tablename__ = 'class_report'

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(Integer, ForeignKey('class.id'), nullable=False)
    total_students = Column(Integer)
    service_activity_count = Column(Integer)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

# Test data for Artist
artist1 = Artist(name='Alice Pot', bio='An acclaimed potter from the coastal town.', birth_date=date(1980, 5, 21))
artist2 = Artist(name='Clay Master', bio='Known for his modern art incorporating clay.', birth_date=date(1975, 8, 15))
artist3 = Artist(name='Pottery Pro', bio='Specializes in pottery classes for beginners.', birth_date=date(1985, 3, 10))
artist4 = Artist(name='Ceramic Sage', bio='A ceramic arts teacher with international exhibitions.', birth_date=date(1970, 9, 12))

# Test data for Item
item1 = Item(name='Vase', description='A beautifully crafted vase.', price=25.00, artist_id=1)
item2 = Item(name='Bowl', description='A simple yet elegant bowl.', price=15.00, artist_id=2)
item3 = Item(name='Cup', description='A ceramic cup with an artistic flair.', price=10.00, artist_id=3)
item4 = Item(name='Plate', description='A decorative plate for display.', price=20.00, artist_id=4)

# Test data for Class
class1 = Class(name='Beginners Pottery', description='A class for beginners to learn pottery basics.', price=50.00, date=date(2023, 11, 1), artist_id=3)
class2 = Class(name='Advanced Techniques', description='Masterclass on advanced pottery techniques.', price=100.00, date=date(2023, 11, 5), artist_id=1)
class3 = Class(name='Creative Sculpting', description='Explore your creative side in pottery.', price=80.00, date=date(2023, 11, 15), artist_id=2)
class4 = Class(name='Traditional Methods', description='Learn traditional pottery methods.', price=60.00, date=date(2023, 11, 20), artist_id=4)

# Test data for Customer
customer1 = Customer(name='John Doe', email='john@example.com', balance=0, credit_limit=1000)
customer2 = Customer(name='Jane Smith', email='jane@example.com', balance=0, credit_limit=1500)
customer3 = Customer(name='Alan Brown', email='alan@example.com', balance=0, credit_limit=500)
customer4 = Customer(name='Diana Green', email='diana@example.com', balance=0, credit_limit=800)

# Test data for Order
order1 = Order(customer_id=1, date=date(2023, 10, 1), amount_total=55)
order2 = Order(customer_id=1, date=date(2023, 10, 3), amount_total=20)
order3 = Order(customer_id=2, date=date(2023, 10, 13), amount_total=100)
order4 = Order(customer_id=3, date=date(2023, 10, 20), amount_total=30)

# Test data for OrderDetail
order_detail1 = OrderDetail(order_id=1, item_id=1, quantity=2, amount=50)
order_detail2 = OrderDetail(order_id=2, item_id=3, quantity=2, amount=10)
order_detail3 = OrderDetail(order_id=3, item_id=2, quantity=5, amount=75)
order_detail4 = OrderDetail(order_id=4, item_id=4, quantity=1, amount=20)

# Test data for Student
student1 = Student(name="Emma White", email="emma@example.com", is_honor_student=False)
student2 = Student(name="Lucas Blue", email="lucas@example.com", is_honor_student=False)
student3 = Student(name="Olivia Red", email="olivia@example.com", is_honor_student=False)
student4 = Student(name="Mason Black", email="mason@example.com", is_honor_student=False)

# Test data for Enrollment
enrollment1 = Enrollment(class_id=1, student_id=1, enrolment_date=date(2023, 9, 21))
enrollment2 = Enrollment(class_id=2, student_id=2, enrolment_date=date(2023, 9, 25))
enrollment3 = Enrollment(class_id=3, student_id=3, enrolment_date=date(2023, 9, 29))
enrollment4 = Enrollment(class_id=4, student_id=4, enrolment_date=date(2023, 9, 30))

# Test data for Activity
activity1 = Activity(name='Community Service', description='Helping the community through pottery.', is_service_activity=True)
activity2 = Activity(name='Exhibitions', description='Participate in national exhibitions.', is_service_activity=False)
activity3 = Activity(name='Workshops', description='Conduct workshops for pottery skills.', is_service_activity=False)
activity4 = Activity(name='Environmental Awareness', description='Pottery projects focused on environmental themes.', is_service_activity=True)

# Test data for StudentActivity
student_activity1 = StudentActivity(student_id=1, activity_id=1, participation_date=date(2023, 10, 1))
student_activity2 = StudentActivity(student_id=2, activity_id=1, participation_date=date(2023, 10, 5))
student_activity3 = StudentActivity(student_id=3, activity_id=2, participation_date=date(2023, 10, 9))
student_activity4 = StudentActivity(student_id=4, activity_id=3, participation_date=date(2023, 10, 12))


session.add_all([artist1, artist2, artist3, artist4, item1, item2, item3, item4, class1, class2, class3, class4, customer1, customer2, customer3, customer4, order1, order2, order3, order4, order_detail1, order_detail2, order_detail3, order_detail4, student1, student2, student3, student4, enrollment1, enrollment2, enrollment3, enrollment4, activity1, activity2, activity3, activity4, student_activity1, student_activity2, student_activity3, student_activity4])
session.commit()
