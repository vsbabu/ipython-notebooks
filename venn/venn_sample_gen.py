#!/usr/bin/env python
import random
# create a csv like customer name, used app
APPS = "uber ola fastcab paytm freecharge mobikwik".split()
MAX_USERS = 5
MIN_APP_PER_USER = 1

apps_len = len(APPS)
print "userid,app"
for u in range(1, MAX_USERS):
    uid = "%06d" % u
    apps = random.sample(APPS, random.randint(MIN_APP_PER_USER, apps_len))
    for a in apps:
        print "u%s,%s" % (uid, a)
