package router

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/logger"
	noteRoutes "github.com/nahidsaikat/notes-api-fiber/internal/routes/note"
)

func SetupRoutes(app *fiber.App) {
	api := app.Group("/api", logger.New())

	// Setup the Node Routes
	noteRoutes.SetupNoteRoutes(api)
}
