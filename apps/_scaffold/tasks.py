from .common import scheduler, settings
from .models import db

# #######################################################
# Use the built-in scheduler (nothing to install)
# #######################################################


# define your tasks (or import them from other file)
def my_task(**inputs):
    print(f"task running with {inputs}")
    try:
        # do something here
        db.commit()
    except:
        # rollback on failure
        db.rollback()
    return {}


if settings.USE_SCHEDULER:
    # register your tasks with the scheduler
    scheduler.register_task("my_task", my_task)

    # enqueue runs (here or in actions) for example
    if db(db.task_run).count() < 1:
        scheduler.enqueue_run("my_task", inputs={}, timeout=2, period=10)

# manage your tasks via dashboard or Grid(path, db.task_run)

# #######################################################
# Optionally configure Celery
# #######################################################
elif settings.USE_CELERY:
    # #######################################################
    # To use celery tasks:
    # 1) pip install -U "celery[redis]"
    # 2) In settings.py:
    # USE_CELERY = True
    # CELERY_BROKER = "redis://localhost:6379/0"
    # 3) Start "redis-server"
    # 4) Start "celery -A apps.{appname}.tasks beat"
    # 5) Start "celery -A apps.{appname}.tasks worker --loglevel=info" for each worker
    # #######################################################

    from celery import Celery

    # to use "from .common import scheduler" and then use it according
    # to celery docs, examples in tasks.py
    celery_scheduler = Celery(
        "apps.%s.tasks" % settings.APP_NAME, broker=settings.CELERY_BROKER
    )

    # register your tasks
    @scheduler.task
    def my_task():
        # reconnect to database
        db._adapter.reconnect()
        try:
            # do something here
            db.commit()
        except:
            # rollback on failure
            db.rollback()

    # run my_task every 10 seconds
    celery_scheduler.conf.beat_schedule = {
        "my_first_task": {
            "task": f"apps.{settings.APP_NAME}.tasks.my_task",
            "schedule": 10.0,
            "args": (),
        },
    }
