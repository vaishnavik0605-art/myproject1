# -- Create
# a
# database
# named
# `education_db` and create
# the
# following
# two
# tables:
# create
# database
# education_db;
# use
# education_db
# -- * Course
#
# --  `course_id` – Primary
# Key, Auto
# Increment
# --  `course_name` – NOT
# NULL, UNIQUE
# --  `duration`
# --  `fee`
# create
# table
# course(course_id
# int
# primary
# key
# auto_increment,
# course_name
# varchar(20)
# unique
# not null,
# duration
# int,
# fee
# int);
#
# INSERT
# INTO
# course(course_name, duration, fee)
# VALUES('BCA', 3, 45000),
# ('BSc CS', 3, 50000),
# ('MCA', 2, 60000),
# ('MSc CS', 2, 55000),
# ('BTech', 4, 80000);
#
# -- Student
#
# --  `student_id` – Primary
# Key, Auto
# Increment
# --  `student_name` – NOT
# NULL
# --  `email` – UNIQUE
# --  `age`
# --  `gender`
# --  `mark`
# --  `courseid` – Foreign
# Key
# referencing
# `Course(courseid)`
#
# create
# table
# student(student_id
# int
# primary
# key
# auto_increment,
# student_name
# varchar(20)
# not null,
# email
# varchar(20),
# age
# int,
# gender
# enum("female", "male"),
# mark
# int,
# courseid
# int,
# foreign
# key(courseid)
# references
# course(course_id));
#
# INSERT
# INTO
# student(student_name, email, age, gender, mark, courseid)
# VALUES
# ('Arun', 'arun@gmail.com', 20, 'male', 85, 1),
# ('Anjali', 'anjali@gmail.com', 21, 'female', 92, 1),
# ('Rahul', 'rahul@gmail.com', 22, 'male', 78, 2),
# ('Meera', 'meera@gmail.com', 20, 'female', 88, 3),
# ('Vishnu', 'vishnu@gmail.com', 23, 'male', 81, 4);
#
# INSERT
# INTO
# student
# (student_name, email, age, gender, mark, courseid)
# VALUES
# ('Akhil', 'akhil@gmail.com', 21, 'male', 80, 1);
#
# -- Insert
# records
#
# --  ### Questions
#
# -- 1.
# Write
# a
# query
# to
# display
# all
# students
# who
# scored
# more
# than * 80
# marks, ordered
# by
# mark in descending
# order.
#
# select *
# from student where
#
# mark > 80
# order
# by
# mark
# desc;
#
# -- 2.
# Write
# a
# query
# to
# find
# the
# highest
# mark, lowest
# mark, and average
# mark
# of
# all
# students.
# select
# max(mark) as highest_mark, min(mark) as lowest_mark, avg(mark) as average_mark
# from student;
#
# -- 3.
# Write
# a
# query
# to
# display
# the
# top
# 5
# students
# based
# on
# their
# marks.
# select *
# from student order
#
# by
# mark
# desc
# limit
# 5;
#
# -- 4.
# Write
# a
# query
# to
# display
# the
# names and marks
# of
# students
# whose
# age is between
# 18 and 25, ordered
# by
# age.
# select
# student_name, mark
# from student where
#
# age
# between
# 18 and 25
# order
# by
# age;
#
# -- 5.
# Write
# a
# query
# to
# find
# the
# number
# of
# students in each
# course.
# select
# course_name, count(*)
# from course group
#
# by
# course_name;
#
# -- 6.
# Write
# a
# query
# to
# display
# the
# courses
# that
# have
# more
# than
# 2
# students.
# select
# course_name, count(*)
# from student inner
#
# join
# course
# on
# student.courseid = course.course_id
# group
# by
# course_name
# having
# count(*) > 2;
#
# -- 7.
# Write
# a
# query
# to
# display
# the
# student
# name, mark, and course
# name
# using
# an
# `INNER
# JOIN
# `.
#
# select
# student_name, mark, course_name
# from student inner
#
# join
# course
# on
# student.courseid = course.course_id;
#
# -- 8.
# Write
# a
# query
# to
# display
# all
# courses and their
# students, including
# courses
# that
# have
# no
# students, using
# a
# `LEFT
# JOIN
# `.
#
# select
# course_name, student_name
# from student inner
#
# join
# course
# on
# student.courseid = course.course_id;
#
# -- 9.
# Write
# a
# query
# to
# display
# students
# whose
# marks
# are
# greater
# than
# the
# overall
# average
# mark
# using
# a
# --  subquery.
#
# select
# student_name, mark
# from student where
#
# mark > (select avg(mark)
# from student);
#
# -- 10.
# Write
# a
# query
# to
# find
# the
# second - highest
# mark and display
# the
# student
# name, mark, and course
# name
# --  using
# a
# subquery and `JOIN`.
# SELECT
# student_name, mark, course_name
# FROM
# student
# INNER
# JOIN
# course
# ON
# courseid = course_id
# WHERE
# mark = (
#     SELECT MAX(mark)
# FROM
# student
# WHERE
# mark < (SELECT MAX(mark)
# FROM
# student)
# );
#
#
#
# --  ### Git Repository Task
#
# -- 1.
# Create
# a
# new
# GitHub
# repository
# for this SQL practice task.
# -- 2.
# Create
# a
# file
# named
# `answers.sql` and write
# the
# SQL
# queries
# for all 10 questions in it.
# -- 3.
# Commit and push
# the
# file
# to
# your
# GitHub
# repository.
# -- 4.
# Make
# the
# repository
# public and share
# the
# GitHub
# repository
# link *.
# -- 5.