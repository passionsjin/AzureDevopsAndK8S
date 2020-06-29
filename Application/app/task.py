from celery import shared_task


@shared_task
def asyn_sleep(sec):
    count = 0
    for i in range(10000000 * sec):
        count += 1
    return count


# @shared_task
# def simple_task():
