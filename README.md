# cron-test
Given a set of tasks and simulated current time, output the soonest time at which each of the commands will fire.

First, set up the virtual environment for the project:
```
python3 -m venv venv
source venv/bin/activate
```

To run the code, issue the following command:
```
./main.py HH:MM < config.txt
```

To run the test, initiate:
```
pytest -q tests.py
```
