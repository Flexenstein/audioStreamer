import generateAudio
import threading
import pyaudio
from pynput.mouse import Controller
from pynput.keyboard import Listener, KeyCode, Key

exit_key = Key.esc
freq1Up_key = KeyCode(char='u')
freq1Down_key = KeyCode(char='j')
freq2Up_key = KeyCode(char='i')
freq2Down_key = KeyCode(char='k')

p = pyaudio.PyAudio()

fs = 44100 
duration = 2   
initFreqList = [0,50]
initVolume = 0.5    

stream = p.open(format=pyaudio.paFloat32,
        channels=1,
        rate=fs,
        output=True)


class streamAudio(threading.Thread):
    def __init__(self, initFreqList, initVolume, p, fs, stream):
        super(streamAudio, self).__init__()
        self.freqList = initFreqList
        self.volume = initVolume
        self.p = p
        self.stream = stream
        self.fs = fs
        self.running = True
        self.program_running = True
        input

    def exit(self):
        self.running = False
        self.program_running = False

    def freq1Up(self):
        self.freqList[0] += 5
        print('Frequencies:')
        print(self.freqList)

    def freq1Down(self):
        self.freqList[0] -= 5
        print('Frequencies:')
        print(self.freqList)

    def freq2Up(self):
        self.freqList[1] += 5
        print('Frequencies:')
        print(self.freqList)

    def freq2Down(self):
        self.freqList[1] -= 5
        print('Frequencies:')
        print(self.freqList)

    def run(self):
        print("Press ESC to stop program")
        freqList = self.freqList
        volume = self.volume
        fs = self.fs
        while self.running:
            audioOutput = generateAudio.generateSample(freqList)
            stream.write(volume*audioOutput)

        stream.stop_stream()
        stream.close()

        p.terminate()
                
emouse = Controller()
audio_thread = streamAudio(initFreqList, initVolume, p, fs, stream)
audio_thread.start()


def on_press(key):
    if key == exit_key:
        audio_thread.exit()
        listener.stop()
    elif key == freq1Up_key:
        audio_thread.freq1Up()
    elif key == freq1Down_key:
        audio_thread.freq1Down()
    elif key == freq2Up_key:
        audio_thread.freq2Up()
    elif key == freq2Down_key:
        audio_thread.freq2Down()


with Listener(on_press=on_press) as listener:
    listener.join()