# co-authors Aman, Ashley
printenv USER

gunzip dictionary.gz -c | grep -xE "[muocaft]{1,}" | grep "a"
gunzip dictionary.gz -c | grep -xE "[taibrnl]{1,}" | grep "b"
gunzip dictionary.gz -c | grep -xE "[maocndi]{1,}" | grep "c"
gunzip dictionary.gz -c | grep -xE "[anozigr]{1,}" | grep "z"
