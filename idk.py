from RaspberryMotors.motors import servos

def main():
	print('start')

	s1 = servos.servo(11)
	s2 = servos.servo(13)

	s1.setAngleAndWait(0)
	s2.setAngleAndWait(0)
	s1.setAngleAndWait(180)
	s2.setAngleAndWait(180)

	s1.shutdown()
	s2.shutdown()

	print('yeet')

if __name__ == '__main__':
	main()
