@echo off
set PATH=%PATH%;C:\Python27\
:foo
IF %1="" GOTO finish
	python C:\download_subtitle.py %1 
	SHIFT
	GOTO foo
:finish	