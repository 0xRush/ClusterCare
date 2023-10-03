from apscheduler.schedulers.background import BackgroundScheduler
from .seeding_DB import seed
# days=1
# seconds=5
days=1
def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(seed, 'interval', days=1)
	scheduler.start()