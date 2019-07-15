#!/bin/bash
echo "Installing Python dependecies"
pip install -r requirements.txt

echo "Installing firefox geckodriver in browsers folder in the project dir"
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar xvfz geckodriver-v0.24.0-linux64.tar.gz
mv geckodriver browsers/geckodriver
rm -rf geckodriver-v0.24.0-linux64.tar.gz

echo "Installing chromedriver in browsers folder in the project dir"
wget https://chromedriver.storage.googleapis.com/75.0.3770.140/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver browsers/
rm -rf chromedriver_linux64.zip