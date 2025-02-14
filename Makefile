CC=gcc
CFLAGS=-Wall -Wextra -std=c99 -pedantic -g
TESTCFLAGS=-Wall -Wextra -std=c99 -D TEST

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

test_eccentric: eccentric.c test_eccentric.c
	$(CC) $(TESTCFLAGS) -o $@ test_eccentric.c

test_ll_equal: ll_equal.c node.h test_ll_equal.c
	$(CC) $(TESTCFLAGS) -o $@ test_ll_equal.c

test_ll_cycle: ll_cycle.c node.h test_ll_cycle.c
	$(CC) $(TESTCFLAGS) -o $@ test_ll_cycle.c

clean:
	$(RM) a.out eccentric ll_equal ll_cycle program programa hello interactive_hello test_eccentric test_ll_equal test_ll_cycle

.PHONY: clean all
