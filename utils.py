#!/usr/bin/env python

import readline
import rlcompleter
readline.parse_and_bind('tab:complete')

def suro_util_history():
    for i in range(1, readline.get_current_history_length() + 1):
        print readline.get_history_item(i)
