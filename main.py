from data_func.apps_data_stat import *
from data_func.apps_data_vis import *
from manual_testing import tests
import os


MAIN_MENU: str = """
'1': Получить общую информацию о массиве данных
'2': Вывести все категории приложений
'3': Вывести все жанры приложений
'4': Вывести самые популярные жанры
'5': Вывести самые популярные приложения
'6': Получить среднее значение Рейтинга/Размера/Цены/Установок
'7': Получить медианное значение Рейтинга/Размера/Цены/Установок
'8': Визуализация данных
'9': Запустить тест
'0': Выйти из программы
"""

MAIN_FUNCTION_CHOICES: dict = {
    '1': get_data_overview,
    '2': get_all_categories,
    '3': get_all_genres,
    '4': get_x_most_popular_genres,
    '5': get_x_most_popular_apps,
    '6': get_mean_rating_size_price_installs,
    '7': get_median_rating_size_price_installs,
    '9': tests
}

VISUALISATION_MENU: str = """
    '1': Визуализировать категории приложений
    '2': Визуализировать жанры приложений
    '3': Визуализировать рейтинг приложений по жанру
    '4': Визуализировать общее распределение рейтинга приложений
    '5': Визуализировать размер приложений по жанру
    '6': Визуализировать % бесплатных приложений по жанру
    '7': Визуализировать распределение цены приложений по жанру
    '8': Визуализировать число установок по жанру
    '9': Визуализировать зависимость между рейтингом и размером приложений
    '0': Вернутся в главное меню
    """

VISUALISATION_FUNCTION_CHOICES: dict = {
    '1': vis_categories,
    '2': vis_genres,
    '3': vis_rating_per_genre,
    '4': vis_rating_as_boxenplot,
    '5': vis_size_per_genre,
    '6': vis_free_and_paid_per_genre,
    '7': vis_price_as_scatterplot,
    '8': vis_installs_per_genre,
    '9': vis_optimal_app_size_per_genre
}


def user_menu() -> None:
    """
    Основной пользовательский интерфейс.
    Запускается через 'if __name__ == '__main__'
    """

    # Создаем папку для графиков, если её нет
    try:
        os.mkdir(path='data_visualization')
    except FileExistsError:
        pass

    user_input = input(MAIN_MENU+'\n')
    while user_input != '0':
        if user_input in (MAIN_FUNCTION_CHOICES.keys()):
            MAIN_FUNCTION_CHOICES[user_input]()
            user_input = input(MAIN_MENU + '\n')
        # Меню визуализации данных
        elif user_input == '8':
            user_second_input = input(VISUALISATION_MENU + '\n')
            while user_second_input != '0':
                if user_second_input in list(VISUALISATION_FUNCTION_CHOICES.keys()):
                    VISUALISATION_FUNCTION_CHOICES[user_second_input]()
                    user_second_input = input(VISUALISATION_MENU + '\n')
                else:
                    print('Недействительный выбор\n')
                    user_second_input = input(VISUALISATION_MENU + '\n')
            user_input = input(MAIN_MENU + '\n')
        else:
            print('Недействительный выбор\n')
            user_input = input(MAIN_MENU)


print('Программа завершена')


if __name__ == '__main__':
    user_menu()
