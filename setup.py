from setuptools import setup
from setuptools.extension import Extension

setup(
    ext_modules=[
        Extension(
            name="nscsv._parser",
            sources=["nscsv/_parser.c"]
        )
    ],
)
