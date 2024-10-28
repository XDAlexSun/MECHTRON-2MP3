CC = gcc
CFLAGS = -O3 -fPIC
LIBRARY = libmysort.so
SRC = mySort.c

$(LIBRARY): $(SRC)
	$(CC) $(CFLAGS) -shared -o $(LIBRARY) $(SRC)

clean:
	rm -f $(LIBRARY)
