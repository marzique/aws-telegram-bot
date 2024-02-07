import os

from job_scraper_service import JobScraperService
from bot_service import BotService
from utils import json_to_markdown


def send_telegram_message(event, context):
    job_scraper_service = JobScraperService()
    jobs = job_scraper_service.get_jobs()
    for job in jobs:
        html = json_to_markdown(job)
        BotService().send_message(html, os.environ.get('CHAT_ID'))
    return "Hello from Lambda!"
