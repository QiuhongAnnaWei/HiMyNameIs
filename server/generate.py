from textgenrnn import textgenrnn

def generateOne(pre):
    textgen = textgenrnn(weights_path='./models/dearblueno_weights.hdf5',
        vocab_path='./models/dearblueno_vocab.json',
        config_path='./models/dearblueno_config.json',
        name='dearblueno')
    return textgen.generate(temperature=0.5, prefix=pre, return_as_list=True)[0]