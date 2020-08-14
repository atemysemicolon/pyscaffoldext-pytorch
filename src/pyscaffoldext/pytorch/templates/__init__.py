# -*- coding: utf-8 -*-
import os
import string
from pathlib import Path
from pkg_resources import resource_string

from .. import __version__ as pytorch_version


def get_template(name):
    """Retrieve the template by name

    Args:
        name: name of template

    Returns:
        :obj:`string.Template`: template
    """
    file_name = "{name}.template".format(name=name)
    data = resource_string(__name__, file_name)
    # we assure that line endings are converted to '\n' for all OS
    data = data.decode(encoding="utf-8").replace(os.linesep, "\n")
    return string.Template(data)


def get_src_folder(opts):
    """path of src folder relative to pyscaffold project

    Get's src folder that will constitute the (namespace) package.

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        list: path to `src` folder
    """
    if "namespace" in opts:
        path = [opts["project"], "src", opts["namespace"], opts["package"]]
    else:
        path = [opts["project"], "src", opts["package"]]
    return path


# TODO : add docstrings
def src_template(opts, subpackage, filename):
    relative_path = str(Path("lib").joinpath(subpackage).joinpath(filename))
    template = get_template(relative_path)
    return template.safe_substitute(opts)


# TODO : add docstrings
def project_root_template(opts, subpackage, filename):
    relative_path = str(Path(subpackage).joinpath(filename))
    template = get_template(relative_path)
    return template.safe_substitute(opts)


def gitignore_all(opts):
    """gitignore file that ignores just everything

    Ignore everything except of this gitignore file.

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("gitignore_all")
    return template.safe_substitute(opts)


def gitignore_data(opts):
    """gitignore file that ignores almost everything

    Ignore everything except of gitignore also in sub directories.

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("gitignore_data")
    return template.safe_substitute(opts)


def readme_md(opts):
    """Adds a basic README.md

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("readme_md")
    opts["pkg"] = opts["package"].ljust(19)
    opts["dsproject_version"] = pytorch_version
    return template.safe_substitute(opts)


# TODO: Remove
def environment_yaml(opts):
    """Environment.yaml with some basic libraries

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("environment_yaml")
    return template.safe_substitute(opts)


# TODO: Remove
def template_ipynb(opts):
    """Adds a template Jupyter notebook

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("template_ipynb")
    return template.safe_substitute(opts)


# TODO: Remove
def train_model_py(opts):
    """Adds a template python experiment

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("train_model_py")
    return template.safe_substitute(opts)
