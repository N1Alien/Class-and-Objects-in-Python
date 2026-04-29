from faker import Faker

fake = Faker()

number_of_cards = int(input("enter number of cards:"))
type_of_cards = input("enter 1 for business cards, 2 for base cards:")

business_cards = []

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
    for _ in range(number_of_cards):
        if contact_type == "1":
            business_cards.append(
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
            business_cards.append(
                BaseContact(
                    name=fake.first_name(),
                    surname=fake.last_name(),
                    phone_number=fake.phone_number(),
                    email=fake.email(),
                )
            )
    
    for card in business_cards:
        print(f"{card.name} {card.surname} - {card.email} - {card.phone_number} - {card.company_phone_number if isinstance(card, BusinessContact) else 'N/A'} - {card.position if isinstance(card, BusinessContact) else 'N/A'} - {card.company_name if isinstance(card, BusinessContact) else 'N/A'}")


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

