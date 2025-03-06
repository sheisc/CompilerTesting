# CompilerTesting


## How to use


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