# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXINTL	  = sphinx-intl
PAPER         =
BUILDDIR      = build
LANGS		  = zh en

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

.PHONY: help clean html dirhtml pickle json htmlhelp qthelp latex changes linkcheck doctest gettext trans-po trans-build

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html         to make standalone HTML files"
	@echo "  dirhtml      to make HTML files named index.html in directories"
	@echo "  pickle       to make pickle files"
	@echo "  json         to make JSON files"
	@echo "  htmlhelp     to make HTML files and a HTML help project"
	@echo "  qthelp       to make HTML files and a qthelp project"
	@echo "  latex        to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  changes      to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck    to check all external links for integrity"
	@echo "  doctest      to run all doctests embedded in the documentation (if enabled)"
	@echo "  gettext      to make PO message catalogs"
	@echo "  trans-po     to make per-language message catalogs"
	@echo "  trans-build  to build documentation in all languages"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/MarineInVEST.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/MarineInVEST.qhc"

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make all-pdf' or \`make all-ps' in that directory to" \
	      "run these through (pdf)latex."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

gettext:
	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale
	@echo
	@echo "Build finished. The message catalogs are in $(BUILDDIR)/locale."

trans-po:
	for language in $(LANGS); do \
		$(SPHINXINTL) update -c source/conf.py -p $(BUILDDIR)/locale -l $$language ; \
	done;
	@echo
	@echo ".po build finished.  Per-language message catalogs saved to"
	@echo "./Locale/<lang_code>/LC_MESSAGES/*.po"
	@echo "These .po files should be sent to the translator(s) and put back"
	@echo "into their LC_MESSAGES folder when translated."

trans-build:
	for language in $(LANGS); do \
		echo "***Building docs for language $$language" ; \
		$(SPHINXINTL) build -c source/conf.py ; \
		$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) -D language=$$language $(BUILDDIR)/html_$$language ; \
	done;
	@echo
	for language in $(LANGS); do \
		echo "Language $$language built to $(BUILDDIR)/html_$$language" ; \
	done;

