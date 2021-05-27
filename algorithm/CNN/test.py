import numpy as np


class NormBase:
    """Base class of normalizations.
    """
    def __init__(self, num_channels, gamma=None, beta=None, eps=1e-5):
        """Initialization.
        `gamma` and `beta` are learnable parameters which are denoted as
        `gamma` and `beta` in the equation.
        """
        self.C = num_channels
        self.eps = eps

        self.gamma = gamma if gamma is not None else np.random.uniform(size=self.C)
        self.beta = beta if beta is not None else np.random.uniform(size=self.C)

    def forward(self, input):
        raise NotImplementedError


class InstanceNorm(NormBase):
    def forward(self, input):

        mini_batch_mean = input.sum(axis=0)/len(input)
        mini_batch_var = ((input-mini_batch_mean)**2).sum(axis=0)/len(input)
        output = (input-mini_batch_mean)/((mini_batch_var+self.eps)**0.5)

        for i in range(self.C):
            gamma = self.gamma[i]
            beta = self.beta[i]
            output[:,i,:,:] = gamma*output[:,i,:,:] + beta

        return output
        
temp = InstanceNorm(3)

input_ = np.array(
    [
        [
            [
                [1,2,1,1],
                [1,1,2,8],
                [1,3,1,1],
                [1,1,1,4]
                ],
            [
                [2,2,1,2],
                [2,3,2,2],
                [2,2,2,3],
                [2,2,3,2]
                ],

            [
                [3,3,4,3],
                [3,5,3,3],
                [7,3,5,3],
                [3,7,3,3]
                ]
        ]
    ]
    )

temp.forward(input_)
