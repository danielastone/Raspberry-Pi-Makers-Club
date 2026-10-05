#Testing and Evaluation Scripts
-Sensor
-Simulation

## Run the existing formula tests

Use Python 3.11–3.12, install `requirements.txt`, and run
`python -m unittest discover -s tests -v`. CI runs the same command.
The tests contain copies of notebook formulas; they do not execute the notebook
or establish physical validity, hardware integration, or calibration accuracy.
