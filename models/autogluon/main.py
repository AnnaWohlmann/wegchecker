import autogluon.core as ag
from autogluon.vision import ImagePredictor, ImageDataset

def train():
    # filename = ag.download('https://autogluon.s3.amazonaws.com/datasets/shopee-iet.zip')
    # ag.unzip(filename)
    dataset, _, test_dataset = ImageDataset.from_folders('https://autogluon.s3.amazonaws.com/datasets/shopee-iet.zip')
    predictor = ImagePredictor()
    predictor.fit(dataset, hyperparameters={'epochs': 2})
    fit_result = predictor.fit_summary()
    print('Top-1 train acc: %.3f, val acc: %.3f' %(fit_result['train_acc'], fit_result['valid_acc']))

    test_acc = predictor.evaluate(test_dataset)
    print('Top-1 test acc: %.3f' % test_acc['top1'])

    filename = 'models/autrogluon/predictor.ag'
    predictor.save(filename)

def predict(img):
    filename = 'models/autrogluon/predictor.ag'
    predictor_loaded: ImagePredictor = ImagePredictor.load(filename)
    result = predictor_loaded.predict(img)
    return result