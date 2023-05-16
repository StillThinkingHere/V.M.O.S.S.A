@echo off

set "filename=Pits\pit - a1\Pit-000.avo"

set /p content=<"%filename%"

if "%content%"=="True" (
    start /B "" cmd /C "pip install -r req.txt && python starter.py"
) else (
    start /B "" cmd /C "python starter.py"
)

