import pytest
from main import BooksCollector

@pytest.fixture(autouse=True)
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def add_books(collector):
    collector.add_new_book('Война и Мир')
    collector.add_new_book('Горе от ума')
    collector.add_new_book('Ведьмак')

@pytest.fixture
def set_genre(collector, add_books):
    collector.set_book_genre('Война и Мир','Ужасы')
    collector.set_book_genre('Ведьмак','Ужасы')
    collector.set_book_genre('Горе от ума','Комедии')