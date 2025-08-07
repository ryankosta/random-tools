#!/bin/env python3
import os
import sys

def check_sudo():
    if os.geteuid() != 0:
        print("This script must be run as root (sudo).")
        sys.exit(1)

NUM_CPU=os.cpu_count()
def get_scaling_dir(cpunum:int):
    return f"/sys/devices/system/cpu/cpu{cpunum}/cpufreq/scaling_governor"
def check_setup():
    if not os.path.isfile(get_scaling_dir(0)):
        print("WARN: Power scaling settings not properly configured (ie: cpufreq directory DNE)")
        exit()

        
def set_all():
    for cpunum in range(NUM_CPU):
        cmd = "echo performance > " + get_scaling_dir(cpunum)
        os.system(cmd)
check_sudo()
check_setup()
set_all()
