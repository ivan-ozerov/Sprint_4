from main import BooksCollector
import pytest
    

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

        
    @pytest.fixture(autouse=True)
    def collector(self):
        collector = BooksCollector()
        return collector

    @pytest.fixture
    def add_books(self, collector):
        collector.add_new_book('Война и Мир')
        collector.add_new_book('Горе от ума')
        collector.add_new_book('Ведьмак')

    @pytest.fixture
    def set_genre(self, collector, add_books):
        collector.set_book_genre('Война и Мир','Ужасы')
        collector.set_book_genre('Ведьмак','Ужасы')
        collector.set_book_genre('Горе от ума','Комедии')

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name', ['Война и Мир', '!"№;%:?*()-_=+', '14211453', 'Warhammer 40000', 'ВОЙНА И МИР', 'война и мир', '1234567890123456789012345678901234567890'])
    def test_add_new_book_add_different_books_with_valid_len_will_be_added(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    def test_add_new_book_add_book_with_invalid_len_will_not_added(self, collector):
        book_name = '12345678901234567890123456789012345678901'
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_correct_genre_it_will_be_added(self, collector, add_books):
        book_genre = 'Ужасы'
        book_name = 'Война и Мир'
        collector.set_book_genre(book_name, book_genre)
        assert collector.books_genre[book_name] == book_genre

    def test_set_book_genre_incorrect_genre_will_not_be_added(self, collector, add_books):
        book_genre = 'Комедийный триллер'
        book_name = 'Война и Мир'
        collector.set_book_genre(book_name, book_genre)
        assert collector.books_genre[book_name] == ''

    def test_get_book_genre_correct_genre_will_be_returned(self, collector, add_books, set_genre):
        book_genre = 'Ужасы'
        book_name = 'Война и Мир'
        assert collector.get_book_genre(book_name) == book_genre

    def test_get_book_genre_without_genre_will_be_returned_empty(self, collector, add_books):
        book_name = 'Война и Мир'
        assert collector.get_book_genre(book_name) == ''

    def test_get_books_with_specific_genre_correct_genre(self, collector, add_books, set_genre):
        books_list = ['Война и Мир', 'Ведьмак']
        for book in books_list:
            assert book in collector.get_books_with_specific_genre('Ужасы')

    def test_get_books_with_specific_genre_genre_in_lowercase(self, collector, add_books, set_genre):
        books_list = ['Война и Мир', 'Ведьмак']
        for book in books_list:
            assert book not in collector.get_books_with_specific_genre('ужасы')

    def test_get_books_genre_correct_len(self, collector, add_books, set_genre):
        assert len(collector.get_books_genre()) == 3
        
    def test_get_books_genre_correct_books_and_genres(self, collector, add_books, set_genre):
        books_list = {'Война и Мир':'Ужасы',
                      'Ведьмак':'Ужасы',
                      'Горе от ума':'Комедии'}
        assert books_list == collector.get_books_genre()
            
    def test_get_books_for_children_correct_books_return(self, collector, add_books, set_genre):
        assert collector.get_books_for_children() == ['Горе от ума']

    def test_add_book_in_favorites_book_added_and_not_in_favorites(self, collector, add_books, set_genre):
        book_name = 'Ведьмак'
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    def test_add_book_in_favorites_book_added_but_already_in_favorites(self, collector, add_books, set_genre):
        book_name = 'Ведьмак'
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    def test_add_book_in_favorites_book_not_added_and_not_in_favorites(self, collector, add_books, set_genre):
        book_name = 'Гарри Поттер'
        collector.add_book_in_favorites(book_name)
        assert book_name not in collector.favorites

    def test_delete_book_from_favorites_book_is_in_favorites_deleted(self, collector, add_books):
        book_name = 'Горе от ума'
        if book_name not in collector.favorites:    
            favorites_before = collector.favorites
            collector.add_book_in_favorites(book_name)
        else:
            favorites_before = collector.favorites

        collector.delete_book_from_favorites(book_name)
        assert favorites_before == collector.favorites

    def test_delete_book_from_favorites_book_not_in_favorites_not_affect_favorites_list(self, collector, add_books):
        book_name = 'Горе от ума'
        if book_name not in collector.favorites:
            favorites_before = collector.favorites
            collector.delete_book_from_favorites(book_name)
        else:
            collector.delete_book_from_favorites(book_name)
            collector.delete_book_from_favorites(book_name)
            favorites_before = collector.favorites
        
        assert favorites_before == collector.favorites

    def test_get_list_of_favorites_books_list_same_as_was_inserted(self, collector, add_books):
        book_name = 'Горе от ума'
        book_name2 = 'Ведьмак'
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name2)
        assert collector.get_list_of_favorites_books() == [book_name, book_name2]