"""
File:           config.py
Created on:     08/01/2021, 19:44
"""
import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', 'renad')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'renadpass')
DB_NAME = os.getenv('DB_NAME', 'capstone')
SQLALCHEMY_DATABASE_URI = "postgres://enfhffpzheqmni:345d59e638253aa6949ebc7d28c23056213e9c6127258898862ad46f7f5390b6@ec2-18-235-107-171.compute-1.amazonaws.com:5432/d592s45o64pojn"