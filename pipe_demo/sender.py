#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This code sends a message on a pipe, then it waits the return message and print it
from subprocess import PIPE,Popen
pipe = Popen('./receiver.py',shell=True,stdin=PIPE,stdout=PIPE)
payload_message="passed by the sender to the receiver"
pipe.stdin.write(payload_message+"\n")
pipe.stdin.flush()
print pipe.stdout.readline(),
