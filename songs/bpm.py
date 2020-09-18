import librosa
def tempo(fp):
    y, sr = librosa.load(fp)
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    print(librosa.beat.tempo(onset_envelope=onset_env, sr=sr))


import sys
tempo(sys.argv[1])