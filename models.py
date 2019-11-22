import otree.api
from Tools.scripts.make_ctype import values
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Anita Eichmann, Hertha , Lara Torka, Mayra Wagner'

doc = "X"


class Constants(otree.api.BaseConstants):
    name_in_url = 'assignment'
    players_per_group = None
    num_rounds = 6


    # x = initial_endowment = currency_range(c(100), c(200), c(50))
    # y =
    endowment1 = otree.api.Currency(1345)
    endowment2 = otree.api.Currency(1445)
    endowment3 = otree.api.Currency(1545)


# class Introduction(otree.api.BaseSubsession):
# pass


class Subsession(otree.api.BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            if self.round_number == 3:
                p.payoff = Constants.endowment1 - self.priceTShirt - self.priceCoffee - self.priceMobile -\
                           self.priceContract - self.priceChair
            if self.round_number == 4:
                p.payoff = Constants.endowment2 - self.priceTShirt - self.priceCoffee - self.priceMobile - \
                           self.priceContract - self.priceChair
            if self.round_number == 5:
                p.payoff = Constants.endowment3 - self.priceTShirt - self.priceCoffee - self.priceMobile - \
                           self.priceContract - self.priceChair


class Group(otree.api.BaseGroup):
    pass


class Player(otree.api.BasePlayer):
    evaluation1 = otree.api.models.FloatField(
        label='Your self-evaluation in %',
        min=0, max=100)
    evaluation2 = otree.api.models.FloatField(
        label='Your self-evaluation in %',
        min=0, max=100)
    evaluation3 = otree.api.models.FloatField(
        label='Your self-evaluation in %',
        min=0, max=100)

    choiceTShirt = otree.api.models.IntegerField(
        choices=[
            [1, 'T-Shirt Firm A'],
            [2, 'T-Shirt Firm B'],
            [3, 'T-Shirt Firm C'],
        ],
        widget=widgets.RadioSelect)

    priceTShirt = otree.api.models.CurrencyField()

    choiceCoffee = otree.api.models.IntegerField(
        choices=[
            [1, 'Coffee A'],
            [2, 'Coffee Firm B'],
            [3, 'Coffee Firm C'],
        ],
        widget=widgets.RadioSelect)

    priceCoffee = otree.api.models.CurrencyField()

    choiceMobile = otree.api.models.IntegerField(
        choices=[
            [1, 'Mobilephone A'],
            [2, 'Mobilephone B'],
            [3, 'Mobilephone C'],
        ],
        widget=widgets.RadioSelect)

    priceMobile = otree.api.models.CurrencyField()

    choiceContract = otree.api.models.IntegerField(
        choices=[
            [1, 'Contract A'],
            [2, 'Contract B'],
            [3, 'Contract C'],
        ],
        widget=widgets.RadioSelect)

    priceContract = otree.api.models.CurrencyField()

    choiceChair = otree.api.models.IntegerField(
        choices=[
            [1, 'Chair A'],
            [2, 'Chair B'],
            [3, 'Chair C'],
        ],
        widget=widgets.RadioSelect)

    priceChair = otree.api.models.CurrencyField()

    # def __init__(self: Absatz self.priceTShirt = c(18)

    def set_payoff(self):
        if self.choiceTShirt == 1:
            self.priceTShirt = otree.api.Currency(10)
        if self.choiceTShirt == 2:
            self.priceTShirt = otree.api.Currency(15)
        if self.choiceTShirt == 3:
            self.priceTShirt = otree.api.Currency(20)
        if self.choiceCoffee == 1:
            self.priceCoffee = otree.api.Currency(5)
        if self.choiceCoffee == 2:
            self.priceCoffee = otree.api.Currency(10)
        if self.choiceCoffee == 3:
            self.priceCoffee = otree.api.Currency(15)
        if self.choiceMobile == 1:
            self.priceMobile = otree.api.Currency(400)
        if self.choiceMobile == 2:
            self.priceMobile = otree.api.Currency(700)
        if self.choiceMobile == 3:
            self.priceMobile = otree.api.Currency(1000)
        if self.choiceContract == 1:
            self.priceContract = otree.api.Currency(20)
        if self.choiceContract == 2:
            self.priceContract = otree.api.Currency(40)
        if self.choiceContract == 3:
            self.priceContract = otree.api.Currency(60)
        if self.choiceChair == 1:
            self.priceChair = otree.api.Currency(50)
        if self.choiceChair == 2:
            self.priceChair = otree.api.Currency(150)
        if self.choiceChair == 3:
            self.priceChair = otree.api.Currency(250)

        if self.round_number == 3:
            self.payoff1 = Constants.endowment1 - self.priceTShirt - self.priceCoffee - self.priceMobile - self.priceContract - self.priceChair

        if self.round_number == 4:
            self.payoff2 = Constants.endowment2 - self.priceTShirt - self.priceCoffee - self.priceMobile - self.priceContract - self.priceChair

        if self.round_number == 5:
            self.payoff3 = Constants.endowment3 - self.priceTShirt - self.priceCoffee - self.priceMobile - self.priceContract - self.priceChair
