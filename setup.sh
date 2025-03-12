#!/bin/bash


CUR_LLVM_DIR=llvm
CUR_CSMITH_DIR=csmith


if [ ! -d $CUR_LLVM_DIR ]; then
    wget http://releases.llvm.org/7.0.0/clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz
    tar -xvf clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz
    mv clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04 ./$CUR_LLVM_DIR
    rm -f clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz	
fi

if [ ! -d $CUR_CSMITH_DIR ]; then
    git clone https://github.com/csmith-project/csmith.git
    cd csmith
    sudo apt install g++ gcc cmake m4
    mkdir -p csmith.installed
    cmake -DCMAKE_INSTALL_PREFIX=csmith.installed .
    make && make install
    cd ..
fi




