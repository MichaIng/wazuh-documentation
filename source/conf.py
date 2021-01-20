# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# Note that not all possible configuration values are present in this
# autogenerated file. For a full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

import sys
import os
import re
import shlex
import datetime
import time
from requests.utils import requote_uri

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = u'Wazuh'
author = u'Wazuh, Inc.'
copyright = u'&copy; ' + str(datetime.datetime.now().year) + u' &middot; Wazuh Inc.'

# The short X.Y version
version = '4.0'
is_latest_release = False

# The full version, including alpha/beta/rc tags
# Important: use a valid branch (4.0) or, preferably, tag name (v4.0.0)
release = '4.0'
apiURL = 'https://raw.githubusercontent.com/wazuh/wazuh/'+release+'/api/api/spec/spec.yaml'

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks', # Sphinx built-in extension
    'sphinxcontrib.images',
    'sphinx_tabs.tabs',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

extlinks = {'api-ref': ('https://DOMAIN/user-manual/api/reference.html#%s',
                      '')}

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en-US'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'wazuh_doc_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'wazuh_web_url': 'https://wazuh.com',
    'wazuh_doc_url': 'https://documentation.wazuh.com',
    'globaltoc_depth': 5,
    'includehidden': True,
    'collapse_navigation': False,
    'prev_next_buttons_location': 'bottom'
}


# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/img/wazuh_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
if version >= '4.0':
    html_additional_pages = {
        'user-manual/api/reference': 'api-redoc.html',
    }

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If empty string, we eliminate permalinks from documentation.
# html_add_permalinks = ""

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'WazuhDocs'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'WazuhDocs.tex', u'Documentation',
   u'Wazuh, Inc.', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'wazuhdocs', u'Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'WazuhDocs', u'Documentation',
   author, 'Wazuh', 'Documentation',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html', 'not_found.html']


# -- Extension configuration -------------------------------------------------

# -- Images extension -----------------------------------------------------

images_config = {
    'default_group': 'default'
}

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Minify ------------------------------------------------------------------

extra_assets = []

def minification(actual_path):

    files = [
        ['css/style','css'],
        ['css/wazuh-icons','css'],
        ['css/custom-redoc','css'],
        ['js/version-selector','js'],
        ['js/redirects','js'],
        ['js/style','js'],
        ['js/custom-redoc','js']
    ]
    
    if is_latest_release == True:
        for asset in extra_assets:
            files.append(asset.split('.'))

    for file in files:

        path_end = actual_path+'/_static/'
        min_file = os.path.join(path_end, file[0]+'.min.'+file[1])
        minify = True
        min_file_content = ''

        if os.path.isfile(min_file):
            with open(min_file, 'r') as f_min:
                min_file_content = f_min.read()

        with open(os.path.join(path_end, file[0]+'.'+file[1]), 'r') as f:

            output = f.read()

            # remove comments - this will break a lot of hacks :-P
            output = re.sub( r'\s*/\*\s*\*/', "$$HACK1$$", output ) # preserve IE<6 comment hack
            output = re.sub( r'/\*[\s\S]*?\*/', "", output )
            output = output.replace( "$$HACK1$$", '/**/' ) # preserve IE<6 comment hack

            # url() doesn't need quotes
            output = re.sub( r'url\((["\'])([^)]*)\1\)', r'url(\2)', output )

            # spaces may be safely collapsed as generated content will collapse them anyway
            output = re.sub( r'\s+', ' ', output )

            # shorten collapsable colors: #aabbcc to #abc
            output = re.sub( r'#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3(\s|;)', r'#\1\2\3\4', output )

            # fragment values can loose zeros
            output = re.sub( r':\s*0(\.\d+([cm]m|e[mx]|in|p[ctx]))\s*;', r':\1;', output )

        if output == min_file_content:
            minify = False

        if minify:
            with open(min_file, 'w') as f2:
                f2.write(output)

# -- Versions -------------------------------------------------------------------

def customReplacements(app, docname, source):
    result = source[0]
    for key in app.config.custom_replacements:
        result = result.replace(key, app.config.custom_replacements[key])
    source[0] = result

