import random
from datetime import datetime

# task 1  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from faker import Faker

fake = Faker()

number_of_cards = int(input("enter number of cards:"))
type_of_cards = input("enter 1 for business cards, 2 for base cards:")

class BaseContact:
    def __init__(self, name, surname, phone_number, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email

    def contact(self):
        print(f"I'm dialing {self.phone_number} and calling {self.name} {self.surname}")

    @property
    def label_length(self):
        return len(self.name) + len(self.surname)


class BusinessContact(BaseContact):
    def __init__(self, name, surname, phone_number, email, company_name, position, company_phone_number):
        super().__init__(name, surname, phone_number, email)
        self.company_name = company_name
        self.position = position
        self.company_phone_number = company_phone_number

    def contact(self):
        print(
            f"I'm dialing {self.company_phone_number} and calling {self.name} {self.surname} from {self.company_name}"
        )


def create_business_cards_list(number_of_cards, contact_type):
    cards = []
    for _ in range(number_of_cards):
        if contact_type == "1":
            cards.append(
                BusinessContact(
                    name=fake.first_name(),
                    surname=fake.last_name(),
                    phone_number=fake.phone_number(),
                    email=fake.email(),
                    company_name=fake.company(),
                    position=fake.job(),
                    company_phone_number=fake.phone_number(),
                )
            )
        else:
            cards.append(
                BaseContact(
                    name=fake.first_name(),
                    surname=fake.last_name(),
                    phone_number=fake.phone_number(),
                    email=fake.email(),
                )
            )

    for card in cards:
        print(f"{card.name} {card.surname} - {card.email} - {card.phone_number} - {card.company_phone_number if isinstance(card, BusinessContact) else 'N/A'} - {card.position if isinstance(card, BusinessContact) else 'N/A'} - {card.company_name if isinstance(card, BusinessContact) else 'N/A'}")
    
    return cards


create_business_cards_list(number_of_cards, type_of_cards)

new_contact_base = BaseContact("John", "Doe", "99999999999", "john.doe@example.com")
new_contact_base.contact()

new_contact_business = BusinessContact(
    name="Jane",
    surname="Smith",
    phone_number="987654321",
    email="jane.smith@example.com",
    company_name="Example Corp",
    position="Manager",
    company_phone_number="123-456-7890"
)
new_contact_business.contact()

print('**************************************************************************************************************')
print('\n')
# decorators  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# def say_louder(func):
#    def wrapper():
#        result = func()
#        return result.upper()
#    return wrapper


# @say_louder
# def say_hello():
#    greeting = "Hello stranger!"
#    return greeting

# print(say_hello())


# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = datetime.now()
#         result = func(*args, **kwargs)
#         end_time = datetime.now()
#         elapsed_time = (end_time - start_time).total_seconds()
#         print(f"Computation time: {elapsed_time:.2f} seconds")
#         return result
#     return wrapper

# @measure_time
# def create_business_cards(count):
#     fake = Faker()
#     cards = []
#     for _ in range(count):
#         cards.append(
#             BusinessContact(
#                 name=fake.first_name(),
#                 surname=fake.last_name(),
#                 phone_number=fake.phone_number(),
#                 email=fake.email(),
#                 company_name=fake.company(),
#                 position=fake.job(),
#                 company_phone_number=fake.phone_number(),
#             )
#         )
#     return cards

# create_business_cards(1000)


# task 2  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Movie:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.play_count = 0

    def play(self):
        self.play_count += 1

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class TVSeries(Movie):
    def __init__(self, title, release_year, genre, season_number, episode_number):
        super().__init__(title, release_year, genre)
        self.season_number = season_number
        self.episode_number = episode_number

    # No method 'play' needed here - it will be inherited from Movie

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def play_item(self, index):
        if 0 <= index < len(self.items):
            self.items[index].play()

    def display_library(self):
        for idx, item in enumerate(self.items):
            print(f"{idx}: {item} - Plays: {item.play_count}")

    def get_movies(self):
        return sorted(
            [item for item in self.items if not isinstance(item, TVSeries)],
            key=lambda x: x.title.lower(),
        )

    def get_series(self):
        return sorted(
            [item for item in self.items if isinstance(item, TVSeries)],
            key=lambda x: x.title.lower(),
        )

    def search(self, title):
        title_lower = title.lower()
        return [item for item in self.items if title_lower == item.title.lower()]

    def generate_views(self):
        if self.items:
            item = random.choice(self.items)
            views = random.randint(1, 100)
            for _ in range(views):
                item.play()

    def run_generator_ten_times(self):
        for _ in range(10):
            self.generate_views()

    def top_titles(self, count=5, content_type=None):
        if content_type == "movie":
            items = self.get_movies()
        elif content_type == "series":
            items = self.get_series()
        else:
            items = self.items

        return sorted(items, key=lambda x: x.play_count, reverse=True)[:count]


library = Library()
library.add_item(Movie("Pulp Fiction", 1994, "Crime"))
library.add_item(TVSeries("The Simpsons", 1989, "Comedy", 1, 6))
library.add_item(Movie("Star Gate", 1994, "Science Fiction"))
library.add_item(TVSeries("Star Trek Voyager", 1989, "Comedy", 1, 10))
library.add_item(Movie("Matrix", 1999, "Science Fiction"))
library.add_item(TVSeries("Allo Allo", 1988, "Comedy", 1, 9))
library.add_item(Movie("Transformers", 2012, "Science Fiction"))
library.add_item(TVSeries("Mac Gyver", 1985, "Action", 1, 11))
library.add_item(Movie("Osiris", 2025, "Science Fiction"))
library.add_item(TVSeries("Battlestar Galactica", 2006, "Science Fiction", 1, 4))
library.add_item(Movie("The Darkest Hour", 2024, "War"))
library.add_item(TVSeries("Space above and beyond", 1987, "Action", 1, 1))


# print("Library contents:")
# library.display_library()

# print("Playing some items...")
# library.play_item(0)
# library.play_item(1)
# library.display_library()

# print("Movies or series in library sorted by title:")
# print([str(serie) for serie in library.get_series()])
# print([str(movie) for movie in library.get_movies()])

# print("Searching for items in library...")
# search_results = library.search("Pulp Fiction")
# print("Search results:")
# for item in search_results:
#     print(item)

# print("Generating random views for 1  item...")
# library.generate_views()
# library.display_library()


# print("Generating random views run 10 times...")
# library.run_generator_ten_times()
# library.display_library()


# print("Top 5 most popular items of series or movies:")
# library.run_generator()
# for item in library.top_titles(5, 'series'):
#     print(f"{item} - Plays: {item.play_count}")

# def add_season_to_library(library, title, release_year, genre, season_number, num_episodes):
#     for episode in range(1, num_episodes + 1):
#         library.add_item(TVSeries(title, release_year, genre, season_number, episode))


# # Example usage:
# add_season_to_library(library, "Doctor Who", 2005, "Science Fiction", 1, 10)
# library.display_library()

# print(library)

# def count_series_episodes(library, series_title):
#     episodes = [item for item in library.items if isinstance(item, TVSeries) and item.title.lower() == series_title.lower()]
#     print(f"{series_title}: {len(episodes)} episodes available")
#     return len(episodes)


# # Example usage:
# count_series_episodes(library, "Doctor Who")
# count_series_episodes(library, "The Simpsons")



print("Movie Library")

library.run_generator_ten_times()

current_date = datetime.now().strftime("%d.%m.%Y")
print(f"Most popular movies and TV shows of {current_date}")

for item in library.top_titles(3):
    print(f"{item} - Plays: {item.play_count}")


print('**************************************************************************************************************')