import time
from pylsl import StreamInlet, resolve_stream
from time import sleep

# first resolve an EEG stream on the lab network
print("looking for an stream...")
streams = resolve_stream("name", "obci_eeg1")

inlet = StreamInlet(streams[0])
duration = 10


def testLSLSamplingRate():
    start = time.time()
    numSamples = 0
    numChunks = 0

    while time.time() <= start + duration:
        samples, timestamp = inlet.pull_chunk()
        if timestamp:
            numChunks += 1
            if samples is not None:
                assert len(samples) != 0
                numSamples += len(samples)
            # print(samples);

    print("Number of Chunks == {}".format(numChunks))
    print("Avg Sampling Rate == {}".format(numSamples / duration))


testLSLSamplingRate()