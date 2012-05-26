import perceptron_train
import perceptron_predict
import unittest

class PerceptronTestCase(unittest.TestCase):
    def testPrediction(self):
        training_set = [[3,3], [4,3], [1,1], [2,1]]
        test_set = [[5,5], [1,1]]
        label = [1, 1, -1, -1]
        model = perceptron_train.perceptron_train(training_set, label)
        prediction = perceptron_predict.perceptron_predict(test_set, model)
                
        self.assertEqual(prediction, [1, -1])

if __name__=="__main__":
    unittest.main()