# -*- coding: utf-8 -*-
#
# Marine InVEST documentation build configuration file, created by
# sphinx-quickstart on Mon Feb  7 14:08:42 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

sys.path.append(os.path.abspath('../extensions'))
extensions = ['sphinx.ext.mathjax', 'numfig', 'json']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']
#templates_path = ['/home/swood/Desktop/marine_invest_userguide/investUGsphinx/source/.templates','.templates']
#templates_path = ['/absolute/path/to/dir/','relative/path/']

# i18n details
locale_dirs = ['locale/']
gettext_compact = False

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'InVEST'
copyright = u'2017, The Natural Capital Project'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# If we're building the docs and have knowledge of the natcap.invest package,
# use the version string.  The LT doesn't like long dev version strings, so
# we're using '+VERSION+' to denote a placeholder version string.
# If natcap.invest is not available, fall back to '+VERSION+'.
version = '3.5.0+dev'
root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..'))
try:
    from natcap.invest import __version__
    version = __version__
except ImportError:
    try:
        import subprocess
        version = subprocess.check_output(
            ['python', 'setup.py', '--version'], cwd='../../..')
    except subprocess.CalledProcessError:
        raise

# The full version, including alpha/beta/rc tags.
release = version
print ('Release: %s' % release)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
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


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'default'
html_theme = 'natcapUG'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['../themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'InVESTdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt,oneside,openany'
## THE ONESIDE AND OPENANY ARE AN UGLY HACK TO REMOVE BLANK PAGES AFTER CHAPTERS.
## ## POTENTIALLY INCOMPATIBLE WITH FUTURE VERSIONS OF SPHINX

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index',
   'InVEST_%s_Documentation.tex' % version,
   "InVEST User's Guide",
   '',  # Author looks best when blank.  List of editors, citation on next page
   'manual'),
]

rst_prolog = """
.. |invest_pdf_location| replace::
    Download PDF
__ {linktarget}
""".format(linktarget='../InVEST_%s_Documentation.pdf' % version)

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = 'title_page_images/header.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
latex_use_modindex = False

# Don't include the annoying blank pages
#latex_elements = {
#    'classoptions': ',oneside,openany'
#}
latex_elements = {
    # Instead of doing a standard sphinx titlepage, use the below.
    'maketitle': '\n'.join([
        r"\begin{center}",
        r"\vspace*{1cm}",
        r"{\Huge \textbf{InVEST User's Guide}}",
        r"",
        r"\vspace{0.5cm}",
        r"{\Large \em {Integrated Valuation of Ecosystem Services and Tradeoffs}}",
        r"",
        r"\vspace{0.25cm}",
        r"Version %s" % version,
        r"\end{center}",
        r"",
        r"\vfill",  # fill insert space between the above and the editors block
    ]),
    'tableofcontents': '',
    'fncychap': r'\usepackage[Bjarne]{fncychap}',
    'preamble': '\n'.join([
        r'\ChTitleVar{\Huge\rm\raggedright}',
        r'\pdfpxdimen=1in',
        r'\divide\pdfpxdimen by 96',
    ])
}
