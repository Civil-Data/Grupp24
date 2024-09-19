default:
	pylint src/**/*.py tests/**/*.py

test:
	pytest -v

latex:
	cd report && latexmk -pdf -shell-escape main.tex
	make clean

clean:
	cd report && latexmk -c && rm -rf _minted-main && rm -f main.bbl && rm -f main.synctex.gz

run:
	python src/main.py

install:
	pip install -r requirements.txt
