# About This Project  
This is basic implementation of Perceptron and Backpropagation method for Artificial Neural Network. It is used to recognize letter which is represented as an array of length 81 (9x9).
The `index.html` and `generator.js` are used to generate training data. At the moment, only letter A and B are classified. 

# What I learn  
- Basic implementation of perceptron and backpropagation method

# How to
## Generating Data
  1. Open `index.html`
  2. Draw letter-like shape by pressing button
  3. Enter desired output in the text field
  4. Press GenerateData button
  5. The result will be generated as an array and printed on the Browser's Console

## Run the program -> todo: add epoch limitation
  1. `python2 perceptron.py`
  2. `python2 backprop.py`

## Test the result -> todo: create model automatically based on previously ran program
  1. `python2 test_perceptron.py`
  1. `python2 test_backprop.py`