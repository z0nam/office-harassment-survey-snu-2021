from otree.api import *


doc = """
사무금융노동자 직장내 괴롭힘 설문조사 - 시작화면
@date 2021.7.7
@author 서울대 사회학과 추지현 교수팀
@developer namun@snu.ac.kr  
"""


class Constants(BaseConstants):
    name_in_url = 'introduction_union'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Introduction(Page):
    pass


page_sequence = [Introduction]
