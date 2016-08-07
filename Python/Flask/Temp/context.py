from first import app
from flask import current_app

app_ctx = app.app_context()
app_ctx.push()
#current_app.name

print current_app.name