#!/usr/bin/fish
for file in ascii_frames/*.txt
    #clear
    cat $file
    sleep 0.1
end
