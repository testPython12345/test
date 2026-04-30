import logging
'''
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Это сообщение отладолчного уровня')
logging.info('Это информационное собщение о ходе выполнения программы')
logging.warning('Предупреждение')
logging.error('Сообщение об ошибке')

logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

log_file = logging.FileHandler('app.log')
log_file.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file.setFormatter(formatter)

logger.addHandler(log_file)

logger.debug('Сообщение debug')
logger.error('Ошибка')
'''
from datetime import datetime, timedelta

now = datetime.now()
print(now)

custom_time = datetime(1995, 5, 25, 14, 46, 50)
print(custom_time)

date1 = datetime(2023, 4, 14)
date2 = datetime(2024, 4, 14)
print(date1-date2)

today = datetime.today()
future = today + timedelta(10)
print(today)
print(future)