custom_replacements = {
    "|CURRENT_MAJOR|" : "4.x",
    "|WAZUH_LATEST|" : "4.0.4",
    "|WAZUH_LATEST_ANSIBLE|" : "4.0.4",
    "|WAZUH_LATEST_KUBERNETES|" : "4.0.4",
    "|WAZUH_LATEST_PUPPET|" : "4.0.4",
    "|WAZUH_LATEST_OVA|" : "4.0.4",
    "|WAZUH_LATEST_DOCKER|" : "4.0.4",
    "|OPEN_DISTRO_LATEST|" : "1.11.0",
    "|ELASTICSEARCH_LATEST|" : "7.9.1",
    "|ELASTICSEARCH_LATEST_OVA|" : "7.9.1",
    "|ELASTICSEARCH_LATEST_ANSIBLE|" : "7.8.0",
    "|ELASTICSEARCH_LATEST_KUBERNETES|" : "7.8.0",
    "|ELASTICSEARCH_LATEST_PUPPET|" : "7.8.0",
    "|ELASTICSEARCH_LATEST_DOCKER|" : "7.9.1",
    "|OPENDISTRO_LATEST_DOCKER|" : "1.11.0",
    "|OPENDISTRO_LATEST_KUBERNETES|" : "1.11.0",
    "|DOCKER_COMPOSE_VERSION|" : "1.27.4",
    "|SPLUNK_LATEST|" : "8.0.4",
    "|WAZUH_SPLUNK_LATEST|" : "3.13.2",
    "|ELASTIC_6_LATEST|" : "6.8.8",
    "|WAZUH_REVISION_YUM_AGENT_I386|" : "1",
    "|WAZUH_REVISION_YUM_MANAGER_I386|" : "1",
    "|WAZUH_REVISION_YUM_AGENT_X86|" : "1",
    "|WAZUH_REVISION_YUM_MANAGER_X86|" : "1",
    "|WAZUH_REVISION_YUM_API_X86|" : "1",
    "|WAZUH_REVISION_YUM_AGENT_AARCH64|" : "1",
    "|WAZUH_REVISION_YUM_MANAGER_AARCH64|" : "1",
    "|WAZUH_REVISION_YUM_API_AARCH64|" : "1",
    "|WAZUH_REVISION_YUM_AGENT_ARMHF|" : "1",
    "|WAZUH_REVISION_YUM_MANAGER_ARMHF|" : "1",
    "|WAZUH_REVISION_YUM_API_ARMHF|" : "1",
    "|WAZUH_REVISION_YUM_AGENT_I386_EL5|" : "1",
    "|WAZUH_REVISION_YUM_AGENT_X86_EL5|" : "1",
    "|WAZUH_REVISION_DEB_AGENT_I386|" : "1",
    "|WAZUH_REVISION_DEB_MANAGER_I386|" : "1",
    "|WAZUH_REVISION_DEB_AGENT_X86|" : "1",
    "|WAZUH_REVISION_DEB_MANAGER_X86|" : "1",
    "|WAZUH_REVISION_DEB_API_X86|" : "1",
    "|WAZUH_REVISION_DEB_AGENT_AARCH64|" : "1",
    "|WAZUH_REVISION_DEB_MANAGER_AARCH64|" : "1",
    "|WAZUH_REVISION_DEB_API_AARCH64|" : "1",
    "|WAZUH_REVISION_DEB_AGENT_ARMHF|" : "1",
    "|WAZUH_REVISION_DEB_MANAGER_ARMHF|" : "1",
    "|WAZUH_REVISION_DEB_API_ARMHF|" : "1",
    "|WAZUH_REVISION_HPUX|" : "1",
    "|WAZUH_REVISION_OSX|" : "1",
    "|WAZUH_REVISION_WINDOWS|" : "1",
    "|WAZUH_REVISION_AIX|" : "1",
    "|CHECKSUMS_URL|" : "https://packages.wazuh.com/4.x/checksums/wazuh/",
    "|RPM_AGENT|" : "https://packages.wazuh.com/4.x/yum/wazuh-agent",
    "|RPM_MANAGER|" : "https://packages.wazuh.com/4.x/yum/wazuh-manager",
    "|DEB_AGENT|" : "https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent",
    "|DEB_MANAGER|" : "https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-manager/wazuh-manager",
    "|DEB_API|" : "https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-api/wazuh-api",
    # Variables for Elastic's Elasticsearch
    "|ELASTICSEARCH_ELK_LATEST|" : "7.9.3",
    "|ELASTICSEARCH_ELK_LATEST_ANSIBLE|" : "7.8.0",
    "|ELASTICSEARCH_ELK_LATEST_KUBERNETES|" : "7.8.0",
    "|ELASTICSEARCH_ELK_LATEST_PUPPET|" : "7.8.0",
    "|ELASTICSEARCH_ELK_LATEST_DOCKER|" : "7.8.0",
}

# -- Setup -------------------------------------------------------------------

