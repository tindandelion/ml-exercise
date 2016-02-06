def make(model):
    def pred(sample):
        labels = model.predict([sample])
        label = int(labels[0]) if labels else None
        return label
    
    return pred
