from app import create_app  # Assuming your __init__.py has create_app()

# Initialize your Flask app
app = create_app()

# Vercel requires this specific variable name
handler = app
