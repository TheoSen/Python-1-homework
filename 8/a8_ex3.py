#todo
# creat a class StandardScaler 
# that standardizes features by removing the mean (µ) and scaling to unit standard deviation (σ).
import math
class StandardScaler:
    
    def __init__(self):
        # mu: the mean
        # sig: the variance
        self.mu = None
        self.sig = None
    
    # cal the mean and the standard deviation of the input features
    def fit(self,features: list):
        self.mu = sum(features)/len(features)
        self.sig = math.sqrt((sum((x-self.mu) **2 for x in features) / (len(features)-1)))
    
    # return a list of scaled input features based on the mu and sig
    def transform(self, features: list):
        if self.mu is None or self.sig is None:
            raise ValueError("Scaler has not been fitted")
        else:
            scaled_feature = [(x-self.mu)/self.sig for x in features]
        return scaled_feature
    
    # combines the fit and transform steps and returns the fitted input
    def fit_transform(self, features: list):
        self.fit(features)
        return self.transform(features)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Indices must be integers")
        
        if key == 0:
            return self.mu
        elif key == 1:
            return self.sig
        else:
            raise IndexError("Index out of range")
