.PHONY: build test

build:
	python3 scripts/build_flagToASM.py
	python3 scripts/build_ASMtoBin.py
	python3 scripts/build_bin_to_ram.py
	rm program.asm program.bin
test:
	python3 scripts/test_parseRAM.py
doc:
	pandoc -V geometry:margin=1cm -o writeup/TuringApproved-Writeup.pdf writeup/TuringApproved-Writeup.md

