#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if "sarjis" in sys.argv:
	from project.taustaprosessit.sarjis_parseri import run
	run()
	return True


if "sort" in sys.argv:
	from project. taustaprosessit.sortter import run
	run()
	return True

print "prosessi done"
return True