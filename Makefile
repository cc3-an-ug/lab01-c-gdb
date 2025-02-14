CC=gcc
CFLAGS=-Wall -Wextra -std=c99 -pedantic -g

all: program hello interactive_hello eccentric ll_equal ll_cycle

program: program.c
	$(CC) $(CFLAGS) -o $@ $<

hello: hello.c
	$(CC) $(CFLAGS) -o $@ $<

interactive_hello: interactive_hello.c
	$(CC) $(CFLAGS) -o $@ $<

eccentric: eccentric.c
	$(CC) $(CFLAGS) -o $@ $<

ll_equal: ll_equal.c node.h
	$(CC) $(CFLAGS) -o $@ $<

ll_cycle: ll_cycle.c node.h
	$(CC) $(CFLAGS) -o $@ $<

clean:
	$(RM) a.out eccentric ll_equal ll_cycle program programa hello interactive_hello

.PHONY: clean all
