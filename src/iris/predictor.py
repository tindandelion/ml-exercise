def make(model):
    def pred(sample):
        labels = model.predict([sample])
        if labels:
            return int(labels[0])
        else:
            return None
    
    return pred
