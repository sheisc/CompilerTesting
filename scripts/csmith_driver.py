from build_run import differ_testing

if __name__ == '__main__':
	target_name = "test_case"
	cnt = 0
	while True:
		cnt += 1
		if cnt % 10 == 0:
			print("Generating a test case: NO.{0}".format(cnt))
		differ_testing(target_name)
        
