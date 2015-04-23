#!/usr/bin/env python

import readline

def suro_util_history():
    for i in range(0, readline.get_current_history_length() + 1):
        print readline.get_history_item(i)
