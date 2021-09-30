## Project Description
This project was developed to build a Command Line Interface (CLI) tool in python that will provide foreign exchange rates using the Frankfurter API. The CLI tool will provide historical exchange rates between a base and multiple quote currencies as well as exchange rate conversions for specific currency, amount and date.

## Tool Description and commands
The tool contains two commands: history and convert.

The history command uses start date, end date, base, symbol and output parameters. This command will send an API request to Frankfurter and provide the exchange rates for the specified date duration, provided base and symbol (quote currency). If the dates are not provided, today's day will be used as default. 
The base by default is 'USD' and the symbol is a required parameter. If the output parameter is not provided the output will be displayed on the console.
This command will be invoked as shown in the below example:

Example 1:

`exrates history --start 2021-09-02 --end 2021-09-04 --symbol INR`

The result is displayed as a JSON:

`{"date": "2021-09-02", "base": "USD", "symbol": "INR", "rate": 73.037}
{"date": "2021-09-03", "base": "USD", "symbol": "INR", "rate": 73.029}
`
Example 2:

`exrates history --start 2021-09-02 --end 2021-09-04 --symbol INR --output file_output.txt`

The result is written to the file 'file_output.txt' and is created in the folder where the app is installed.

The convert command uses start date, base, amount and symbol parameters. This command will send an API request to Frankfurter and provide the forex converted amount for the specified date, base, symbol and amount. If the date is not provided, today's day will be used by default. The base by default is 'USD' and the symbol and amount are required parameters.
This command will be invoked as shown in the below example:

Example:

`exrates convert --symbol INR --amount 10`

The result is displayed as shown below:

`{"date": "2021-09-29", "base": "USD", "symbol": "INR", "rate": 741.95}`

## Initial Steps
Initial setup requires the below installation. 
1. click - `pip install click` Click integration and setting up commands to add to our tool
2. setuptools - `pip install setuptools` setuptools is a library we use to package our tool
3. twine - `pip install twine' twine is used for distributing the packages to pypi/test.pypi
4. virtualenv - `pip install virtualenv` virtualenv is an isolated python env where we run out tools and scripts.
5. wheel - `pip install wheel` wheel is used for packaging python tools and packages

For building this Command Line tool I used Click which is a Python package for creating command line interfaces. I also used the setuptools library which was used for packaging and distributing the tool. 

I created a `setup.py` file which includes the setup configuration including the entry_points parameter which identifies the python script - `FX_Rate_tool.py` that contains the main tool logic. This file tells the setuptools how to package the tool.

## Testing the tool
In the terminal I created the virtual environment by typing `virtualenv venv`. 
I activated the virtual env with `source venv\bin\activate`. 
I installed the tool in the venv using `python setup.py develop`. This installs the CLI tool to the virtual environment. This can be tested by typing `exrates history --help` command in the terminal.

## Packaging and Distribution
I used wheel which is a built-package format.`pip install wheel`
Running the below command packages the setuptools for distribution
`python setup.py sdist bdist_wheel`

This command creates a folder dist in the directory. Along with .whl, .egg-info and a .tar.gz files.
For the next steps, I uploaded the binaries to the test environment in https://test.pypi.org. I created an account in https://test.pypi.org and uploaded the binaries using twine. `pip install twine` 
 `twine upload --repository testpypi --skip-existing dist/*`

## Installing and Deploying the tool
Finally, a global link will be created which we can use to run the command from anywhere now. We can use the below command to install the tool
`pip install -i https://test.pypi.org/simple/ FX-Rate-tool==0.0.4`
  

