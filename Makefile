PROJECT = blogpost
REFERENCES = references.bib
FIGSDIR = figs
FIGURES := $(wildcard $(FIGSDIR)/*)
OUTDIR = _build

.PHONY: pdf docx html clean show serve figures

pdf: $(OUTDIR)/$(PROJECT).pdf

docx: $(OUTDIR)/$(PROJECT).docx

html: $(OUTDIR)/index.html

clean:
	rm -rf $(OUTDIR)

show: $(OUTDIR)/$(PROJECT).pdf
	xdg-open $<

serve:
	python serve.py

figures: $(FIGURES) | $(OUTDIR)/$(FIGSDIR)
	cp -r $^ $(OUTDIR)/$(FIGSDIR)

$(OUTDIR)/$(PROJECT).pdf: $(PROJECT).md | $(OUTDIR) $(REFERENCES)
	pandoc -s --bibliography $(REFERENCES) --citeproc -o $@ $<

$(OUTDIR)/$(PROJECT).docx: $(PROJECT).md | $(OUTDIR) $(REFERENCES)
	pandoc -s --bibliography $(REFERENCES) --citeproc -o $@ $<

$(OUTDIR)/index.html: $(PROJECT).md | $(OUTDIR) $(REFERENCES) figures
	pandoc -s --bibliography $(REFERENCES) --citeproc -o $@ $<

$(OUTDIR):
	mkdir $@

$(OUTDIR)/$(FIGSDIR):
	mkdir $@
