"""Compatibility bootstrap for deployments.

Some hosts or start commands expect a top-level module named `app`.
This file re-exports the Flask application defined in `shs_portal/app.py`.
It also ensures the project root is on sys.path so imports work reliably.
"""
import os
import sys

# Ensure repo root is on sys.path (defensive for some hosts)
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

try:
    # Preferred: import the application object from the package
    from shs_portal.app import app  # type: ignore
except Exception as e:
    # Helpful runtime message when import fails
    raise RuntimeError(f"Failed to import shs_portal.app: {e}")


if __name__ == '__main__':
    # Run the development server when executed directly
    app.run(host='0.0.0.0', debug=True)
