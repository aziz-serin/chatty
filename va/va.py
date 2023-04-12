from app import App
from controllers.chat_controller import openai

app = App(db_host="localhost", db_port=27017)

def main():
    register()
    app.__app__.run(port=8080)

def register():
    app.__app__.register_blueprint(openai)

if __name__ == "__main__":
    main()
