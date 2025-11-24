import numpy as np
class neuron:
    def __init__(self,biais,weights):
        self.biais=biais
        self.weights=weights
    def forward(self,inputs):
        return np.dot(self.weights,inputs)+self.biais

class layer:
    def __init__(self,biais,weights):
        self.biais=biais
        self.weights=weights
    def forward(self,inputs):
        return np.dot(self.weights,inputs)+self.biais
