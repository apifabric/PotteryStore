# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 19, 2024 20:58:24
# Database: sqlite:////tmp/tmp.p2YpX0lIrW-01JD33EA4TGKFTDRW87E98DGF5/PotteryStore/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Activity(SAFRSBaseX, Base):
    """
    description: Represents extra-curricular activities students can participate in
    """
    __tablename__ = 'activity'
    _s_collection_name = 'Activity'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    is_service_activity = Column(Boolean)

    # parent relationships (access parent)

    # child relationships (access children)
    StudentActivityList : Mapped[List["StudentActivity"]] = relationship(back_populates="activity")



class Artist(SAFRSBaseX, Base):
    """
    description: Represents artists whose works and classes are featured
    """
    __tablename__ = 'artist'
    _s_collection_name = 'Artist'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    bio = Column(Text)
    birth_date = Column(Date)

    # parent relationships (access parent)

    # child relationships (access children)
    ClassList : Mapped[List["Class"]] = relationship(back_populates="artist")
    ItemList : Mapped[List["Item"]] = relationship(back_populates="artist")



class Customer(SAFRSBaseX, Base):
    """
    description: Represents customers who purchase items and classes
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    balance = Column(Numeric)
    credit_limit = Column(Numeric)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")



class Student(SAFRSBaseX, Base):
    """
    description: Represents students enrolled in pottery classes
    """
    __tablename__ = 'student'
    _s_collection_name = 'Student'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    is_honor_student = Column(Boolean)

    # parent relationships (access parent)

    # child relationships (access children)
    StudentActivityList : Mapped[List["StudentActivity"]] = relationship(back_populates="student")
    EnrollmentList : Mapped[List["Enrollment"]] = relationship(back_populates="student")



class Class(SAFRSBaseX, Base):
    """
    description: Represents pottery classes offered by the store
    """
    __tablename__ = 'class'
    _s_collection_name = 'Class'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Numeric, nullable=False)
    date = Column(DateTime, nullable=False)
    artist_id = Column(ForeignKey('artist.id'))

    # parent relationships (access parent)
    artist : Mapped["Artist"] = relationship(back_populates=("ClassList"))

    # child relationships (access children)
    ClassReportList : Mapped[List["ClassReport"]] = relationship(back_populates="_class")
    EnrollmentList : Mapped[List["Enrollment"]] = relationship(back_populates="_class")



class Item(SAFRSBaseX, Base):
    """
    description: Represents handmade items sold in the store
    """
    __tablename__ = 'item'
    _s_collection_name = 'Item'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Numeric, nullable=False)
    artist_id = Column(ForeignKey('artist.id'))

    # parent relationships (access parent)
    artist : Mapped["Artist"] = relationship(back_populates=("ItemList"))

    # child relationships (access children)
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="item")



class Order(SAFRSBaseX, Base):
    """
    description: Represents orders made by customers
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    amount_total = Column(Numeric)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="order")
    OrderReportList : Mapped[List["OrderReport"]] = relationship(back_populates="order")



class StudentActivity(SAFRSBaseX, Base):
    """
    description: Represents participation of students in activities
    """
    __tablename__ = 'student_activity'
    _s_collection_name = 'StudentActivity'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey('student.id'), nullable=False)
    activity_id = Column(ForeignKey('activity.id'), nullable=False)
    participation_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    activity : Mapped["Activity"] = relationship(back_populates=("StudentActivityList"))
    student : Mapped["Student"] = relationship(back_populates=("StudentActivityList"))

    # child relationships (access children)



class ClassReport(SAFRSBaseX, Base):
    """
    description: View or report for classes, summarizing events and participation
    """
    __tablename__ = 'class_report'
    _s_collection_name = 'ClassReport'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    class_id = Column(ForeignKey('class.id'), nullable=False)
    total_students = Column(Integer)
    service_activity_count = Column(Integer)

    # parent relationships (access parent)
    _class : Mapped["Class"] = relationship(back_populates=("ClassReportList"))

    # child relationships (access children)



class Enrollment(SAFRSBaseX, Base):
    """
    description: Represents the enrollment of students to classes
    """
    __tablename__ = 'enrollment'
    _s_collection_name = 'Enrollment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    class_id = Column(ForeignKey('class.id'), nullable=False)
    student_id = Column(ForeignKey('student.id'), nullable=False)
    enrolment_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    _class : Mapped["Class"] = relationship(back_populates=("EnrollmentList"))
    student : Mapped["Student"] = relationship(back_populates=("EnrollmentList"))

    # child relationships (access children)



class OrderDetail(SAFRSBaseX, Base):
    """
    description: Represents details of each order, including purchased items
    """
    __tablename__ = 'order_detail'
    _s_collection_name = 'OrderDetail'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'), nullable=False)
    item_id = Column(ForeignKey('item.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    amount = Column(Numeric)

    # parent relationships (access parent)
    item : Mapped["Item"] = relationship(back_populates=("OrderDetailList"))
    order : Mapped["Order"] = relationship(back_populates=("OrderDetailList"))

    # child relationships (access children)



class OrderReport(SAFRSBaseX, Base):
    """
    description: View or report for orders, to keep track of total amounts
    """
    __tablename__ = 'order_report'
    _s_collection_name = 'OrderReport'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'), nullable=False)
    total_amount = Column(Numeric)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderReportList"))

    # child relationships (access children)
