def books_context_processor(request):
    return {
        "mojedane": "Warto czytać książki",
        "request": request
    }

