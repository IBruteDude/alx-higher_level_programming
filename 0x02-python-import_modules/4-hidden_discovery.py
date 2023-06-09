#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
	dirnames = dir(hidden_4)
	for i in dirnames:
		if i[:2] != '__':
			print(i)