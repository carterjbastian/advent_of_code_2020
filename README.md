# Instructions

You can run the challenge for any day by running:
```
python main.py <day> <part>

python main.py 1 1 # Runs part 1 of day 1
python main.py 5 2 -t # Runs the tests for part 2 of day 5
python main.py 7 3 -d # Runs parts 1 and 2 of day 7 in DEBUG mode
```

You can run the challenge for any day by running:
```
python main.py <day> <part>

python main.py 1 1 # Runs part 1 of day 1
python main.py 5 2 # Runs part 2 of day 5
python main.py 7 3 # Runs parts 1 and 2 of day 7
```


# Dev Instructions

Real inputs go into the `inputs/` directory named `{day}.txt`.
Test inputs and answers go into the `test/` directory.


```
virtualenv venv
source venv/bin/activate

# ... do some stuff... eg:
pip install -r requirements.txt
./main.py 1  # run day 1

# deactivate and clean up
deactivate
rm -rf venv
```
