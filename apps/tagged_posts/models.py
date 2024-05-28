"""
This file defines the database models
"""

from .common import db, Field, auth
from pydal.validators import *
import re

db.define_table(
    "post_item",
    Field("content", "text"),
    auth.signature)

db.define_table(
    "tag_item",
    Field("name"),
    Field("post_item_id", "reference post_item")
)    

def parse_post_content(content, post_item_id):
    for word in re.compile("\#\w+").findall(content):
        db.tag_item.insert(name=word[1:], post_item_id=post_item_id)    
        

