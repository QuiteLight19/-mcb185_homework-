import biofun

s = 'ACGTGGGGGGCATATG'

print(biofun.transcribe('ACGT'))
print(biofun.revcomp('AAAACGT'))
print(biofun.translate(s))
print(biofun.gc_comp(s))
print(biofun.gc_skew(s), biofun.gc_skew(biofun.revcomp(s)))