import warnings
import json
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':

	# create a Dejavu instance
	djv = Dejavu(config)
	print "type f for get inpit from file and type m for use microphone"
	inp = raw_input()
	# Fingerprint all the mp3's in the directory we give it
	djv.fingerprint_directory("mp3", [".mp3"])
	# Recognize audio from a file
	if inp == "f":
		song = djv.recognize(FileRecognizer, "Josh-Woodward--I-Want-To-Destroy-Something-Beautiful.mp3")
		print "From file we recognized: %s\n" % song
	# Or recognize audio from your microphone for `secs` seconds
	if inp == "m":
		secs = 5
		song = djv.recognize(MicrophoneRecognizer, seconds=secs)
		if song is None:
			print "Nothing recognized -- did you play the song out loud so your mic could hear it? :)"
		else:
			print "From mic with %d seconds we recognized: %s\n" % (secs, song)

	# Or use a recognizer without the shortcut, in anyway you would like
	#recognizer = FileRecognizer(djv)
	#song = recognizer.recognize_file("mp3/Josh-Woodward--I-Want-To-Destroy-Something-Beautiful.mp3")
	#print "No shortcut, we recognized: %s\n" % song
