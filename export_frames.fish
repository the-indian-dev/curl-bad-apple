#!/usr/bin/fish
mkdir frames
ffmpeg -i bad_apple.mp4 -r 10 -qscale:v 2 frames/frame_%04d.jpg
