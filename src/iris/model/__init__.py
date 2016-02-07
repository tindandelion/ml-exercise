import sys
import os.path as path

model_path = path.join(path.dirname(__file__), "model.pkl") 

def load():
    import iris.model.Model as Model
    sys.modules['Model'] = Model
    mdl = Model.load_model(model_path)
    mdl.timestamp = path.getctime(model_path)
    return mdl
