from otree.api import *


doc = """
5. 응답자 배경 정보
@date 2021.7.13
@author 서울대 사회학과 추지현 교수팀
@developer namun@snu.ac.kr 
"""


class Constants(BaseConstants):
    name_in_url = 'interview_request'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    phone_number = models.StringField(
        blank=True,
        label="비대면 화상 인터뷰가 가능할 경우 연락처 혹은 이메일을 남겨주세요. (사례비 있음)",
    )
    #다음은 개인 인적사항에 대한 질문입니다.



# PAGES
class InterviewRequest(Page):
    form_model = 'player'
    form_fields = [
        'phone_number',
    ]


page_sequence = [InterviewRequest]
