from celery_app import celery_app

@celery_app.task(bind=True, name='demo_task')
def demo_task(self):
    print("*************hi***********************")