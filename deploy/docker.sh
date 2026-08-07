#!/bin/bash
set -e
if [[ "$(uname)" == "Darwin" ]]; then
	bin="container"
else
	bin="docker"
fi

$bin build -t docs
$bin run -p 4000:4000 -p 35729:35729 -v "$PWD/src:/jekyll" --rm -it docs