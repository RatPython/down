#!/usr/bin/python3

from datetime import *
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String, DateTime, Boolean, BigInteger

Base = declarative_base()


class queue(Base):
    __tablename__ = "queue"

    id = Column(BigInteger, primary_key=True)
    url = Column(String)
    size = Column(Integer)
    prior = Column(Integer)
    user = Column(String)
    passwd = Column(String)
    mirror = Column(Boolean)
    processpid = Column(Integer)
    status = Column(Integer)
    grp = Column(String)
    signkey = Column(String)
    enckey = Column(String)
    adddt = Column(DateTime)
    processbegin = Column(DateTime)
    processend = Column(DateTime)

    def __init__(self, url, size, prior=100, user='', passwd='', mirror=False, processid=-1, status=0, grp='',
                 signkey='', enckey='', adddt=datetime.today(), processbegin=datetime(1970, 1, 1),
                 processend=datetime(1970, 1, 1)):
        self.url = url
        self.size = size
        self.prior = prior
        self.user = user
        self.passwd = passwd
        self.mirror = mirror
        self.processpid = processid
        self.status = status
        self.grp = grp
        self.signkey = signkey
        self.enckey = enckey
        self.adddt = adddt
        self.processbegin = processbegin
        self.processend = processend

    def __repr__(self):
        return "queue '%s', '%s', '%s'" % (self.url, self.size, self.status)


class delqueue(Base):
    __tablename__ = "delqueue"

    id = Column(BigInteger, primary_key=True)
    fname = Column(String)
    status = Column(Integer)
    statusstr = Column(String)
    lastdt = Column(DateTime)

    def __init__(self, fname, status, statusstr, lastdt=datetime.today()):
        self.fname = fname
        self.status = status
        self.statusstr = statusstr

    def __repr__(self):
        return "delqueue '%s', '%s', '%s', '%s'" % (self.fname, self.status, self.statusstr,self.lastdt)
