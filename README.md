# Hi, My Name is...

Introducing "Hi, My Name Is...", an online tool for generating unique and creative names using a neural network trained on a database of top names.

This online tool takes in an input of any or all of the following: desired prefix, uniqueness level, and/or similar-sounding word for the name that they want. Then, we use that information to generate an exciting new name following the user's specifications using a recurrent neural network from [textgenrnn](https://github.com/minimaxir/textgenrnn) trained using a database of top US baby names from 2015-2019 (from the [SSA Database](https://www.ssa.gov/oact/babynames/limits.html)). Specifically, for similar-sounding name, we made use of the Soundex algorithm, cosine similarity, and bag of words to output a name that has similar pronunciation to the specified word.

### To run:
From the project directory:  
`cd server`  
`pip3 install -r requirements.txt`  
`python3 app.py`  

Potentially, you may need to edit the textgenrnn source file to accomodate a recent update of Tensorflow. Please refer to the github issue [here](https://github.com/minimaxir/textgenrnn/issues/197).

The site should be up and running at [localhost:5000/](http://localhost:5000/)

