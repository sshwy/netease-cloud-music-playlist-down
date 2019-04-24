import json
from mess import *

with open("./config.json",'r') as load_f:
    cfg=json.load(load_f)

def info(s):
    print(INFO+s)
    with open(cfg['log_file'],'a') as log_f:
        log_f.write(s+"\n")

def warn(s):
    print(WARN+s)
    with open(cfg['log_file'],'a') as log_f:
        log_f.write(s+"\n")
    with open(cfg['log_warn_file'],'a') as log_f:
        log_f.write(s+"\n")

def err(s):
    print(ERR+s)
    with open(cfg['log_file'],'a') as log_f:
        log_f.write(s+"\n")
    with open(cfg['log_err_file'],'a') as log_f:
        log_f.write(s+"\n")

