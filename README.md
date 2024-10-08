# Elevator optimization

[![Run Pylint](https://github.com/Civil-Data/Grupp24/actions/workflows/pylint.yml/badge.svg)](https://github.com/Civil-Data/Grupp24/actions/workflows/pylint.yml) [![Run PyTest](https://github.com/Civil-Data/Grupp24/actions/workflows/pytest.yml/badge.svg)](https://github.com/Civil-Data/Grupp24/actions/workflows/pytest.yml) [![Run build](https://github.com/Civil-Data/Grupp24/actions/workflows/run.yml/badge.svg)](https://github.com/Civil-Data/Grupp24/actions/workflows/run.yml) [![Run latex](https://github.com/Civil-Data/Grupp24/actions/workflows/latex.yml/badge.svg)](https://github.com/Civil-Data/Grupp24/actions/workflows/latex.yml)

## Description on how to run the project

1. Clone the repository:

	```sh
	git clone https://github.com/Civil-Data/Grupp24.git
	```

2. Navigate to the project directory:

	```sh
	cd Grupp24
	```

3. Install the required dependencies:

	```sh
	make install
	```

4. Run the evolutionary algorithm:

	```sh
	make run
	```

### Installation

- To install the required dependencies, run `make install`

### Run

- To run the evolutionary algorithm run `make run`

### Lint

- To lint the whole project run `make lint`

### Test

- To run the tests, run `make test`

### Generate PDF and clean files in report directory

- To generate the PDF and clean files in the report directory, run `make latex`

### Clean files in report directory

- To clean files in the report directory, run `make clean`
