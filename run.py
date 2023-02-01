from waitress import serve
from application import create_app


app = create_app()


def main():
    serve(app, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
