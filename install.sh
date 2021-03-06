#!/bin/bash

shell_path=$(pwd)
bin_path=${shell_path}/bin
tool_path=${shell_path}/tools

function install_cutFile() {
  cutFile_tool_path=${tool_path}/cutFile
  cd ${bin_path}
  ln -s ${cutFile_tool_path}/cutFile.py cutFile
  echo "cutFile installed."
}

function install_myMan() {
  myman_tool_path=${tool_path}/myMan
  cd ${bin_path}
  ln -s ${myman_tool_path}/myman.py myman
  echo "myman installed."
}

install_cutFile
install_myMan