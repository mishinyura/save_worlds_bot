def format_data_word(*args):
    col_names = ('id', 'eng', 'rus', 'transcription', 'audio')
    new_data = dict(zip(col_names, *args))
    return new_data