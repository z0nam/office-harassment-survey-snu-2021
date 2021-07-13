from otree.api import *
from GlobalConstants import GlobalConstants


doc = """
4. 관련 제도 운용 실태와 정책 수요
@date 2021.7.13
@author 서울대 사회학과 추지현 교수팀
@developer namun@snu.ac.kr 
"""


class Constants(BaseConstants):
    name_in_url = 'policy'
    players_per_group = None
    num_rounds = 1

    POL4_QUESTIONS = [
        "우리 직장은 직장내 괴롭힘이 발생할 가능성이 높다",
        "내가 향후 직장내 괴롭힘을 당한다 해도 우리 직장은 필요한 조치를 취해주지 않을 것이다. ",
        "직장내 괴롭힘을 문제 삼으면 결국 피해자만 손해 본다",
        "직장내 괴롭힘은 피해 그 자체보다 그 후 2차 피해가 더욱 심각하다.",
        "직장에서 피해 주장이 과도하게 이뤄지는 경우가 많다. ",
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field_pol4(index):
    return models.IntegerField(
        label=Constants.POL4_QUESTIONS[index-1],
        widget=widgets.RadioSelect,
        choices=GlobalConstants.L4_CHOICES,
    )


def make_field_pol5(order):
    return models.IntegerField(
        label="직장 내 괴롭힘에 대한 대응에 있어, 현재 가장 시급한 것은 무엇이라 생각하십니까? 세 가지를 골라 주세요.(%d순위)" % order,
        widget=widgets.RadioSelect,
        choices=[
            [1, "① 피해자 보호(가해자의 분리, 상담 지원, 휴식 부여, 불이익 조치 예방 등) 강화"],
            [2, "② 직장 내 괴롭힘 가해자에 대한 처벌 강화"],
            [3, "③ 피해자 비밀보호, 익명신고, 피해자 불이익 금지 등을 통한 신고 여건 마련"],
            [4, "④ 직장 내 괴롭힘 상담과 예방을 위한 창구 및 신고센터 설치"],
            [5, "⑤ 직장 내 괴롭힘에 대한 실태조사(정신건강 포함)나 예방 교육 "],
            [6, "⑥ 직장 내 괴롭힘 금지에 관한 내부 규정(단체협약, 취업규칙, 대응 매뉴얼 등) 마련과 홍보"],
            [7, "⑦ 사건이 무마, 은폐되지 않도록 직장 내 조사기구 구성의 독립성, 공정성, 전문성 강화 "],
            [8, "⑧ 기관장의 문제에 대한 인식 제고"],
            [9, "⑨ 노조의 대응 역량 및 역할 강화"],
            [10, "⑩ 직장 내 괴롭힘 관련 정부의 지도감독 강화"],
            [11, "⑪ 성차별적, 권위적 조직 문화 개선"],
            [12, "⑫ 기타(직접입력)"],
        ]
    )


class Player(BasePlayer):
    # 귀하의 직장은 직장 내 괴롭힘 예방 및 해결을 위한 어떤 노력을 하고 있습니까? 알고 계신 모든 것을 선택해 주십시오.
    pol1_1 = models.BooleanField(
        label="① 상담 창구가 설치되어 있다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    pol1_2 = models.BooleanField(
        label="② 취업규칙 등의 내부규정이 있다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    pol1_3 = models.BooleanField(
        label="③ 직장 내 괴롭힘에 대한 교육을 하고 있다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    pol1_4 = models.BooleanField(
        label="④ 직장 내 괴롭힘 관련 자료를 배포하거나 게시한다 .",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    pol1_5 = models.BooleanField(
        label="⑤ 면담이나 설문조사 등을 통해 실태를 파악한다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    pol1_6 = models.BooleanField(
        label="⑥ 도움을 받을 수 있는 공적기관 정보를 제공하고 있다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    pol1_7 = models.BooleanField(
        label="⑦ 모르겠다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    pol2 = models.IntegerField(
        label="지난 2년간 직장내 괴롭힘 예방 교육(성희롱 예방 교육, 폭력예방교육 제외)을 받은 적이 있습니까?",
        widget=widgets.RadioSelect,
        choices=GlobalConstants.YNU_CHOICES,
    )

    pol3 = models.IntegerField(
        label="귀하의 노동조합은 직원의 고민, 불만, 고충, 갈등 등을 상담해 주거나 해결을 위한 지원을 하고 있습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "지원하고 있지 않다"],
            [2, "지원하고 있다"],
            [3, "모른다"],
        ]
    )

    pol4_1 = make_field_pol4(1)
    pol4_2 = make_field_pol4(2)
    pol4_3 = make_field_pol4(3)
    pol4_4 = make_field_pol4(4)
    pol4_5 = make_field_pol4(5)

    pol5_1st = make_field_pol5(1)
    pol5_1st_op = models.LongStringField(
        label="",
        blank=True,
    )
    pol5_2nd = make_field_pol5(2)
    pol5_2nd_op = models.LongStringField(
        label="",
        blank=True,
    )
    pol5_3rd = make_field_pol5(3)
    pol5_3rd_op = models.LongStringField(
        label="",
        blank=True,
    )

    pol6 = models.LongStringField(
        label="기타 직장 내 괴롭힘 또는 본 설문조사와 관련하여 하고 싶은 의견이 있으시면 자유롭게 작성해 주십시오.",
        blank=True,
    )


# PAGES
class Policy(Page):
    form_model = 'player'
    form_fields = [
        'pol1_1',
        'pol1_2',
        'pol1_3',
        'pol1_4',
        'pol1_5',
        'pol1_6',
        'pol1_7',
        'pol2',
        'pol3',
        'pol4_1',
        'pol4_2',
        'pol4_3',
        'pol4_4',
        'pol4_5',
        'pol5_1st',
        'pol5_1st_op',
        'pol5_2nd',
        'pol5_2nd_op',
        'pol5_3rd',
        'pol5_3rd_op',
        'pol6',
    ]

    @staticmethod
    def vars_for_template(player):
        return{
            'INIT': 10,
            'END': 10+len(Constants.POL4_QUESTIONS),
            'L4_CHOICES': [i[1] for i in GlobalConstants.L4_CHOICES]
        }


page_sequence = [Policy]
