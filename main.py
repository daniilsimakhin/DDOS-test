import logging
import configparser
import os
import time

import requests
from peewee import *

from models import *
from thread_manager import *


def run():
    keys = [40002995, 11223344, 22334455, 55667788, 45000368]

    while True:
        for i in keys:
            #make request
            time.sleep(1)
            logging.info(i)


def database_manage():
    with db:
        db.create_tables([Device, Request])
    logging.info("Database creating")

    with db:
        first = Device(name="first", sn=45000406).save()
        second = Device(name="second", sn=11223344).save()
        third = Device(name="third", sn=22334455).save()
        fourth = Device(name="fourth", sn=55667788).save()



def init_logging():
    logging.basicConfig(
        filename='log_file.log',
        level=logging.DEBUG,
        datefmt='%H:%M:%S',
        format='[%(levelname)s]: %(message)s',
        encoding='utf-8'
    )



def create_request():
    base_dir = "/Users/Python/PycharmProjects/pythonProject/"

    config = configparser.ConfigParser()
    config.read(os.path.join(base_dir, 'config.ini'), encoding="utf-8")
    debug = config['general'].getboolean('debug')

    with db:
        devices = Device.select().where(Device.sn != 0)
        print(devices)

    url = 'https://'
    #r = requests.post(url, json={"key": "value"})
    #print(r.status_code)


if __name__ == '__main__':
    init_logging()
    #database_manage()
    create_request()
    #threaded(4, 10)

