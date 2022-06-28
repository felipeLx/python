"""
Feedforward is the process neural networks use to turn the input into an output.

Backpropagation
	Doing a feedforward operation.
	Comparing the output of the model with the desired output.
	Calculating the error.
	Running the feedforward operation backwards (backpropagation) to spread the error to each of the weights.
	Use this to update the weights, and get a better model.
	Continue this until we have a model that is good.

Calculation of the derivative of the sigmoid function
Recall that the sigmoid function has a beautiful derivative, which we can see in the following calculation. This will make our backpropagation step much cleaner.

omega'(x) = (alpha / (alpha * x)) * (1/(1 + exp(x)) = omega(x) * (1-omega(x))
"""
