#!/usr/bin/python3
"""
__init__ method for models directory to create an instance
of FileStorage class

Attributes:
    storage (ptr): an instance of FileStorage
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
