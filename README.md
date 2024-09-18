# qa_python

Реализованные тесты в формате <метод>:<тестовые методы>:

1. add_new_book(self, name): 
    * test_add_new_book_add_different_books_with_valid_len_will_be_added(self, collector, book_name)
    * test_add_new_book_add_book_with_invalid_len_will_not_added(self, collector)

2. set_book_genre(self, name, genre)
    * test_set_book_genre_correct_genre_it_will_be_added(self, collector, add_books)
    * test_set_book_genre_incorrect_genre_will_not_be_added(self, collector, add_books)

3. get_book_genre(self, name)
    * test_get_book_genre_correct_genre_will_be_returned(self, collector, add_books, set_genre)
    * test_get_book_genre_without_genre_will_be_returned_empty(self, collector, add_books)

4. get_books_with_specific_genre(self, genre)
    * test_get_books_with_specific_genre_correct_genre(self, collector, add_books, set_genre)
    * test_get_books_with_specific_genre_genre_in_lowercase(self, collector, add_books, set_genre)

5. get_books_genre(self)
    * test_get_books_genre_correct_len(self, collector, add_books, set_genre)
    * test_get_books_genre_correct_books_and_genres(self, collector, add_books, set_genre)

6. get_books_for_children(self)
    * test_get_books_for_children_correct_books_return(self, collector, add_books, set_genre)

7. add_book_in_favorites(self, name)
    * test_add_book_in_favorites_book_added_and_not_in_favorites(self, collector, add_books, set_genre)
    * test_add_book_in_favorites_book_added_but_already_in_favorites(self, collector, add_books, set_genre)
    * test_add_book_in_favorites_book_not_added_and_not_in_favorites(self, collector, add_books, set_genre)

8. delete_book_from_favorites(self, name)
    * test_delete_book_from_favorites_book_is_in_favorites_deleted(self, collector, add_books)
    * test_delete_book_from_favorites_book_not_in_favorites_not_affect_favorites_list(self, collector, add_books)

9. get_list_of_favorites_books(self)
    * test_get_list_of_favorites_books_list_same_as_was_inserted(self, collector, add_books)