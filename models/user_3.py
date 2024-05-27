#!/usr/bin/python3

import hashlib
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new User instance"""
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = self.hash_password(kwargs['password'])

    def __setattr__(self, name, value):
        """Sets attribute to a new value, hashing password if necessary"""
        if name == "password":
            value = self.hash_password(value)
        super().__setattr__(name, value)

    def hash_password(self, password):
        """Hashes a password using MD5"""
        return hashlib.md5(password.encode()).hexdigest()
