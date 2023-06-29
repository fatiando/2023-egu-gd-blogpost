PROJECT = blogpost
REFERENCES = references.bib
OUTDIR = _build

pdf: $(OUTDIR)/$(PROJECT).pdf

docx: $(OUTDIR)/$(PROJECT).docx

html: $(OUTDIR)/index.html

clean:
	rm -rf $(OUTDIR)

show: $(OUTDIR)/$(PROJECT).pdf
	xdg-open $<

serve: $(OUTDIR)/index.html
	livereload --target $(OUTDIR) $(OUTDIR)


$(OUTDIR)/$(PROJECT).pdf: $(PROJECT).md | $(OUTDIR) $(REFERENCES)
	pandoc -s --bibliography $(REFERENCES) --citeproc -o $@ $<

$(OUTDIR)/$(PROJECT).docx: $(PROJECT).md | $(OUTDIR) $(REFERENCES)
	pandoc -s --bibliography $(REFERENCES) --citeproc -o $@ $<

$(OUTDIR)/index.html: $(PROJECT).md | $(OUTDIR) $(REFERENCES)
	pandoc -s --bibliography $(REFERENCES) --citeproc -o $@ $<

$(OUTDIR):
	mkdir $@
