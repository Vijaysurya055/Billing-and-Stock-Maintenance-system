# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Import the required modules
from PyInstaller.utils.hooks import collect_all
from PyInstaller.building.api import PYZ, EXE, COLLECT

# Define the main script along with other scripts
exe = EXE(PYZ,  
          scripts=['main.py', 'admin.py', 'employee.py'],  # Define the scripts directly
          name='main',
          icon='D:/jeyam/jeyam1/jeyam_logo.ico')

# Add additional folders and their contents
coll = COLLECT(exe,
               binaries=[],
               zipfiles=[],
               datas=[('Database', 'Database'), ('fonts', 'fonts'), ('images', 'images'),('sqlite3', 'sqlite3')],
               strip=False,
               upx=True,
               name='Jeyam Department Store' )