def setup(app):

    actual_path = os.path.dirname(os.path.realpath(__file__))

    minification(actual_path)

    app.add_css_file("css/fontawesome.min.css?ver=%s" % os.stat(
        os.path.join(actual_path, "_static/css/fontawesome.min.css")).st_mtime)
    app.add_css_file("css/wazuh-icons.min.css?ver=%s" % os.stat(
        os.path.join(actual_path, "_static/css/wazuh-icons.css")).st_mtime)
    app.add_css_file("css/style.min.css?ver=%s" % os.stat(
        os.path.join(actual_path, "_static/css/style.css")).st_mtime)

    app.add_js_file("js/version-selector.min.js?ver=%s" % os.stat(
        os.path.join(actual_path, "_static/js/version-selector.js")).st_mtime)
    app.add_js_file("js/style.min.js?ver=%s" % os.stat(
        os.path.join(actual_path, "_static/js/style.js")).st_mtime)
    app.add_js_file("js/redirects.min.js?ver=%s" % os.stat(
        os.path.join(actual_path, "_static/js/redirects.js")).st_mtime)
    app.add_config_value('custom_replacements', {}, True)
    app.connect('source-read', customReplacements)

	# List of compiled documents
    app.connect('html-page-context', collect_compiled_pagename)
    app.connect('build-finished', finish_and_clean)

exclude_doc = ["not_found"]
list_compiled_html = []

def finish_and_clean(app, exception):
    ''' Performs the final tasks after the compilation '''

    # Create additional files such as the `.doclist` and the sitemap
    creating_file_list(app, exception)

    # Remove extra minified files
    for asset in extra_assets:
        mini_asset = '.min.'.join(asset.split('.'))
        if os.path.exists(app.srcdir + '/_static/' + mini_asset):
            os.remove(app.srcdir + '/_static/' + mini_asset)

    # Manage the guide-assets
    if os.path.isdir(app.outdir + '/_static/guide-assets'):
        file_names = os.listdir(app.outdir + '/_static/guide-assets')
        if is_latest_release == True:
            # Move the folder 'guide-assets' to the root folder defined as outdir
            os.mkdir(app.outdir + '/guide-assets')
            for file_name in file_names:
                os.rename(app.outdir + '/_static/guide-assets/' + file_name, app.outdir + '/guide-assets/' + file_name,)
        else:
            # Remove the folder 'guide-assets'
            for file_name in file_names:
                os.remove(app.outdir + '/_static/guide-assets/' + file_name)
            os.rmdir(app.outdir + '/_static/guide-assets')

def collect_compiled_pagename(app, pagename, templatename, context, doctree):
    ''' Runs once per page, storing the pagename (full page path) extracted from the context '''
    if templatename == "page.html" and pagename not in exclude_doc:
        list_compiled_html.append(context['pagename']+'.html')
    else:
        pass

def creating_file_list(app, exception):
    ''' Creates the files containing the path to every html file that was compiled. These files are the `.doclist` and the release sitemap. '''
    if app.builder.name == 'html':
        build_path = app.outdir
        separator = '\n'
        sitemap_version = version
        if is_latest_release == True:
            sitemap_version = 'current'
            
        # Create the release sitemap content
        sitemap = '<?xml version=\'1.0\' encoding=\'utf-8\'?>'+separator
        sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+separator
         
        for compiled_html in list_compiled_html:
            sitemap += '\t<url><loc>' + requote_uri(html_theme_options.get('wazuh_doc_url') + '/' + sitemap_version + '/' + compiled_html) + '</loc></url>' + separator
        # Close sitemap content    
        sitemap += '</urlset>'

        # Create .doclist file
        with open(build_path+'/.doclist', 'w') as doclist_file:
            list_text = separator.join(list_compiled_html)
            doclist_file.write(list_text)

        # Create release sitemap file
        with open(build_path+'/'+sitemap_version+'-sitemap.xml', 'w') as sitemap_file:
            sitemap_file.write(sitemap)

exclude_patterns = [
    "css/wazuh-icons.css",
    "css/style.css",
    "js/version-selector.js",
    "js/redirects.js",
    "js/style.js"
]

exclude_patterns = exclude_patterns + extra_assets

# -- Additional configuration ------------------------------------------------

if (tags.has("production")):
    production = True
else:
    production = False

html_context = {
    "display_github": True,
    "github_user": "wazuh",
    "github_repo": "wazuh-documentation",
    "conf_py_path": "/source/",
    "github_version": version,
    "production": production,
    "apiURL": apiURL,
    "compilation_ts": str(time.time()),
    "is_latest_release": is_latest_release
}
sphinx_tabs_nowarn = True
