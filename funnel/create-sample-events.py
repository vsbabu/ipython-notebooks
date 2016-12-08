#!/usr/bin/env python
from random import randint
import datetime

#these many number of devices will get made
NUMBER_OF_DEVICES = 2000
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
#ensure you don't add commas in these.
#csv generation doesn't escape anything
FUNNEL_EVENTS = [
    'First Launch', 
    'Register Button', 
    'Provide Email', 
    'Validate Email', 
    'Terms & Conditions Show', 
    'Terms & Conditions Accept'
    ]


def make_devices(maxnum=NUMBER_OF_DEVICES):
    """
    returns a list of device ids. device ids are hard coded to be 15 digits
    """
    device_ids = []
    for i in range(maxnum):
        device_id = "%05d%05d%05d" % (randint(10000,99999),randint(10000,99999),randint(10000,99999))
        device_ids.append(device_id)
    return device_ids


def print_header():
    print "deviceid,date,event"

if __name__ == '__main__':
    device_ids = make_devices()
    print_header()
    for device_id in device_ids:
        events = FUNNEL_EVENTS[:randint(0, len(FUNNEL_EVENTS))]
        event_time = datetime.datetime.now() - datetime.timedelta(hours=randint(5,10))
        for event in events:
            print "%s,%s,%s" % (device_id, event_time.strftime(DATE_FORMAT), event)
            event_time = event_time + datetime.timedelta(minutes=randint(10,60))
        



