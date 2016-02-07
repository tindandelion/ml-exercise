import iris.model as model

from iris.predictor import with_logging, make
from iris.server import app

mdl = model.load()
app.predictor = with_logging(make(mdl),
                             extra={'model_ctime': mdl.timestamp})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
