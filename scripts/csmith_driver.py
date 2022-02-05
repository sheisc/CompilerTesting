import threading
import signal

from build_run import *

TOTAL_NUM_OF_THREADS = 4
threads = None

class CSmithThread(threading.Thread):
	def __init__(self, thread_id):
		threading.Thread.__init__(self)
		self.thread_id = thread_id
		self.stopped = False
		self.bug_id = 0

	def differ_testing(self, target_name="test_cast", dest_path_prefix="./"):
		src_file = target_name + ".c"
		# generate a test case
		res = gen_test_case("csmith", src_file)
		if res:
			# build and run it with gcc
			build("gcc", "-O3", src_file, target_name + ".gcc")
			output_gcc, time_out_gcc = run("./" + target_name + ".gcc")
			# print(output_gcc)

			# build and run it with clang
			build("clang", "-O3", src_file, target_name + ".clang")
			output_clang, time_out_clang = run("./" + target_name + ".clang")
			# print(output_clang)

			# compare the results
			if time_out_gcc or time_out_clang:
				print("Time out")
			elif output_gcc != output_clang:
				print("output_gcc != output_clang")
				self.bug_id += 1
				save_test_cases(src_file, dest_path_prefix, self.bug_id, self.thread_id)

	def run(self):
		target_name = "test_case_" + str(self.thread_id)
		cnt = 0
		while not self.stopped:
			cnt += 1
			if cnt % 5 == 0:
				print("Thread {0}: generating a test case: NO.{1}".format(self.thread_id, cnt))
			self.differ_testing(target_name)
		print("Thread {0}: saying goodbye.".format(self.thread_id))

	def stop_testing(self):
		self.stopped = True

def exit_signal_handler(sig, frame):
	global threads
	if threads:
		for cur_thread in threads:
			cur_thread.stop_testing()
	#sys.exit(0)

if __name__ == '__main__':
	signal.signal(signal.SIGINT, exit_signal_handler)
	threads = []
	for thread_id in range(TOTAL_NUM_OF_THREADS):
		cur_thread = CSmithThread(thread_id)
		threads.append(cur_thread)
		cur_thread.start()
	# Handle the CTRL+c to stop all the threads



