#!/usr/bin/python3

import configparser
import sqlite3
import os.path
import os
import logging
import gnupg
import shlex
import argparse
import sys
import subprocess

import sqlalchemy
from sqlalchemy import create_engine
from db import *





#engine = create_engine('postgresql://mt:master@10.10.0.10/down')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()




