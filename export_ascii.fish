#!/usr/bin/fish
mkdir ascii_frames
for file in frames/frame_*.jpg 
        set basename (basename $file .jpg)
        echo "Processing $basename"
	jp2a --height=20 $file > ascii_frames/$basename.txt
    end
