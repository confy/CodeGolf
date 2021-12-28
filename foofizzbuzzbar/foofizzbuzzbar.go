package main

import (
	"fmt"
	"strconv"
)
func main() {
	for i := 1; i < 1001; i++ {
		var s = ""
		if i%2 == 0 {s += "Foo"}
		if i%3 == 0 {s += "Fizz"}
		if i%5 == 0 {s += "Buzz"}
		if i%7 == 0 {s += "Bar"}
		if s == "" {s = strconv.Itoa(i)}
		fmt.Println(s)
	}
}
