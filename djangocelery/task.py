from celery import shared_task
import os
import logging
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s [%(lineno)d]')
from celery.utils.log import get_task_logger

logger = logging.getLogger(__name__)


logger = get_task_logger("celerycalls.log")
@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        logger.info("Logging from task.py")
        print(i)
    logger.info("Logging from task.py")
    return "Done From task.py"


# start the celery worker by using ###   celery -A celeryProject  worker --loglevel=INFO  ## this command

#documents page ###########
#1.https://dev.to/idrisrampurawala/deploying-django-with-celery-and-redis-on-ubuntu-3fo6
#2. https://stackoverflow.com/questions/41922412/error-with-gunicorn-server-start
