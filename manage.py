from flask_script import Command, Manager, Option

from media_player import create_app, models, db

app = create_app()

manager = Manager(app)

@manager.option('-n', '--name', dest='name')
@manager.option('-s', '--slug', dest='slug', default=None)
def create_library(name, slug):
  lb = models.Library(name=name, slug=slug)
  db.session.add(lb)
  db.session.commit()

@manager.option('-lid', '--library_id', dest='library_id')
@manager.option('-n', '--name', dest='name', default=None)
@manager.option('-s', '--slug', dest='slug', default=None)
def create_bucket(name, slug, library_id):
  bk = models.Bucket(name=name, slug=slug, library_id=int(library_id))
  db.session.add(bk)
  db.session.commit()

@manager.option('-n', '--name', dest='name', default='joe')
@manager.option('-s', '--slug', dest='slug', default=None)
@manager.option('-src', '--source', dest='src', default=None)
@manager.option('-bid', '--bucket_id', dest='bucket_id')
def create_bucket_item(name, slug, bucket_id, src):
  bi = models.BucketItem(name=name, slug=slug, bucket_id=int(bucket_id), source_path=src)
  db.session.add(bi)
  db.session.commit()

if __name__ == "__main__":
    manager.run()