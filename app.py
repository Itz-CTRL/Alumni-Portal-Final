# Tiny compatibility bootstrap so gunicorn can import `app:app`
# It simply re-exports the Flask `app` from the package module.
from shs_portal.app import app

# Optional: expose a simple healthcheck endpoint if needed
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
