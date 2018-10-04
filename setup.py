import sys
from cx_Freeze import setup, Executable
import pygame


base = None
#if sys.platform == "win32":
 #   base = "Win32GUI"

executables = [
        Executable("roleta.py" , base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["pygame"],
        include_files = ["imagens"],
        excludes = []
)




setup(
    name = "Roleta_Nutrição",
    version = "1.0",
    description = "Autores : Henrique Jorge e Walney Negreiros",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
