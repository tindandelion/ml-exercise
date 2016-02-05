import sys
import os.path as path

def model_path():
    current_dir = path.dirname(__file__)
    return path.join(current_dir, "model.pkl")
  
def load():
    import iris.model.Model as Model
    sys.modules['Model'] = Model
    return Model.load_model(model_path())
