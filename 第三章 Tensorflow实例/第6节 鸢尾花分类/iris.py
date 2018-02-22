# 第6节 鸢尾花分类
import tensorflow as tf
import pandas as pd

# 获取数据集
TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']

# 输入函数
def train_input_fn(features, labels, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)
    return dataset


def eval_input_fn(features, labels, batch_size):
    features = dict(features)
    if labels is None:
        inputs = features
    else:
        inputs = (features, labels)

    dataset = tf.data.Dataset.from_tensor_slices(inputs)
    dataset = dataset.batch(batch_size)
    return dataset

def load_data(label_name = 'Species'):
    train_path = tf.keras.utils.get_file(
        fname = TRAIN_URL.split('/')[-1],
        origin = TRAIN_URL
        )
    train = pd.read_csv(
        filepath_or_buffer = train_path,
        names = CSV_COLUMN_NAMES,
        header = 0
        )
    train_features, train_label = train, train.pop(label_name)

    test_path = tf.keras.utils.get_file(
    	TEST_URL.split('/')[-1], 
    	TEST_URL
    	)
    test = pd.read_csv(
    	filepath_or_buffer = test_path, 
    	names = CSV_COLUMN_NAMES, 
    	header=0
    	)
    test_features, test_label = test, test.pop(label_name)

    return (train_features, train_label), (test_features, test_label)

def main(argv):
    (train_x, train_y), (test_x, test_y) = load_data()

    feature_columns = []
    for key in train_x.keys():
        feature_columns.append(tf.feature_column.numeric_column(key = key))

    classifier = tf.estimator.DNNClassifier(
    	hidden_units = [10, 10],
        feature_columns = feature_columns,
        model_dir = 'tmp/model',
        n_classes = 3
        )

    # 训练
    classifier.train(
        input_fn = lambda: train_input_fn(train_x, train_y, 100),
        steps= 1000
        )

    # 评估
    eval_result = classifier.evaluate(
        input_fn = lambda: eval_input_fn(test_x, test_y, 100)
        )

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    # 预测
    expected = ['Setosa', 'Versicolor', 'Virginica']
    predict_x = {
        'SepalLength': [5.1, 5.9, 6.9],
        'SepalWidth': [3.3, 3.0, 3.1],
        'PetalLength': [1.7, 4.2, 5.4],
        'PetalWidth': [0.5, 1.5, 2.1],
    }

    predictions = classifier.predict(
        input_fn = lambda: eval_input_fn(predict_x, labels = None, batch_size = 1)
        )

    for pred_dict, expec in zip(predictions, expected):
        template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(SPECIES[class_id],
                              100 * probability, expec))

if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)