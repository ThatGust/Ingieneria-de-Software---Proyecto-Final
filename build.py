#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

name = "Ingieneria-de-Software---Proyecto-Final"
version = "1.0"
summary = "Example PyBuilder / Git project"
url     = "https://github.com/ThatGust/Ingieniera-de-Software---Proyecto-Final"

description = """Proyecto final de Ingenieria de Software."""

authors      = [Author("ThatGust", "alvaro.cano.luque@gmail.com")]
license      = "None"
default_task = "publish"

@init
def initialize(project):
    project.build_depends_on("flask")
    project.build_depends_on("flask_bootstrap")
    project.build_depends_on("flask_wtf")
    project.build_depends_on("wtforms")
    project.build_depends_on("flask_sqlalchemy")
    project.build_depends_on("werkzeug")
    project.build_depends_on("flask_login")
    project.build_depends_on("numpy")
    project.set_property('coverage_break_build', False)

@init
def set_properties(project):
    pass
