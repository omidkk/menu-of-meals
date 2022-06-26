import sys

from app.create_app import create_app

sys.path.append("./app")

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
