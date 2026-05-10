"""
Celery tasks for tagged_posts.

To enable:
1) pip install -U "celery[redis]"
2) In settings.py: USE_CELERY = True and CELERY_BROKER = "redis://localhost:6379/0"
3) Start "redis-server"
4) Start "celery -A apps.{appname}.tasks beat"
5) Start "celery -A apps.{appname}.tasks worker --loglevel=info" for each worker

The module guards every call against ``settings.USE_CELERY`` so it can
be imported safely when Celery is disabled (the default).
"""

from .common import db, settings

if settings.USE_CELERY:
    from celery import Celery

    scheduler = Celery(
        "apps.%s.tasks" % settings.APP_NAME, broker=settings.CELERY_BROKER
    )

    @scheduler.task
    def my_task():
        try:
            # The worker runs in its own thread, so it needs its own
            # database connection.
            db._adapter.reconnect()
            # do something here
            db.commit()
        except Exception:
            db.rollback()

    # Run my_task every 10 seconds.
    scheduler.conf.beat_schedule = {
        "my_first_task": {
            "task": "apps.%s.tasks.my_task" % settings.APP_NAME,
            "schedule": 10.0,
            "args": (),
        },
    }

