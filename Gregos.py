#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Gregos - by jero98772
from core.main import webpage
from core.main import app
def main():
	app.run(debug=True,host="127.0.0.1",port=9600)
if __name__=='__main__':
	main()