from pydub import AudioSegment
from sys import argv
with open(argv[2], 'r') as f:
	tracks = []
	for line in f.readlines():
		l = line.rstrip().split("|")
		x = l[1].split(":")
		l[1] = 1000 * (int(x[0]) * 60 + int(x[1]))
		tracks.append(l)
print(tracks)

full = AudioSegment.from_file(argv[1])

for i in range(0, len(tracks)):
	try:
		full[tracks[i][1]:tracks[i+1][1]].export(argv[3] + "/" + tracks[i][0] + ".m4a", format="ipod", tags={'title': tracks[i][0], 'track': f"{(i + 1):02}" + "/" + f"{len(tracks):02}"})
	except:
		full[tracks[i][1]:len(full)].export(argv[3] + "/" + tracks[i][0] + ".m4a", format="ipod", tags={'title': tracks[i][0], 'track': f"{(i + 1):02}" + "/" + f"{len(tracks):02}"})
	print(tracks[i][0])