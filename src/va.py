from src.va.flaskr import init, register, app

def main():
    init()
    register()
    app.run(app.config["flask"]["host"], app.config["flask"]["port"])

if __name__ == "__main__":
    main()
