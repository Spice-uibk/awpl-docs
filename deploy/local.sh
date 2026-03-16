#!/bin/bash

# Navigate to the sources of the page
cd src

# Install using bundler
bundle install

# Start server
bundle exec jekyll serve
