package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type User struct {
	Name  string `json:"name"`
	Age   int    `json:"age"`
	Email string `json:"email"`
}

func main() {
	var file_name string
	fmt.Print("Input the file name: ")
	fmt.Scan(&file_name)
	fmt.Printf("Your input is: %s\n", file_name)

	file, err := os.Open(file_name)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var user User
	decoder := json.NewDecoder(file)
	err = decoder.Decode(&user)
	if err != nil {
		fmt.Println("Error decoding JSON:", err)
		return
	}

	fmt.Printf("Name: %s, Age: %d, Email: %s\n", user.Name, user.Age, user.Email)
}
