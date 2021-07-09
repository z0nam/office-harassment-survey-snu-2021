from otree.api import *
from GlobalConstants import GlobalConstants
from . import culture_questions

doc = """
직장문화에 대한 평가
@date 2021.7.7
@author 서울대 사회학과 추지현 교수팀
@developer namun@snu.ac.kr 
"""


class Constants(BaseConstants):
    name_in_url = 'culture'
    players_per_group = None
    num_rounds = 1

    L4_CHOICES = GlobalConstants.L4_CHOICES

    CULTURE_QUESTIONS = culture_questions.CULTURE
    ENVIRONMENT_QUESTIONS = culture_questions.ENVIRONMENT_CHANGE


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field_culture(index):
    return models.IntegerField(
        label=Constants.CULTURE_QUESTIONS[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_CHOICES,
    )


def make_field_environment(index):
    return models.IntegerField(
        label=Constants.ENVIRONMENT_QUESTIONS[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_CHOICES,
    )


class Player(BasePlayer):
    culture_1 = make_field_culture(1)
    culture_2 = make_field_culture(2)
    culture_3 = make_field_culture(3)
    culture_4 = make_field_culture(4)
    culture_5 = make_field_culture(5)
    culture_6 = make_field_culture(6)
    culture_7 = make_field_culture(7)
    culture_8 = make_field_culture(8)

    env_1 = make_field_environment(1)
    env_2 = make_field_environment(2)
    env_3 = make_field_environment(3)
    env_4 = make_field_environment(4)
    env_5 = make_field_environment(5)
    env_6 = make_field_environment(6)
    env_7 = make_field_environment(7)
    env_8 = make_field_environment(8)
    env_9 = make_field_environment(9)
    


# PAGES
class Culture(Page):
    form_model = 'player'
    form_fields = [
        'culture_1',
        'culture_2',
        'culture_3',
        'culture_4',
        'culture_5',
        'culture_6',
        'culture_7',
        'culture_8',
    ]

    @staticmethod
    def vars_for_template(player):
        return {
            'CULTURE_INIT': 1,
            'CULTURE_END': len(Constants.CULTURE_QUESTIONS),
            'L4_CHOICES': [i[1] for i in Constants.L4_CHOICES]
        }


class Environment(Page):
    form_model = 'player'
    form_fields = [
        'env_1',
        'env_2',
        'env_3',
        'env_4',
        'env_5',
        'env_6',
        'env_7',
        'env_8',
        'env_9',
    ]

    @staticmethod
    def vars_for_template(player):
        return{
            'ENV_INIT': 1,
            'ENV_END': len(Constants.ENVIRONMENT_QUESTIONS),
            'L4_CHOICES': [i[1] for i in Constants.L4_CHOICES],
        }


page_sequence = [Culture, Environment]
