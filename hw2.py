import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1: data.Point, point2: data.Point):
    if point1.x < point2.x:
        small_x = point1.x
        big_x = point2.x
    else:
        small_x = point2.x
        big_x = point1.x
    if point1.y > point2.y:
        big_y = point1.y
        small_y = point2.y
    else:
        small_y = point1.y
        big_y = point2.y
    top_left = data.Point(small_x, big_y)
    bottom_right = data.Point(big_x, small_y)
    return data.Rectangle(top_left, bottom_right)

# Part 2
def shorter_duration_than(duration1: data.Duration, duration2: data.Duration) -> bool:
    total1 = duration1.minutes * 60 + duration1.seconds
    total2 = duration2.minutes * 60 + duration2.seconds
    if total1 < total2:
        return True
    else:
        return False

# Part 3
def songs_shorter_than(lst: list[data.Song], duration: data.Duration ) -> list[data.Song]:
    result = []
    for song in lst:
       if song.duration.minutes < duration.minutes:
               result.append(song)
       elif song.duration.minutes == duration.minutes:
           if song.duration.minutes < duration.minutes:
               result.append(song)
    return result

# Part 4
def running_time(songs: list[data.Song], playlist: list[int]) -> data.Duration:
    total_seconds = 0
    for song_idx in playlist:
        if 0 <= song_idx < len(songs):
            song = songs[song_idx]
            if song.duration.minutes >= 0 and song.duration.seconds >= 0:
                total_seconds += song.duration.minutes * 60 + song.duration.seconds
    total_minutes = total_seconds// 60
    remaining_seconds = total_seconds % 60
    return data.Duration( minutes = total_minutes, seconds =remaining_seconds)

# Part 5
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    if len(route) <= 1:
        return True
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 =  route[i + 1]
        if [city1, city2] not in city_links:
            if [city2, city1] not in city_links:
                return False
    return True

# Part 6
def longest_repetition(lst: list[int]):
    longest = -1
    longest_i = None
    for i in range(len(lst)):
        length = repeat(lst, i)
        if length > longest:
            longest = length
            longest_i = i
    return longest_i
def repeat(lst, start):
    count = 0
    idx = start
    while(idx < len(lst) and lst[idx] == lst[start]):
        count += 1
        idx += 1
    return count

