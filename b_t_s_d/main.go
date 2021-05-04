package main

import "fmt"

func main(){
	fmt.Print("Enter The Bit Number :=>")
	var bit int
	fmt.Scanln(&bit)
	fmt.Println("The Number of storeable data :=>",caculate_process(bit))
}

func caculate_process(bit int) int{
	var total_value int
	if (bit <= 0){
		total_value = 0
	}else{
		total_value = 1
	}
	for i := 1 ; i <= bit ;i++ {
		total_value *= 2
	}
	return total_value
}