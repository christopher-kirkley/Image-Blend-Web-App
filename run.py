from app import create_app

app = create_app()

"""Conditional to run the application."""
if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = './uploads/'
    app.run(debug=True)

