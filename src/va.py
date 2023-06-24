from src.va.flaskr import init, registerBlueprint, app

def main():
    init()
    registerBlueprint()
    app.run(app.config["flask"]["host"], app.config["flask"]["port"])

if __name__ == "__main__":
    main()
