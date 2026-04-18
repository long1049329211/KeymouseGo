# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
import os

datas = [('assets', 'assets'), ('assets_rc.py', '.')]
# 尝试定位 pywin32_system32 中的 DLL（兼容不同安装位置）
pywin32_dlls = []
try:
    import pywintypes
    dll_dir = os.path.dirname(pywintypes.__file__)
    # pywintypes may be a DLL; try pywin32_system32 sibling
    candidate = os.path.join(os.path.dirname(dll_dir), 'pywin32_system32')
    if os.path.isdir(candidate):
        pywin32_dlls = [
            (os.path.join(candidate, 'pywintypes314.dll'), '.'),
            (os.path.join(candidate, 'pythoncom314.dll'), '.')
        ]
except Exception:
    # 回退到常见安装路径（在此环境中发现）
    candidate = r'D:\Assembly\pythonpip\pywin32_system32'
    if os.path.isdir(candidate):
        pywin32_dlls = [
            (os.path.join(candidate, 'pywintypes314.dll'), '.'),
            (os.path.join(candidate, 'pythoncom314.dll'), '.')
        ]

binaries = pywin32_dlls
hiddenimports = ['win32api', 'win32con']
tmp_ret = collect_all('PySide6')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['KeymouseGo.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='KeymouseGo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='KeymouseGo',
)
