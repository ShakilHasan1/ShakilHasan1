#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : MR.H2SO4 SH4K1L method>     #
# File           : run.py                             #
# Author         : Shakil                             #
# Github         : https://github.com/ShakilHasan1/           #
# Facebook       : https://www.facebook.com/Shakil.Hasan.HLT/   #
# Python version : 2.7                                #
#######################################################

import os, sys, shutil
from app import main as app

base_url = 'https://mbasic.facebook.com'
os.system('mkdir out')
os.system('mkdir dump')
if sys.version_info.major != 2:
	sys.exit('\n\033[0;91m[WARNING] Please use python 2 version\033[0m')

try: shutil.rmtree('app/__pycache__')
except: pass
try: shutil.rmtree('src/__pycache__')
except: pass

for filename in os.listdir('app'):
	if filename[-3:] == 'pyc':
		try: os.remove('app/'+filename)
		except: pass

for filename in os.listdir('src'):
	if filename[-3:] == 'pyc':
		try: os.remove('src/'+filename)
		except: pass

wkwkskkkwwk = app.Brute(base_url)
wkwkskkkwwk.start()