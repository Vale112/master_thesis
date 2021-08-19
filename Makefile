all: build/thesis.pdf


TeXOptions = -lualatex \
			 -interaction=nonstopmode \
			 -halt-on-error \
			 -output-directory=build
                                                                                
build/thesis.pdf: FORCE | build
	lualatex --output-directory=build thesis.tex
	biber --output-directory=build thesis.bcf
	lualatex --output-directory=build thesis.tex
	lualatex --output-directory=build thesis.tex
	
FORCE:
	# content/00_abstract.tex
	# content/01_einleitung.tex
	# content/02_Grundlagen.tex
	# content/03_Methoden.tex
	# content/04_Ergebnisse.tex
	# content/05_Zusammenfassung.tex
	# references.bib
	
build:
	mkdir -p build/

clean:
	rm -rf build
