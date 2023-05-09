# 1. pythonPypi模块打开本地文件










```python
def load_model_hdf(model_path, encoding_json=None, need_encoding=True):
    """Load a model from a .hdf file. If label encodings are not present,
    try to load them from enncoding_json."""
    # try to get structure + encoding from hdf, else use the
    # one provided (or raise an exception if it is not provided).
    m = load_model(model_path, custom_objects={'qscore': qscore})
    encoding = None
    with h5py.File(model_path, 'r') as h5:
        if _encod_path_ in h5:
            encoding = [s.decode() for s in h5[_encod_path_][()]]
            logging.info("Loaded encoding from {}.".format(model_path))

    if encoding is None and encoding_json is not None:
        encoding = load_encoding(encoding_json)
        logging.info("Loaded encoding from {}.".format(encoding_json))

    if encoding is None and need_encoding:
        raise KeyError("Could not find label encodings in the model, please provide an encoding json")

    return m, encoding
```

就像tensorflow直接加载打开本地文件*.h5，只需要传入代码中的文件地址就行


```
model.save('my_model.h5')   # HDF5 file, you have to pip3 install h5py if don't have it
```









