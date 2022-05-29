from services.server import initalize_server

app = initalize_server()

if __name__ == "__main__":
    app.run()