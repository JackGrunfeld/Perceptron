import numpy as np
import random
import pandas as pd

import numpy as np
import random
import pandas as pd

class perceptron:
    def __init__(self, path):
        self.df = pd.read_csv(path, delimiter=' ')
        self.classification = self.df['class']
        self.bias = 1
        self.df = self.df.drop('class', axis=1)
        self.df["bias"] = self.bias
            
        self.columns = self.df.columns
        self.weights = np.ones(len(self.df.columns))
        self.epoch = 0
        self.accuracy = 0
    
    
    def testCurrent(self, instance, classification):
        dotProduct = np.dot(instance, self.weights)
        if (dotProduct) > 0:
            prediction = 'g' 
        else:
            prediction = 'b'
        if prediction == classification:
            return True
        else:   
            return False

    
     
    def activation(self):
        learning_rate = 0.1
        while self.epoch < (1000) and self.accuracy < 0.95:
         
            for i in range(len(self.df.values)):
               if self.testCurrent(self.df.values[i], self.classification[i]) == False:
                    if self.classification[i] == 'g':
                        self.weights += self.df.values[i] * learning_rate
                    else:
                        self.weights -= self.df.values[i] * learning_rate
                        
                    self.accuracy = self.test()
                    
                    if(self.accuracy > 0.95):
                      break
            print(self.epoch)
            self.epoch += 1
           
            
    def test(self):
        correct = 0
        for i in range(len(self.df.values)):
            if self.testCurrent(self.df.values[i], self.classification[i]):
                correct += 1
        return correct/len(self.df)
          
          
           
if __name__ == "__main__":
    p = perceptron('ionosphere.data')
    print("dataFrame: ", p.df)    
    p.activation()
    print("Weights: ", p.weights)
    print("Bias: ", p.bias)
    print("Accuracy: ", p.accuracy)
