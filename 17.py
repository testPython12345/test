import logging
import datetime
import os
import multiprocessing
import time

tasks_file = 'tasks.txt'
log_file = 'log1.txt'

logging.basicConfig(
    filename = log_file,
    level = logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

def write_task_to_file():
    while True:
        try:
            print('Добавление задачи:')
            task_time = input('Введите время (HH:MM): ').strip()
            date = input('Введите дату (YYYY-MM-DD): ').strip()
            desc = input('Введите описание: ').strip()
            fulltime = datetime.datetime.strptime(f'{date} {task_time}', '%Y-%m-%d %H:%M')
            with open(tasks_file, 'a', encoding='utf-8') as file:
                file.write(f'{fulltime.strftime('%Y-%m-%d %H:%M')} -> {desc}\n')
            print('Задача добавлена успешно!')
            logging.info(f'Пользователь добавил задачу: {desc}')
        except ValueError:
            print(f'Ошибка формата даты и времени! {ValueError}')
            logging.error(f'Пользователь ввел неверно дату и время для задачи: {desc}')
        except Exception as e:
            print(f'Ошибка: {e}')
            logging.error(f"Ошибка при добавлении задачи: {e}")


def show_tasks():
    while True:
        try:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            with open(tasks_file, 'r', encoding='utf-8') as file:
                if file:
                    tasks = file.readlines()
                    for task in tasks:
                        task_data = task.split(' -> ')[0]
                        if task_data == now:
                            print('\n'+task)
                            time.sleep(30)
                else:
                    pass
        except Exception as e:
            print(f'Ошибка: {e}')
            logging.error("Ошибка при чтении файла")

def main():
    logging.info('Программа запущена!')
    if not os.path.exists(tasks_file):
        open(tasks_file, 'w', encoding='utf-8').close()
        logging.info('Файл создан успешно!')
    show_process = multiprocessing.Process(target=show_tasks)
    show_process.start()
    write_task_to_file()

if __name__ == '__main__':
    main()