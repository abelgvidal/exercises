package main

import "fmt"


func sumList(list []int) int{
	var total int = 0
	
	for _,element := range list {
		total += element
	}

	return total
}


func main() {
	const maximo = 1000
	var multiples []int
	
	for i := 1; i <= maximo; i++ {
		if i % 3 == 0 || i % 5 == 0 {
			multiples = append(multiples, i)
//			fmt.Println("len-->", len(multiples), "cap-->", cap(multiples), "content-->", multiples)
//			fmt.Println("*********************")
		}
	}

	fmt.Println(sumList(multiples), multiples)
}

