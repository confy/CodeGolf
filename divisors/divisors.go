package main

import "fmt"

func main() {
	for i := 1; i <= 100; i++ {
		for j := 1; j <= i+1; j++ {
			if i%j == 0 {
				fmt.Printf("%d ", j)
			}
		}
		fmt.Println()
	}
}
