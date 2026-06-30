import matplotlib.pyplot as plt

music = ["Pop", "Rock", "Hip Hop", "Classical", "Jazz"]
streams = [2400, 1800, 2200, 900, 700]

plt.bar(music, streams)
plt.title("Music Genre Streams")
plt.xlabel("Music Genres")
plt.ylabel("Number of Streams")
plt.show()

print("Pop is the most streamed music genre with 2400 streams, and Jazz is the least streamed with 700 streams.")
