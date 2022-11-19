import autogluon.core as ag
from autogluon.vision import ImagePredictor, ImageDataset
# import pandas as pd
# import numpy as np
mapping = {
    "0": "footway",
    "1": "primary"
}
def train():
    # filename = ag.download('https://autogluon.s3.amazonaws.com/datasets/shopee-iet.zip')
    # dataset, _, test_set = ImageDataset.from_folders('https://autogluon.s3.amazonaws.com/datasets/shopee-iet.zip')
    # ag.unzip(filename)
    # class 1 footway 0 
    # class 2 primary 1
    dataset = ImageDataset.from_folder('data/Huwawi/HackaTUM_Data/dataset_preprocessed/train')
    test_dataset = ImageDataset.from_folder('data/Huwawi/HackaTUM_Data/dataset_preprocessed/test')
    predictor = ImagePredictor(verbosity = 4)
    # predictor.fit(dataset, hyperparameters={'epochs': 3}, presets=['medium_quality_faster_train'])
    predictor.fit(dataset, hyperparameters={'epochs': 2})
    fit_result = predictor.fit_summary()
    print('Top-1 train acc: %.3f, val acc: %.3f' %(fit_result['train_acc'], fit_result['valid_acc']))

    test_acc = predictor.evaluate(test_dataset)
    print('Top-1 test acc: %.3f' % test_acc['top1'])

    filename = 'models/autogluon/predictor.ag'
    predictor.save(filename)

def predict(img_path):
    filename = 'models/autogluon/predictor83-82.ag'
    # filename = 'models/autogluon/predictor.ag'
    predictor_loaded: ImagePredictor = ImagePredictor.load(filename)
    # print(predictor_loaded.fit_summary())
    predicts = predictor_loaded.predict_proba(img_path)
    result = predictor_loaded.predict(img_path)
    label = result[0]
    prec = predicts[label][0]
    label_str = mapping[str(label)]
    return {"label": label, "prec": prec, "label_str": label_str}

# train()
# train()
# predict(None)