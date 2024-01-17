gunzip -c dictionary.gz | grep "r" | grep -v "[bdefghjklmpqstuvwxy]" | grep -E ".{3}."
