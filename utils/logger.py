import os
import time

from loguru import logger

# 日志收集器
LOG_FOLDER = os.getcwd() + "/logs"
if not os.path.exists(LOG_FOLDER):
    os.mkdir(LOG_FOLDER)
t = time.strftime("%Y_%m_%d")

logger = logger
logger.add("{}/log_{}.log".format(LOG_FOLDER, t), rotation="00:00", encoding="utf-8", retention="300 days")
