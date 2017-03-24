export GOPATH=$(shell pwd)/../

objects = sum.so sum.h

binary:
	go build -buildmode=c-shared -o sum.so ./pygo/main.go
all: binary

clean:
	rm $(objects)
