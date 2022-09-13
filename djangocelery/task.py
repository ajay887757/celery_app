from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done From task.py"


# start the celery worker by using ###   celery -A celeryProject  worker --loglevel=INFO  ## this command
