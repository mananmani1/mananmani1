from cx_Freeze import setup,Executable

setup(name="simple Object Detection",version="0.1", 
description="A software to detect Objects in real time",
executables =[ Executable("main.py")]
)
