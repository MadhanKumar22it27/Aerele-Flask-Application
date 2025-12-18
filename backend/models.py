from database import db

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text)

class Resource(db.Model):
    __tablename__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)

class EventResourceAllocation(db.Model):
    __tablename__ = 'event_resource_allocations'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    resource_id = db.Column(db.Integer, db.ForeignKey('resources.id'), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('event_id', 'resource_id', name='unique_event_resource'),
    )
