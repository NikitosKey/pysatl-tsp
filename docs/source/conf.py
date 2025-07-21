import os
import sys
sys.path.insert(0, os.path.abspath('../../pysatl_tsp/'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PySATL-TSP'
copyright = '2025, PySATL Authors'
author = 'PySATL Authors'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "autodoc2",
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

autodoc2_packages = [
    "../../pysatl_tsp",
]


# -- sphinx-autodoc2 settings ------------------------------------------------
autodoc2_sort_names = True 
autodoc2_sort_annotations = True
autodoc2_set_add_module_names = False 
autodoc2_set_typehints_format = "short" 
autodoc2_set_typehints_role = "obj"
autodoc2_set_show_inheritance = True 
autodoc2_set_hide_base_class_rtype = True
autodoc2_set_private_member_filter = False 
autodoc2_set_special_member_filter = ["__init__", "__call__"] 


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme_options = {
    'collapse_navigation': False,   
    'sticky_navigation': True,     
    'navigation_depth': 6,        
                                 
    'includehidden': True,      
    'style_external_links': True,
    'style_nav_header_background': '#2980B9',
}
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
