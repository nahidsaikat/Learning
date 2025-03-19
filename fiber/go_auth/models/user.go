package models

import (
	"log"

	"golang.org/x/crypto/bcrypt"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var DB *gorm.DB

type User struct {
	gorm.Model
	Username string
	Email    string
	Password string
}

func Connect() {
	var err error

	DB, err = gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
	if err != nil {
		log.Fatal("Unable to connect to database")
	}
	DB.AutoMigrate(&User{}) // Migrate the User model into the database schema

}

func Password_hash(pwd []byte) string {
	hash, err := bcrypt.GenerateFromPassword(pwd, bcrypt.MinCost) // Hash password
	if err != nil {
		log.Println(err)
	}
	return string(hash)
}

func Password_verify(hashed string, raw_pwd []byte) bool {
	bytehash := []byte(hashed)
	err := bcrypt.CompareHashAndPassword(bytehash, raw_pwd) // Compare hash
	if err != nil {
		log.Println(err)
		return false
	}
	return true
}

func UserExists(u *User) bool {
	Connect()

	var user User
	result := DB.First(&user, "username = ? OR email = ?", u.Username, u.Email)

	if result.RowsAffected > 0 {
		log.Println("User exists")
		return true
	} else {
		return false
	}
}

func CreateUser(user_data *User) *gorm.DB {
	Connect() // Connect to database

	result := DB.Create(&User{
		Username: user_data.Username,
		Email:    user_data.Email,
		Password: Password_hash([]byte(user_data.Password)), // Enter hashed password
	})

	return result
}
