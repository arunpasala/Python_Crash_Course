from pathlib import Path
import json

path = Path('Storing_Data/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)