from ..apis import BooksAPI
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register(r"books", BooksAPI, basename="books")

urlpatterns = [
    *router.urls,
]
