from pydub import AudioSegment
from pydub.silence import split_on_silence

sound = AudioSegment.from_file("D:\\Abhishek\\RA\Respeak\\Recordings\\test_recording1.wav",format="wav")
chunks = split_on_silence(sound, 
    # must be silent for at least half a second
    min_silence_len=500,

    # consider it silent if quieter than -16 dBFS
    silence_thresh=-26
)

print "begin exporting"

for i, chunk in enumerate(chunks):
    print i
    chunk.export("D:\Abhishek\RA\Respeak\silence_output\chunk{0}.wav".format(i), format="wav")
