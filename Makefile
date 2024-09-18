default:
	pylint src/**/*.py tests/**/*.py

test:
	pytest -v

latex:
	cd report && latexmk -pdf -shell-escape main.tex && latexmk -c && rm -rf _minted-main && rm -f main.bbl
clean:
	cd report && latexmk -c && rm -rf _minted-main && rm -f main.bbl

run:
	python src/main.py
