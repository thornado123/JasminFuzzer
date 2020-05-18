# DENNE MAKEFILE BLIVER IKKE BRUGT LIGE NU.
JASMINC?=/Users/josefgharib/Desktop/jasmin/compiler/jasminc.native

all: main
	./main

.s: add1.jazz
	$(JASMINC) -lea -o $@ $<

run: add1.s main.c
	$(CC) -O2 -o $@ $^

clean:
	rm -f main add1.s