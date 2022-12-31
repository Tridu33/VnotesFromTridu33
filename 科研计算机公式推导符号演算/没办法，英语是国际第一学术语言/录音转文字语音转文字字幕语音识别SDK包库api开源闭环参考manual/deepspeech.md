# deepspeech


```text
# Transcribe an audio file
deepspeech --model models.pbmm --scorer models.scorer --audio audio/2830-3980-0043.wav
```





教程

```
>deepspeech -h
usage: deepspeech [-h] --model MODEL [--scorer SCORER] --audio AUDIO
                  [--beam_width BEAM_WIDTH] [--lm_alpha LM_ALPHA]
                  [--lm_beta LM_BETA] [--version] [--extended] [--json]
                  [--candidate_transcripts CANDIDATE_TRANSCRIPTS]

Running DeepSpeech inference.

optional arguments:
  -h, --help            show this help message and exit
  --model MODEL         Path to the model (protocol buffer binary file)
  --scorer SCORER       Path to the external scorer file
  --audio AUDIO         Path to the audio file to run (WAV format)
  --beam_width BEAM_WIDTH
                        Beam width for the CTC decoder
  --lm_alpha LM_ALPHA   Language model weight (lm_alpha). If not specified,
                        use default from the scorer package.
  --lm_beta LM_BETA     Word insertion bonus (lm_beta). If not specified, use
                        default from the scorer package.  
  --version             Print version and exits
  --extended            Output string from extended metadata 来自扩展元数据的输出字符串
  --json                Output json from metadata with timestamp of each word 从元数据输出带有每个单词时间戳的json
  --candidate_transcripts CANDIDATE_TRANSCRIPTS
                        Number of candidate transcripts to include in JSON
                        output在JSON输出中包含的候选成绩单数量
```

使用了空格隔开每个发音,等于空格也是一个词,所以alphabet.txt上需要加上空格.(空格不是必须的,可以不用)









-   [项目主页](https://link.zhihu.com/?target=https%3A//github.com/mozilla/DeepSpeech)


DeepSpeech is an open source Speech-To-Text engine, using a model trained by machine learning techniques based on [Baidu's Deep Speech research paper](https://arxiv.org/abs/1412.5567). Project DeepSpeech uses Google's [TensorFlow](https://www.tensorflow.org/) to make the implementation easier.

Documentation for installation, usage, and training models are available on [deepspeech.readthedocs.io](http://deepspeech.readthedocs.io/?badge=latest).

For the latest release, including pre-trained models and checkpoints, [see the latest release on GitHub](https://github.com/mozilla/DeepSpeech/releases/latest).

For contribution guidelines, see [CONTRIBUTING.rst](https://github.com/mozilla/DeepSpeech/blob/master/CONTRIBUTING.rst).

For contact and support information, see [SUPPORT.rst](https://github.com/mozilla/DeepSpeech/blob/master/SUPPORT.rst).



















