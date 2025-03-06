# CompilerTesting

## Overview

- Use and Customize [CSmith](https://github.com/csmith-project/csmith) to automatically generate C programs.

- Test whether there is any difference in the outputs of the same program compiled by GCC and Clang.

## How to use

Download [CSmith](https://github.com/csmith-project/csmith) and [LLVM](https://releases.llvm.org/download.html).

Configure the environment variables CSMITH_HOME and LLVM_INSTALL_PATH in scripts/csmith.sh.

```sh
$ cd scripts
scripts$ . ./csmith.sh 
scripts$ make

```
### Directory

```
scripts
├── Bugs                    bugs found by difference testing
├── build_run.py            build and run a program
├── csmith_driver.py        main() for difference testing in gcc and clang
├── csmith.sh               start everything
├── Makefile
└── replay.py               replay one bug (a C program automatically generated by CSmith) found

```