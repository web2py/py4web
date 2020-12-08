from datetime import datetime, timedelta


class DBStore:
    def __init__(self, db, name="py4web_session"):
        self.__prerequisites__ = [db]
        Field = db.Field
        self.db = db
        if not name in db.tables:
            db.define_table(
                name,
                Field("rkey", "string"),
                Field("rvalue", "text"),
                Field("expiration", "integer"),
                Field("created_on", "datetime"),
                Field("expires_on", "datetime"),
            )
            db.commit()
        self.table = db[name]

    def get(self, key):
        db, table, now = self.db, self.table, datetime.utcnow()
        row = db(table.rkey == key).select().first()
        if not row:
            return None
        if row.expiration:
            row.update_record(expires_on=now + timedelta(row.expiration))
        return row.rvalue

    def set(self, key, value, expiration=None):
        db, table, now = self.db, self.table, datetime.utcnow()
        db(table.expires_on < now).delete()
        row = db(table.rkey == key).select().first()
        expires_on = (
            now + timedelta(expiration) if expiration else datetime(2999, 12, 31)
        )
        if row:
            row.update_record(
                rvalue=value, expires_on=expires_on, expiration=expiration
            )
        else:
            table.insert(
                rkey=key,
                rvalue=value,
                expires_on=expires_on,
                expiration=expiration,
                ceated_on=None,
            )
        db.commit()
