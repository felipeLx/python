import pandas as pd
# AND operator
# to change the weight's and bias
weight1 = 2.0
weight2 = 1.0
bias = -3.0

test_inputs = [(0,0), (0,1), (1,0), (1,1)]
correct_outputs = [False, False, False, True]
outputs = []

for test_input, correct_output in zip(test_inputs, correct_outputs):
    linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
    output = int(linear_combination >= 0)
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

num_wrong = len([output[4] for output in outputs if output[4]== 'No'])
output_frame = pd.DataFrame(outputs, columns=['Input 1', 'Linear Combination', 'Activation Output', 'Is Correct'])
if not num_wrong:
    print('Nice, you got it this correct.\n')
else:
    print('You got {} wrong. Keep trying\n'.format(num_wrong))
print(output_frame.to_string(index=False))

# What are two ways to go from an AND perceptron to an OR perceptron?
# increase the weights
# decrease the magnitude of the bias