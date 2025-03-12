import shlex
import os
import subprocess
import logging
from threading import Timer

CSMITH_HOME = os.getenv("CSMITH_HOME")
if not CSMITH_HOME:
    CSMITH_HOME = "./csmith/csmith.installed"
bug_id = 0


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
    return res == 0


def build(compiler, optimize, src_file, exe_file):
    cmd_line = [compiler, optimize, src_file, "-I"+CSMITH_HOME+"/include", "-o", exe_file]
    #print(cmd_line)
    try:
        proc = subprocess.Popen(cmd_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        return False

    output = proc.communicate()[0]
    #print(output)
    return proc.returncode == 0


def run(exe_file, timeout_sec=1):
    cmd_line = [exe_file]
    ouput = "{0}: time out after {1} seconds.\n".format(exe_file, timeout_sec)
    try:
        output = subprocess.check_output(cmd_line, stderr=subprocess.STDOUT, timeout=timeout_sec)
    except Exception as e:
        return ouput, True
    return output, False

def save_test_cases(src_file, dest_path, bug_id, thread_id=0):
    cmd_line = ["cp", src_file, dest_path+"/bug_" + str(bug_id) + "_" + str(thread_id) + ".c"]
    try:
        subprocess.Popen(cmd_line)
    except Exception as e:
        pass







