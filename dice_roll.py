from random import randint

class RollDice:
	def die_roll(faces):
		return randint(1,faces)

	def roll_command(input):
		try:
			die_count = int(input.split('d')[0])
		except:
			die_count = 1

		die_faces = int(input.split('d')[1].split('+')[0])

		try:
			modifier = int(input.split('+')[1])
		except:
			modifier = 0

	# 	print 'Count: {}\nFaces: {}\nModifier: {}'.format(die_count, die_faces, modifier)
		result = 0
		for i in range(0,die_count):
			result += die_roll(die_faces)
		result += modifier
		return result

	def roll(input):
		result = 0
		for command in input.split(' + '):
			result += roll_command(command)
		return result

	def test():
		print roll('d1')
		print "roll('d1')"
		print roll('d20')
		print "roll('d20')"
		print roll('2d1')
		print "roll('2d1')"
		print roll('2d20')
		print "roll('2d20')"
		print roll('d1+5')
		print "roll('d1+5')"
		print roll('d20+5')
		print "roll('d20+5')"
		print roll('2d1+5')
		print "roll('2d1+5')"
		print roll('2d20+5')
		print "roll('2d20+5')"
		print roll('d1 + d1')
		print "roll('d1 + d1')"
		print roll('d20 + d20')
		print "roll('d20 + d20')"
		print roll('2d1 + 2d1')
		print "roll('2d1 + 2d1')"
		print roll('2d20 + 2d20')
		print "roll('2d20 + 2d20')"
		print roll('d1+5 + d1+5')
		print "roll('d1+5 + d1+5')"
		print roll('d20+5 + d20+5')
		print "roll('d20+5 + d20+5')"
		print roll('2d1+5 + 2d1+5')
		print "roll('2d1+5 + 2d1+5')"
		print roll('2d20+5 + 2d20+5')
		print "roll('2d20+5 + 2d20+5')"