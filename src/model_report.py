import json
import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

import iris.model as wm

from sklearn.metrics import confusion_matrix, classification_report

def load_samples():
    sample_filename = "./test/example.json"
    return [s for s in json.load(open(sample_filename)) if 'label' in s]

def plot_confusion_matrix(cm):
    target_names = ['0', '1', '2']
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion matrix')
    plt.colorbar()
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names, rotation=45)
    plt.yticks(tick_marks, target_names)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

model = wm.load()
samples = load_samples()

label_test = [s['label'] for s in samples]
data = [s['info'] for s in samples]
label_pred = model.predict(data)

cm = confusion_matrix(label_test, label_pred)
print("Confusion matrix:\n", cm)
plt.figure()
plot_confusion_matrix(cm)
plt.savefig('confusion_matrix.png')

report = classification_report(label_test, label_pred)
print("Classification report:\n", report)
