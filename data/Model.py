class SimpleModel:
    """
    SimpleModel test class (homework for ML engineers).
    """
    def __init__(self, scaler=None, model=None):
        """
        Constructs SimpleModel's instances.
        
        @param scaler: data scaling object ('transform' method is used)
        @param model: prediction object ('predict' method is used)
        """
        self.scaler = scaler
        self.model = model
        
    def predict(self, data):
        """
        Predicts category of input data vectors.
        
        @param data: a list of lists of four float numbers, for example [[1.0, -1.5, 4.8, 2.7]]
        @returns: a list of decisions per each input data vector;
                  None if (1) the given data is incorrect or (2) the instance is misconfigured
        """
        try:
            if self.model:
                return self.model.predict(self.scaler.transform(data)) if self.scaler else self.model.predict(data)
        except ValueError:
            pass
            
        return None


def load_model(model_path="./model.pkl"):
    """
    Loads a pickled test model from according to model_path parameter.
    
    @param model_path: (str) path to pickled model file
    @returns: (SimpleModel) an instance of SimpleModel class
    """
    from sklearn.externals import joblib
    
    model = joblib.load(model_path)
    
    return model
        

def save_model(model, model_path="./model.pkl"):
    """
    Saves a test model from according to model_path parameter.

    @param model: (SimpleModel) an instance of SimpleModel class
    @param model_path: (str) path to the model container
    """
    from sklearn.externals import joblib
    
    joblib.dump(model, model_path, compress=True)
