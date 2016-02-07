import logging
import json

from datetime import datetime

def make(model):
    def pred(sample):
        labels = model.predict([sample])
        label = int(labels[0]) if labels else None
        return label
    
    return pred

def with_logging(predictor, logger=None):
    logger = logging.getLogger(__name__) if not logger else logger

    def time_to_run(fn):
        start = datetime.now()
        result = fn()
        end = datetime.now()    
        return (result, (end - start).microseconds)

    def predict_with_logging(sample):
        label, time_delta = time_to_run(lambda: predictor(sample))
        logger.info(json.dumps({'sample': sample,
                                'label': label,
                                'performance_time': time_delta}))
        return label
    
    return predict_with_logging


    
