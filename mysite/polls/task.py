from celery import shared_task
  
@shared_task(bind=True)
def test_func(self):  
    for i in range(100000):
        print(i)  
    return "Completed"