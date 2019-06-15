#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/15 20:29:38
# @Author  : che
# @Email   : ch1huizong@gmail.com
# bug

import os

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker


path = "/tmp"

# step1
engine = create_engine("sqlite:///:memory:", echo=False)

# step2
metadata = MetaData()

fs_table = Table(
    "fs_table",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("path", String(500)),
    Column("file", String(255)),
)
metadata.create_all(engine)

# step3
class Filesystem(object):
    def __init__(self, path, file):
        self.path = path
        self.file = file

    def __repr__(self):
        return "[Filesystem('%s', '%s')]" % (self.path, self.file)


# step4
mapper(Filesystem, fs_table)

# step5
Session = sessionmaker(bind=engine, autoflush=True)
session = Session()

# step6
for dirpath, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(dirpath, file)
        record = Filesystem(fullpath, file)
        session.save(record)

# step7
session.commit()

# step8
for record in session.query(Filesystem):
    print(
        "Database Record Number: %s, Path: %s, File: %s"
        % (record.id, record.path, record.file)
    )
