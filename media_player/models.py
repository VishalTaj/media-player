"""Data models."""

from . import db
from datetime import datetime

class Bucket(db.Model):
  """Data Model for Folder"""


  __tablename__ = 'buckets'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), index=False, unique=True, nullable=False)
  slug = db.Column(db.String(64), index=True, unique=True, nullable=False)
  created = db.Column(db.DateTime, index=False, unique=False, nullable=True, default=datetime.now())
  updated = db.Column(db.DateTime, index=False, unique=False, nullable=True, default=datetime.now())
  library_id = db.Column(
      db.Integer,
      db.ForeignKey('libraries.id', ondelete='CASCADE'),
      nullable=False,
      # no need to add index=True, all FKs have indexes
  )
  library = db.relationship('Library', backref='buckets')
  
  def __repr__(self):
    return '<Bucket {}>'.format(self.name)


class BucketItem(db.Model):
  """Data Model for Folder"""


  __tablename__ = 'bucket_items'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), index=False, unique=True, nullable=False)
  slug = db.Column(db.String(64), index=True, unique=True, nullable=False)
  created = db.Column(db.DateTime, index=False, unique=False, nullable=True, default=datetime.now())
  updated = db.Column(db.DateTime, index=False, unique=False, nullable=True, default=datetime.now())
  source_path = db.Column(db.String(255), index=False, unique=False, nullable=True)
  bucket_id = db.Column(
        db.Integer,
        db.ForeignKey('buckets.id', ondelete='CASCADE'),
        nullable=False,
        # no need to add index=True, all FKs have indexes
    )
  bucket = db.relationship('Bucket', backref='bucket_items')
  created = db.Column(db.DateTime, index=False, unique=False, nullable=True)

  def __repr__(self):
    return '<BucketItem {}>'.format(self.name)

class Library(db.Model):
  """
    Data Model for Category this holds
    the buckets
  """


  __tablename__ = 'libraries'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), index=False, unique=True, nullable=False)
  slug = db.Column(db.String(64), index=True, unique=True, nullable=False)
  created = db.Column(db.DateTime, index=False, unique=False, nullable=True, default=datetime.now())
  updated = db.Column(db.DateTime, index=False, unique=False, nullable=True, default=datetime.now())
  
  def __repr__(self):
    return '<Library {}>'.format(self.name)