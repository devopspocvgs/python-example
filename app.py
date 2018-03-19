import os
import flask
import MySQLdb

application = flask.Flask(__name__)
application.debug = True

@application.route('/populate')
def populate():
  storage = Storage()
  storage.populate()
  score = storage.score()
  return "Hello Devops this is production version, %d!" % score

@application.route('/liveness')
def liveness():
  storage = Storage()
  return "Container is Alive this is production version"

@application.route('/health')
def health():
  return "Healthy this is production version"


class Storage():
  def __init__(self):
    self.db = MySQLdb.connect(
      user   = os.getenv('MYSQL_USERNAME'),
      passwd = os.getenv('MYSQL_PASSWORD'),
      db     = os.getenv('MYSQL_INSTANCE_NAME'),
      host   = os.getenv('MYSQL_SERVICE_HOST'),
      port   = int(os.getenv('MYSQL_SERVICE_PORT'))
    )

    cur = self.db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS scores(score INT)")

  def populate(self):
    cur = self.db.cursor()
    cur.execute("INSERT INTO scores(score) VALUES(1234)")

  def score(self):
    cur = self.db.cursor()
    cur.execute("SELECT * FROM scores")
    row = cur.fetchone()
    return row[0]

if __name__ == "__main__":
  application.run(host='0.0.0.0', port=3000)
