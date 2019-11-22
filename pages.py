
from otree.api import Currency as c, currency_range
from otree.models import player

from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.player.round_number == 1


class Evaluation(Page):
    def is_displayed(self):
        return self.player.round_number == 2

    form_model = 'player'
    form_fields = ['evaluation1', 'evaluation2', 'evaluation3']


class ChoiceEndowment1(Page):
    def is_displayed(self):
        return self.player.round_number == 3

    form_model = 'player'
    form_fields = ['choiceTShirt', 'choiceCoffee', 'choiceMobile', 'choiceContract', 'choiceChair']


class ChoiceEndowment2(Page):
    def is_displayed(self):
        return self.player.round_number == 4

    form_model = 'player'
    form_fields = ['choiceTShirt', 'choiceCoffee', 'choiceMobile', 'choiceContract', 'choiceChair']


class ChoiceEndowment3(Page):
    def is_displayed(self):
        return self.player.round_number == 5

    form_model = 'player'
    form_fields = ['choiceTShirt', 'choiceCoffee', 'choiceMobile', 'choiceContract', 'choiceChair']


class Results(Page):
    def is_displayed(self):
        return self.player.round_number == 6


# round number 1 - evaluation
# round number 2 -


page_sequence = [Introduction, Evaluation, ChoiceEndowment1, ChoiceEndowment2, ChoiceEndowment3, Results]
