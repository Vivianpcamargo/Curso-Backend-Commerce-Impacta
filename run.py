# import os
from api import create_app
from api.model import initialize_db
from dotenv import load_dotenv
import os

load_dotenv()

flask_env = os.getenv('FLASK_ENV')
print('FLASK_ENV:' + str(flask_env))

app = create_app(flask_env)
app.app_context().push()

initialize_db.init()

app.run()
