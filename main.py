from faker import Faker

fake = Faker()


class BusinessCardList:
    def __init__(self, number_of_cards):
        self.business_cards = []
        self.create_business_cards_list(number_of_cards)

    def create_business_cards_list(self, number_of_cards):
        for _ in range(number_of_cards):
            self.business_cards.append(
                {
                    "name": fake.name(),
                    "email": fake.email(),
                }
            )

        self.sort_by_name()
        self.sort_by_surname()
        self.sort_by_email()
   
    def display_business_cards_list(self):
        for card in self.business_cards:
            split_name = card['name'].split()
            print(f"Name: {split_name[0]} Surname: {split_name[1]}, Email: {card['email']}")
    
    def sort_by_name(self):
        self.business_cards = sorted(self.business_cards, key=lambda card: card['name'])
        self.display_business_cards_list()
        print("\n")

    def sort_by_surname(self):
        self.business_cards = sorted(self.business_cards, key=lambda card: card['name'].split()[1])
        self.display_business_cards_list()
        print("\n")

    def sort_by_email(self):
        self.business_cards = sorted(self.business_cards, key=lambda card: card['email'])
        self.display_business_cards_list()
        print("\n")
 

MyList = BusinessCardList(5)