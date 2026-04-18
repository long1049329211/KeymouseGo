@echo off
REM Build KeymouseGo.exe using PyInstaller
setlocal
set PYTHON=C:\Users\Admin\AppData\Local\Python\pythoncore-3.14-64\python.exe

echo Installing/upgrading PyInstaller...
"%PYTHON%" -m pip install --upgrade pyinstaller

echo Running PyInstaller using KeymouseGo.spec...
"%PYTHON%" -m PyInstaller --noconfirm KeymouseGo.spec

echo Build finished. See dist\KeymouseGo

endlocal
pause
