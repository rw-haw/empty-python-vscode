#!/bin/bash
wget https://github.com/rw-haw/empty-python-vscode/archive/refs/heads/main.zip
unzip main.zip
mv empty-python-vscode-main/* ./
rm -rf empty-python-vscode-main
rm main.zip
mv RENAMETO.env .env