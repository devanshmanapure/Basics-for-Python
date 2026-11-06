#Song Duration Calculator
songs = {}
for i in range(3):
    name = input("Enter song name: ")
    time = int(input("Enter duration (seconds): "))
    songs[name] = time
total = sum(songs.values())
print("Total Duration:", total // 60, "minutes")
print("Longest Song:", max(songs, key=songs.get))
print("Shortest Song:", min(songs, key=songs.get))