# python-template
Create a template using puthon Flask with SQLIte


export FLASK_APP='app:create_app'

flask db init

flask db migrate -m "Initial migration."

flask db upgrade
