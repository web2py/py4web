"""
This file defines the database models
"""

import re

from pydal.validators import IS_LENGTH, IS_NOT_EMPTY

from .common import Field, auth, db

# Cap how many tags a single post can produce.  Without this, an
# adversarial post containing thousands of ``#tags`` would create one
# row per tag.
MAX_TAGS_PER_POST = 50
# Cap each tag length to avoid storing arbitrary garbage in the index.
MAX_TAG_LENGTH = 64
TAG_PATTERN = re.compile(r"#(\w+)")

db.define_table(
    "post_item",
    Field("content", "text", requires=IS_NOT_EMPTY()),
    auth.signature,
)

db.define_table(
    "tag_item",
    Field("name", requires=IS_LENGTH(maxsize=MAX_TAG_LENGTH, minsize=1)),
    Field("post_item_id", "reference post_item"),
)


def parse_post_content(content, post_item_id):
    """Insert a (deduplicated, normalised, length-capped) tag row per
    ``#tag`` in ``content``."""
    seen = set()
    for word in TAG_PATTERN.findall(content)[:MAX_TAGS_PER_POST]:
        name = word.lower()[:MAX_TAG_LENGTH]
        if name in seen:
            continue
        seen.add(name)
        db.tag_item.insert(name=name, post_item_id=post_item_id)
