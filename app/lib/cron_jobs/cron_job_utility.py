from .cron_job_helpers import CronSessionHelper

class CronJobUtility():
    def __init__(self):
        self.session = CronSessionHelper()

    