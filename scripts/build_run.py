import shlex
import os
import subprocess
import logging
from threading import Timer

CSMITH_HOME = os.getenv("CSMITH_HOME")
if not CSMITH_HOME:
    CSMITH_HOME = "/home/iron/github/CompilerTesting/csmith/csmith.installed"
#bug_id = 0

# def Popen(*pargs, **kwargs):
#     try:
#         return subprocess.Popen(*pargs, **kwargs)
#     except OSError:
#         raise


def gen_test_case(csmith, src_file, *csmith_args):
    cmd_line = [csmith]
    cmd_line.extend(csmith_args)
    #print(len(csmith_args))
    cmd_line.append("-o")
    cmd_line.append(src_file)
    #print(cmd_line)
    try:
        proc = subprocess.Popen(cmd_line)
    except Exception as e:
        #print("except Exception as e")
        return False
    res = proc.wait()
    if res != 0:
        return False
    return True


def build(compiler, optimize, src_file, exe_file):
    cmd_line = [compiler, optimize, src_file, "-I"+CSMITH_HOME+"/include", "-o", exe_file]
    #print(cmd_line)
    try:
        proc = subprocess.Popen(cmd_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        return False

    output = proc.communicate()[0]
    #print(output)
    if proc.returncode != 0:
        return False
    return True

def run(exe_file, timeout_sec=10):
    cmd_line = [exe_file]
    try:
        output = subprocess.check_output(cmd_line, stderr=subprocess.STDOUT, timeout=timeout_sec)
    except Exception as e:
        return exe_file + ": " + e.__str__()
    return output

def save_test_cases(src_file, dest_path, bug_id):
    cmd_line = ["cp", src_file, dest_path+"/bug_" + str(bug_id) + ".c"]
    try:
        subprocess.Popen(cmd_line)
    except Exception as e:
        pass


def differ_testing(target_name="test_cast"):
    bug_id = 0
    src_file = target_name + ".c"
    # generate a test case
    res = gen_test_case("csmith", src_file)
    if res:
        # build and run it with gcc
        build("gcc", "-O3", src_file, target_name + ".gcc")
        output_gcc = run("./" + target_name + ".gcc")
        #print(output_gcc)

        # build and run it with clang
        build("clang", "-O3", src_file, target_name + ".clang")
        output_clang = run("./" + target_name + ".clang")
        #print(output_clang)

        # compare the results
        if output_gcc != output_clang:
            print("output_gcc != output_clang")
            bug_id += 1
            save_test_cases(src_file, "./", bug_id)



# if __name__ == '__main__':
#     target_name = "test_case"
#     while True:
#         differ_testing(target_name)

