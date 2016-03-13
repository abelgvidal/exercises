package main

import "fmt"


func fibonacci(limit uint) []uint {
	var seq []uint
	var x uint = 1
	var y uint = 2

	seq = append(seq, x)
	seq = append(seq, y)
	
	for newValue:=uint(0);newValue<=limit; {
		newValue = x+y
		seq = append(seq, newValue)
		x = y
		y = newValue
	}

	return seq
}

func removeOdds(mylist []uint) []uint {
	var result []uint

	for _, element := range mylist {
		if element % 2 == 0 {
			result = append(result, element)
		}
	}

	return result
}

func sumList(mylist []uint) uint {
	var total uint
	for _, element := range mylist {
		total += element
	}

	return total
}

func main() {
	var serie []uint
	serie = fibonacci(4000000)
	fmt.Println(len(serie), serie)
	pares := removeOdds(serie)
	fmt.Println(len(pares), pares)
	total := sumList(pares)
	fmt.Println(total)
}

