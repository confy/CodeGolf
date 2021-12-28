package main

import "fmt"

func hello(name string) string {
	if name == "" {
		return "Hello, World!"
	}
	return fmt.Sprintf("Hello, %s!", name)
}

func main() {
	fmt.Println(hello("Adrian"))
}
