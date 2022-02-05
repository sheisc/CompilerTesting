###################################################################
#
#   How to use:
#
#		python3 replay.py bug_1.c
#
####################################################################

from build_run import build, run
import sys

def write_file(filepath, output):
    with open(filepath, 'wb') as f:
        f.write(output)

def replay(src_file):
    print(src_file)
    target_name = src_file.split(".")[0]
    build("gcc", "-O3", src_file, target_name + ".gcc")
    output_gcc, timeout = run("./" + target_name + ".gcc")
    print(output_gcc)

    build("clang", "-O3", src_file, target_name + ".clang")
    output_clang, timeout = run("./" + target_name + ".clang")
    print(output_clang)

    if timeout:
        print("time out")
    elif output_clang != output_gcc:
        print("\n\noutput_clang != output_gcc\n")
        write_file("./" + target_name + ".gcc.txt", output_gcc)
        write_file("./" + target_name + ".clang.txt", output_clang)
    else:
        print("\n\noutput_clang == output_gcc\n")


if __name__ == '__main__':
    test_case = "test_cast.c"
    if len(sys.argv) > 1:
        test_case = sys.argv[1]
    print("Replaying the test case {0}\n".format(test_case))
    replay(test_case)

