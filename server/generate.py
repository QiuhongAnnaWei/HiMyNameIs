from textgenrnn import textgenrnn

def generateOne(pre, temp):
    p = None if pre=="" else pre
    t = 0.5 if temp==0 else temp
    model_name = 'allnames2015-'
    dirpath = './models/allnames2015-/' # from server/
    textgen = textgenrnn(weights_path=f'{dirpath}{model_name}_weights.hdf5',
                        vocab_path=f'{dirpath}/{model_name}_vocab.json',
                        config_path=f'{dirpath}/{model_name}_config.json')
    return textgen.generate(temperature=t, prefix=p, n=5, max_gen_length=100, return_as_list=True)[0]