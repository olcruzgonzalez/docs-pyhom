# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import pathlib
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
import datetime



# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PyHom'
author = 'Oscar L. Cruz Gonzalez'
current_year = datetime.datetime.now().year
if current_year==2023:
    copyright = '2023, Oscar L. Cruz Gonzalez'
else:
    copyright = f'2023-{current_year}, Oscar L. Cruz Gonzalez'
version= '1.0'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title= 'pyhom - pyhom 1.0 documentation'
html_short_title= 'Documentation'

#html_logo = 'Logo_HTML.svg'
html_favicon = 'images/favicon.svg'


#--------------------------------
html_theme = 'furo'

html_static_path = ['_static']
html_theme_options = {
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
   #"announcement": "<em>Important</em> announcement!",

   "light_logo": "White_Logo.svg",
    "dark_logo": "Black_Logo.svg",

    

    
}


#--------------------------------


