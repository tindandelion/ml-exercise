import logging

from iris.server import app

handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s|%(asctime)s|%(levelname)s|%(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
