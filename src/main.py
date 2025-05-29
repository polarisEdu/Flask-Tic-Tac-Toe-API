from src.di.container import Container


def main():

    container = Container()
    app = container.get_flask_app()

    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()