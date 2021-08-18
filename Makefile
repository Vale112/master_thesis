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

build:
	mkdir -p build/

clean:
	rm -rf build
