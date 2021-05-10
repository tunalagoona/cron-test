# cron-test
Given a set of tasks, each running at least daily and simulated current time, output the soonest time at which each of the commands will fire
    
Run the command like this:
```
./main.py HH:MM < config.txt
```

To run the test, initiate:
```
pytest -q tests.py
```
