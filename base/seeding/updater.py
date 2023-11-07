from apscheduler.schedulers.background import BackgroundScheduler
from .seeding_DB import seed
from .train import ML_train
# days=1
# seconds=5

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(seed, 'interval', seconds=60)
	scheduler.add_job(ML_train, 'interval', days=1)
	scheduler.start()