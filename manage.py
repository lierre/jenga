import sys

from flask.ext.script import Manager, Shell

from jenga import create_app
from jenga.extensions import db


def _make_context():
    from jenga.extensions import db
    return dict(db=db)

app = create_app()
manager = Manager(app)
manager.add_command("shell", Shell(make_context=_make_context))


@manager.command
def run():
    """Run web server for local development"""
    app.run(debug=True, host='0.0.0.0', port=8080)


@manager.command
def reset_db():
    """Reset the database"""
    print "WARNING: This will reset the database and may cause data loss."
    response = raw_input("Are you sure you want to continue? (Yes/No)")
    if not response == "Yes":
        print "Aborted."
        sys.exit()

    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    manager.run()
