## How to run
1. Activate virtual env and `poetry install`
1. Start neo4j on port 7687, e.g. `neo4j console`
1. `FLASK_APP=main.py flask run`
1. Test that things are working: `curl localhost:7687/hello`
## Directory structure
```
common/
config/
graph/  # neo4j db models and data access
  models/
  data_access/
rest/         # API business logic, and schemas
  v0/...     # handler schemas
  service/   # business logic
server/  # The HTTP interface: routing, validation, server boilerplate
  handlers/
```
In general, modules in `server.handlers` should depend only on modules in `rest`.
Business logic is isolated to `rest.service` and should not leak into the data access or HTTP layers.
Modules in `rest.service` will depend on `graph.data_access`, which in turn will depend on `graph.models`.
