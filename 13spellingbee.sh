# co-author: Aman, Ashley
gunzip -c dictionary.gz | grep "r" | grep -v "[bdefghjklmpqstuvwxy]" | grep -E ".{3}."
# gunzip dictionary.gz -c | grep -xE "[ziacorn]{4,}" | grep "r"  this is what the TA and I came up with in office hours 
