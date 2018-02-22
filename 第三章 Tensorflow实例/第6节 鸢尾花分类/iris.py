# 第6节 鸢尾花分类
import tensorflow as tf
import pandas as pd

# 获取数据集
TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']

train_path = tf.keras.utils.get_file(
	fname = TRAIN_URL.split('/')[-1],
	origin = TRAIN_URL
	)
train = pd.read_csv(
	filepath_or_buffer = train_path,
	names = CSV_COLUMN_NAMES,
	header = 0
	)
train_features, train_label = train, train.pop('Species')

test_path = tf.keras.utils.get_file(
	TEST_URL.split('/')[-1], 
	TEST_URL
	)
test = pd.read_csv(
	filepath_or_buffer = test_path,
	names = CSV_COLUMN_NAMES,
	header=0
	)
test_features, test_label = test, test.pop('Species')

predict_features = {
'SepalLength': [5.1, 5.9, 6.9],
'SepalWidth': [3.3, 3.0, 3.1],
'PetalLength': [1.7, 4.2, 5.4],
'PetalWidth': [0.5, 1.5, 2.1]
}
expected_label = ['Setosa', 'Versicolor', 'Virginica']

# 输入函数
def train_input_fn():
	dataset = tf.data.Dataset.from_tensor_slices(
		(dict(train_features), train_label)
		)
	dataset = dataset.shuffle(1000).repeat().batch(100)
	return dataset

def eval_input_fn():
	dataset = tf.data.Dataset.from_tensor_slices(
		(dict(test_features), test_label)
		)
	dataset = dataset.batch(100)
	return dataset

def pred_input_fn():
	dataset = tf.data.Dataset.from_tensor_slices(
		dict(predict_features)
		)
	dataset = dataset.batch(1)
	return dataset

def main(argv):
	feature_columns = []
	for key in train_features.keys():
		feature_columns.append(tf.feature_column.numeric_column(key = key))

	classifier = tf.estimator.DNNClassifier(
		hidden_units = [10, 10],
		feature_columns = feature_columns,
		model_dir = 'tmp/model',
		n_classes = 3
		)

	# 训练
	classifier.train(
		input_fn = train_input_fn,
		steps= 1000
		)

	# 评估
	eval_result = classifier.evaluate(
		input_fn = eval_input_fn
		)

	print('\nTest set accuracy: %.2f\n'%eval_result['accuracy'])

	# 预测
	predictions = classifier.predict(
		input_fn = pred_input_fn
		)

	for pred_dict, expec in zip(predictions, expected_label):
		class_id = pred_dict['class_ids'][0]
		probability = pred_dict['probabilities'][class_id]

		print('\nPrediction is "%s" (%.1f%%), expected "%s"'%(
			SPECIES[class_id],
			100 * probability,
			expec
			))

if __name__ == '__main__':
	tf.logging.set_verbosity(tf.logging.INFO)
	tf.app.run(main)