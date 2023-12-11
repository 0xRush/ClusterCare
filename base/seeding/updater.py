from apscheduler.schedulers.background import BackgroundScheduler
from .seeding_DB import seed
from .ML_train import trainML
from .ML_predection import ML_predict
# days=1
# seconds=5

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(seed, 'interval', days=1)
	scheduler.add_job(trainML, 'interval', days=1)
	scheduler.add_job(ML_predict, 'interval',days=1)
	scheduler.start()