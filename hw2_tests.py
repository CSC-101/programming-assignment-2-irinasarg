import data
import hw2
import unittest

from hw2 import create_rectangle


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_Rectangle_1(self):
        point1 = data.Point(5, 2)
        point2 = data.Point(6, 7)
        rectangle = create_rectangle(point1, point2)
        self.assertEqual(rectangle.top_left.x, 5)
        self.assertEqual(rectangle.top_left.y, 7)
        self.assertEqual(rectangle.bottom_right.x, 6)
        self.assertEqual(rectangle.bottom_right.y, 2)

    def test_create_Rectangle_2(self):
        point1 = data.Point(-2, 0)
        point2 = data.Point(3, 8)
        rectangle = create_rectangle(point1, point2)
        self.assertEqual(rectangle.top_left.x, -2)
        self.assertEqual(rectangle.top_left.y, 8)
        self.assertEqual(rectangle.bottom_right.x, 3)
        self.assertEqual(rectangle.bottom_right.y, 0)

    # Part 2
    def test_shorter_duration_than_1(self):
        duration1 = data.Duration(3, 5)
        duration2 = data.Duration(10, 9)
        result = hw2.shorter_duration_than(duration1, duration2)
        self.assertEqual(result, True )

    def test_shorter_duration_than_2(self):
        duration1 = data.Duration(7, 5)
        duration2 = data.Duration(4, 2)
        result = hw2.shorter_duration_than(duration1, duration2)
        self.assertEqual(result, False )
    # Part 3
    def test_songs_shorter_than_1(self):
        song1 = data.Song("Irina", "Love", data.Duration(2,3))
        song2 = data.Song("Maya", "Fire", data.Duration(7,12))
        result = hw2.songs_shorter_than([song1, song2], data.Duration(7, 5))
        self.assertEqual(result, [song1])

    def test_songs_shorter_than_2(self):
        song1 = data.Song("Bob", "Lemons", data.Duration(2,5))
        song2 = data.Song("Maya", "Fire", data.Duration(1,12))
        result = hw2.songs_shorter_than([song1, song2], data.Duration(7, 5))
        self.assertEqual(result, [song1, song2])

    # Part 4
    def test_running_time_1(self):
        song1 = data.Song("artist 1", "song 1", data.Duration(5, 10))
        song2 = data.Song("artist 2", "song 1", data.Duration(2, 20))
        song3 = data.Song("artist 3", "song 1", data.Duration(1, 15))
        song4 = data.Song("artist 4", "song 1", data.Duration(0, 20))
        songs = [song1, song2, song3, song4]
        playlist = [0, 2, 1, 3, 0]
        result = hw2.running_time(songs, playlist)
        self.assertEqual(result.minutes, 14)
        self.assertEqual(result.seconds, 15)

    def test_running_time_2(self):
        song1 = data.Song("artist 1", "song 1", data.Duration(5, 10))
        song2 = data.Song("artist 2", "song 1", data.Duration(-2, -20))
        songs = [song1, song2]
        playlist = [0, 1]
        result = hw2.running_time(songs, playlist)
        self.assertEqual(result.minutes, 5)
        self.assertEqual(result.seconds, 10)

    # Part 5
    def test_valid_route_1(self):
        city_links = [["san luis obispo", "santa margarita"],
            ['san luis obispo', "pismo beach"],
            ["atascadero", "santa margarita"]]
        route = ["san luis obispo", "LA", "atascadero"]
        self.assertFalse(hw2.validate_route(city_links, route))

    def test_valid_route_2(self):
        city_links = [["san luis obispo", "santa margarita"],
            ['san luis obispo', "pismo beach"],
            ["atascadero", "santa margarita"]]
        route = ["san luis obispo", "santa margarita", "atascadero", "santa margarita", "san luis obispo", "pismo beach"]
        self.assertTrue(hw2.validate_route(city_links, route))

    # Part 6
    def test_longest_repetition_1(self):
        list = [1, 1, 1, 2, 2, 2, 2, 3]
        result = hw2.longest_repetition(list)
        expected = 3
        self.assertEqual(expected, result)

    def test_longest_repetition_2(self):
        list = []
        result = hw2.longest_repetition(list)
        expected = None
        self.assertEqual(expected, result)

    def test_longest_repetition_3(self):
        list = [2, 2, 3, 3]
        result = hw2.longest_repetition(list)
        expected = 0
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
