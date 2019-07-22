from server.app_init import create_app
from flask import g


app = create_app()
app.run(host="0.0.0.0", debug=True)
