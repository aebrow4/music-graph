## How to run
1. Activate virtual env and `poetry install`
1. FLASK_APP=main.py flask run
1. Start neo4j on port 7687, e.g. `neo4j console`
1. Test that things are working: `curl localhost:7687/hello`

Oh, and change site-packages/neomodel/util.py from
```
from neo4j.v1 import GraphDatabase ...
```
to
```
from neo4j import GraphDatabase ...
```

