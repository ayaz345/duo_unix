
import os

if os.environ.get('BUILDDIR'):
    build = f"{os.environ['BUILDDIR']}/tests"
else:
    build = os.path.dirname(__file__) or '.'

topbuilddir = os.path.realpath(f'{build}/..')

login_duo = os.path.realpath(f'{topbuilddir}/login_duo/login_duo')


