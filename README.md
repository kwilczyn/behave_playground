# behave_playground
This project was prepared as a playground to check Behave test framework. 
It contains a few test scenarios for testing very basic Main Google page features.
All the scenarios were written using Gherkin syntax.
The architecture of this project is based on PO pattern.

## Before you start
1. Download the latest stable build of Chromedriver and add it to the system PATH
2. Install python3 in version 3.6 or newer
3. Install all required libraries included in requirements.txt using python pip

## How to run the tests?
Run behave module in the main project directory:
```
python -m behave -D execution_delay=1 > result.txt
```
The parameter -D execution_delay is optional and is used to decrease execution speed (only to observe execution steps by humans). The value = 1 means: wait one second after each executed step. A default value of this parameter is 0.
