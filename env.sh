#!/bin/bash

CUR_LLVM_DIR=llvm
CUR_CSMITH_DIR=csmith


export CSMITH_HOME=$(cd $(dirname $0);pwd)/$CUR_CSMITH_DIR/csmith.installed
export LLVM_INSTALL_PATH=$(cd $(dirname $0);pwd)/$CUR_LLVM_DIR
export PATH=$LLVM_INSTALL_PATH/bin:$CSMITH_HOME/bin:$PATH


