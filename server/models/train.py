from textgenrnn import textgenrnn

model_cfg = {
    'word_level': True,   # set to True if want to train a word-level model (requires more data and smaller max_length)
    'rnn_size': 128,   # number of LSTM cells of each layer (128/256 recommended)
    'rnn_layers': 2,   # number of LSTM layers (>=2 recommended)
    'rnn_bidirectional': False,   # consider text both forwards and backward, can give a training boost
    'max_length': 10,   # number of tokens to consider before predicting the next (20-40 for characters, 5-10 for words recommended)
    'max_words': 10000,   # maximum number of words to model; the rest will be ignored (word-level model only)
}

train_cfg = {
    'line_delimited': True,   # set to True if each text has its own line in the source file
    'num_epochs': 2,   # set higher to train the model for longer
    'gen_epochs': 2,   # generates sample text from model after given number of epochs
    'train_size': 0.8,   # proportion of input data to train on: setting < 1.0 limits model from learning perfectly
    'dropout': 0.0,   # ignore a random proportion of source tokens each epoch, allowing model to generalize better
    'validation': False,   # If train__size < 1.0, test on holdout dataset; will make overall training slower
    'is_csv': False   # set to True if file is a CSV exported from Excel/BigQuery/pandas
}

file_name = "../sources/cleaned.txt"
model_name = "dearblueno"

textgen = textgenrnn(name=model_name)

textgen.train_from_file(
    file_path=file_name,
    new_model=True,
    num_epochs=train_cfg['num_epochs'],
    gen_epochs=train_cfg['gen_epochs'],
    # batch_size=1024,
    # train_size=train_cfg['train_size'],
    # dropout=train_cfg['dropout'],
    # validation=train_cfg['validation'],
    # is_csv=train_cfg['is_csv'],
    rnn_layers=model_cfg['rnn_layers'],
    rnn_size=model_cfg['rnn_size'],
    # rnn_bidirectional=model_cfg['rnn_bidirectional'],
    # max_length=model_cfg['max_length'],
    # dim_embeddings=100,
    word_level=model_cfg['word_level']
)

textgen.save()
