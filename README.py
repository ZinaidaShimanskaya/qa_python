from main import BooksCollector

class TestBooksCollector:

    # 1. Добавление двух книг
    def test_add_new_book_add_two_books_two_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    # 2. Добавление двух одинаковых книг
    def test_add_new_book_add_the_same_book_twice_the_book_added_once(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Мастер и Маргарита')
        assert len(collector.get_books_rating()) == 1

    # 3. Установление книге рейтинга 10
    def test_set_book_rating_set_book_rating_10_the_book_rating_is_ten(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 10)
        assert collector.get_book_rating('Война и мир') == 10

    # 4. Установление книге рейтинга 0
    def test_set_book_rating_set_book_rating_zero_the_book_rating_is_one(self):
        collector = BooksCollector()
        collector.add_new_book('Бесы')
        collector.set_book_rating('Бесы', 0)
        assert collector.get_book_rating('Бесы') == 1

    # 5. Установление книге рейтинга 11
    def test_set_book_rating_set_book_rating_eleven_the_book_rating_is_one(self):
        collector = BooksCollector()
        collector.add_new_book('Идиот')
        collector.set_book_rating('Идиот', 11)
        assert collector.get_book_rating('Идиот') == 1

    # 6. Получение рейтинга книги по ее имени
    def test_get_book_rating_get_book_rating_9_book_rating_is_9(self):
        collector = BooksCollector()
        collector.add_new_book('Гранатовый браслет')
        collector.set_book_rating('Гранатовый браслет', 9)
        rating=collector.get_book_rating('Гранатовый браслет')
        assert rating == 9

    # 7. Получение списка книг с определенным рейтингом
    def test_get_books_with_specific_rating_get_books_with_rating_three_books_with_rating_three_are_displayed(self):
        collector = BooksCollector()
        collector.add_new_book('Капитанская дочка')
        collector.add_new_book('Евгений Онегин')
        collector.set_book_rating('Капитанская дочка', 3)
        collector.set_book_rating('Евгений Онегин', 3)
        books_with_rating_three=collector.get_books_with_specific_rating(3)
        assert books_with_rating_three == ['Капитанская дочка', 'Евгений Онегин']

    # 8. Добавление книги в избранное
    def test_add_book_in_favourites_add_a_book_in_favourites_the_book_is_added(self):
        collector = BooksCollector()
        collector.add_new_book('Тарас Бульба')
        collector.add_book_in_favorites('Тарас Бульба')
        assert len(collector.get_list_of_favorites_books()) == 1

    # 9. Добавление той же самой книги в избранное дважды
    def test_add_book_in_favourites_add_book_in_favourites_twice_book_is_added_once(self):
        collector = BooksCollector()
        collector.add_new_book('Герой нашего времени')
        collector.add_book_in_favorites('Герой нашего времени')
        collector.add_book_in_favorites('Герой нашего времени')
        assert len(collector.get_list_of_favorites_books()) == 1

    # 10. Добавление книги, которой нет в словаре, в избранное
    def test_add_book_in_favourites_add_book_not_from_books_rating_to_favourites_favourites_is_empty(self):
            collector = BooksCollector()
            collector.add_book_in_favorites('1984')
            assert len(collector.get_list_of_favorites_books()) == 0

    # 11. Удаление книги из избранного
    def test_delete_book_from_favorites_delete_one_book_from_favorites_book_is_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('На западном фронте без перемен')
        collector.add_book_in_favorites('На западном фронте без перемен')
        collector.delete_book_from_favorites('На западном фронте без перемен')
        assert len(collector.get_list_of_favorites_books()) == 0

