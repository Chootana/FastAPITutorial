from random import choice
from time import sleep


class MockMLAPI:
    def __init__(self):
        self.model = None
    
    def load(self, filepath=''):
        """
        When server is activated, load weight for performance improvement.
        Then, assign pretrained model instance to self.model.
        """
        sleep(20)
        pass
    
    def predict(self, x):
        """
        - Load data 
        - Pre-process
        - Prediction by self.model 
        - Post-process
        """

        sleep(10)
        preds = [choice(['happy', 'sad', 'angry']) for _ in range(len(x))]
        out = [
            {'text': t.text, 'sentiment': s} for t, s in zip(x, preds)
        ]

        return out
