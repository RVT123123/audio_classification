import os
class Config:
    def __init__(self, mode='conv', nfilt=26, nfeat=13, nfft=512, rate=16000):
        self.mode = mode
        self.nfilt = nfilt
        self.nfeat =nfeat
        self.nfft = nfft
        self.rate = rate
        self.step = int(rate/10)
        self.model_path = os.path.join('/content/gdrive/My Drive/AUDIO_classifier/models/'+ mode + '.model')
        self.p_path = os.path.join('/content/gdrive/My Drive/AUDIO_classifier/pickle/' + mode + '.p')

