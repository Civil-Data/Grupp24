default:
	make check
	make run

run:
	python src/main.py

check:
	make test
	make lint

lint:
	pylint src/**/*.py tests/**/*.py

test:
	pytest -v

latex:
	cd report && latexmk -pdf -shell-escape -interaction=nonstopmode main.tex
	make clean

clean:
	cd report && latexmk -c && rm -rf _minted-main && rm -f main.bbl && rm -f main.synctex.gz

install:
	pip install -r requirements.txt

update:
	pip freeze > requirements.txt

experiment:
	python src/experiment/create_experiment.py

experiment-clean:
	rm buildings/*
	rm generations/*
