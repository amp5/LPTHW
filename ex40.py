class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	def sing_backwards_line(self):
		for line in reversed(self.lyrics):
			print line

HB_lyrics = "Happy birthday to you", "I don't want to get sued", "So I'll stop right there"

BOP_lyrics = "They rally around tha family", "With pockets full of shells"

S_lyrics = "You are my sunshine", "My only sunshine", "You make me happy", "When skies are gray"

HATH_lyrics = ["I wish I was slave to an age-old trade",
			"Like riding 'round in railcars and working long days",
			"Lord have mercy on my rough and rowdy ways"]

happy_bday = Song(HB_lyrics)

bulls_on_parade = Song(BOP_lyrics)

sunshine = Song(S_lyrics)

Head_and_the_Heart = Song(HATH_lyrics)

happy_bday.sing_me_a_song()
print "..."
bulls_on_parade.sing_me_a_song()
print "..."
sunshine.sing_me_a_song()
print "..."
Head_and_the_Heart.sing_me_a_song()
print "..."
print "REVERSE"
print "..."
happy_bday.sing_backwards_line()
print "..."
bulls_on_parade.sing_backwards_line()
print "..."
sunshine.sing_backwards_line()
print"..."
Head_and_the_Heart.sing_backwards_line()
