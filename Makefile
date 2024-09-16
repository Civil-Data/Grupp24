default:
	pylint src/**/*.py tests/**/*.py

test:
	pytest -v

latex:
	cd report && pdflatex -shell-escape main.tex && rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk

run:
	python src/main.py
