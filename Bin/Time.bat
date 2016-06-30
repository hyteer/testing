@echo off

echo 取日期、时间变量值
set yy=%date:~0,4%
set mm=%date:~5,2%
set dd=%date:~8,2%
set hh=%time:~0,2%
set mn=%time:~3,2%
set ss=%time:~6,2%
set filename=%yy%%mm%%dd%%hh%%mn%%ss%.txt
echo %filename%

CMD