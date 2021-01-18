DEPS=main.c fuzzgoat.c
CFLAGS=-fprofile-arcs -ftest-coverage
LIBS=-lm

all: $(DEPS)
	$(CC) -o fuzzgoat $(DEPS) $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm ./fuzzgoat
