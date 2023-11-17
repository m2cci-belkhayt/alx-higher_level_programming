#!/usr/bin/python3
# test_base.py
"""Defines unittests for base.py.
"""
import os
import unittest
from models.base import Base

def test_id_increment(self):
    base1 = Base()
    base2 = Base()
    self.assertEqual(base1.id, base2.id - 1)
    self.assertEqual(base2.id, base1.id + 1)

def test_custom_id(self):
    base_with_id = Base(5)
    self.assertEqual(base_with_id.id, 5)