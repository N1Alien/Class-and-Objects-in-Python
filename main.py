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
                    "company": fake.company(),
                    "position": fake.job(),
                    "email": fake.email(),
                }
            )

        self.display_business_cards_list()
            
    def display_business_cards_list(self):
        for card in self.business_cards:
            print(f"Name: {card['name']} , Company: {card['company']}, Position: {card['position']}, Email: {card['email']}")
    
    
MyList = BusinessCardList(5)

