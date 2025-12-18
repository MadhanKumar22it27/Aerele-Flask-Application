from flask import Flask, render_template
from database import db
from routes.events import events_bp
from routes.resources import resources_bp
from routes.allocations import allocations_bp
from routes.reports import reports_bp

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scheduler.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ---------- API Blueprints ----------
app.register_blueprint(events_bp, url_prefix='/events')
app.register_blueprint(resources_bp, url_prefix='/resources')
app.register_blueprint(allocations_bp, url_prefix='/allocations')
app.register_blueprint(reports_bp, url_prefix='/reports')

# ---------- UI Routes ----------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/events-ui')
def events_ui():
    return render_template('events.html')

@app.route('/resources-ui')
def resources_ui():
    return render_template('resources.html')

@app.route('/allocate-ui')
def allocate_ui():
    return render_template('allocate.html')

@app.route('/report-ui')
def report_ui():
    return render_template('report.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
