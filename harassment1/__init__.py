from otree.api import *
from . import har1_questions
from GlobalConstants import GlobalConstants

doc = """
직장문화에 대한 평가
@date 2021.7.7
@author 서울대 사회학과 추지현 교수팀
@developer namun@snu.ac.kr 
"""


class Constants(BaseConstants):
    name_in_url = 'harassment1'
    players_per_group = None
    num_rounds = 1

    HAR1_QUESTIONS = har1_questions.HAR1_QUESTIONS


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field_har1_experienced(index):
    return models.BooleanField(
        label=Constants.HAR1_QUESTIONS[index - 1],
        widget=widgets.CheckboxInput,
        blank=True,
    )


def make_field_har1_seen(index):
    return models.BooleanField(
        label=Constants.HAR1_QUESTIONS[index - 1],
        widget=widgets.CheckboxInput,
        blank=True,
    )


def make_field_har1_7(order):
    return models.IntegerField(
        label="귀하가 피해 이후 개인적으로 감내하거나 적극적인 조치를 취하지 않은 이유는 무엇입니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "① 문제를 제기할만큼 심각한 것은 아니거나 일상에서 흔한 일이라서"],
            [2, "② 나만 이상한 사람, 분란을 일으킨 사람으로 여겨질 것 같아서"],
            [3, "③ 업무능력 부족, 실수 등 나에게 책임이 있다고 생각해서"],
            [4, "④ 직장 내에서 피해 사실이 공개될까봐"],
            [5, "⑤ 알려도 공정하게 사건이 처리되지 않거나 상황이 개선되지 않을 것 같아서"],
            [6, "⑥ 조치를 취할 수 있는 방법을 모르거나 담당 기구를 몰라서"],
            [7, "⑦ 직장 내 괴롭힘에 대해 상담하기 어려운 분위기 때문에"],
            [8, "⑧ 직무 배치, 평가, 승진, 해고, 근로계약연장, 정규직 전환 등 인사상 불이익이 우려돼서"],
            [9, "⑨ 기타( 직접입력 )"],
        ]
    )


def make_field_har1_13(order):
    return models.IntegerField(
        label="귀하가 경험한 위 피해가 발생하게 된 가장 주된 원인은 무엇이라 생각합니까? 순서대로 두가지를 뽑아 주십시오.",
        widget=widgets.RadioSelect,
        choices=[
            [1, "① 직장의 경영정책(인력감축, 고객서비스정책 등)"],
            [2, "② 실적과 성과를 강조하는 직장 분위기"],
            [3, "③ 성차별적 조직 문화"],
            [4, "④ 상명하복의 조직 문화"],
            [5, "⑤ 열악한 근무 여건과 과도한 업무로 인한 스트레스"],
            [6, "⑥ 고용 불안정"],
            [7, "⑦ 가해자 개인의 인성 문제"],
            [8, "⑧ 내 잘못"],
            [9, "⑨ 기타 (직접입력)"],
        ]
    )


def make_field_har1s_8(order):
    return models.IntegerField(
        label="위 상황을 목격한 후 피해자를 돕거나 직장에 적극적인 조치를 취하지 않은 이유는 무엇입니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "① 문제를 제기할만큼 심각한 것은 아니거나 일상에서 흔한 일이라 생각해서 "],
            [2, "② 피해자와 함께 이상한 사람, 분란을 일으킨 사람으로 여겨질 것 같아서	"],
            [3, "③ 업무능력 부족, 실수 등 피해자에게도 책임이 있다고 생각해서"],
            [4, "④ 피해자가 원하지 않을 것 같아서"],
            [5, "⑤ 알려도 공정하게 사건이 처리되지 않거나 상황이 개선되지 않을 것 같아서"],
            [6, "⑥ 딱히 도와줄 방법을 모르거나 담당 기구를 몰라서"],
            [7, "⑦ 직장내 괴롭힘에 대하여 문제제기를 하기 어려운 분위기 때문에"],
            [8, "⑧ 나까지 직무 배치, 평가, 승진, 해고, 근로계약연장, 정규직 전환 등 인사상 불이익을 받을까봐"],
            [9, "⑨ 남의 일에 관여할 이유가 없어서"],
        ]
    )


def make_field_har1s_12(order):
    return models.IntegerField(
        label="귀하가 목격한 상황이 발생하게 된 가장 주된 원인은 무엇이라 생각합니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "① 직장의 경영정책(인력감축, 고객서비스정책 등)"],
            [2, "② 실적과 성과를 강조하는 직장 분위기 "],
            [3, "③ 성차별적 조직 문화"],
            [4, "④ 상명하복의 조직 문화"],
            [5, "⑤ 열악한 근무 여건과 과도한 업무로 인한 스트레스"],
            [6, "⑥ 고용 불안정"],
            [7, "⑦ 가해자 개인의 인성 문제"],
            [8, "⑧ 피해자 잘못"],
            [9, "⑨ 기타 (직접입력)"],
        ]
    )


class Player(BasePlayer):
    har1_experienced_1 = make_field_har1_experienced(1)
    har1_experienced_2 = make_field_har1_experienced(2)
    har1_experienced_3 = make_field_har1_experienced(3)
    har1_experienced_4 = make_field_har1_experienced(4)
    har1_experienced_5 = make_field_har1_experienced(5)
    har1_experienced_6 = make_field_har1_experienced(6)
    har1_experienced_7 = make_field_har1_experienced(7)
    har1_experienced_8 = make_field_har1_experienced(8)
    har1_experienced_9 = make_field_har1_experienced(9)
    har1_experienced_10 = make_field_har1_experienced(10)
    har1_experienced_11 = make_field_har1_experienced(11)
    har1_experienced_12 = make_field_har1_experienced(12)
    har1_experienced_13 = make_field_har1_experienced(13)
    har1_experienced_14 = make_field_har1_experienced(14)
    har1_experienced_15 = make_field_har1_experienced(15)
    har1_experienced_16 = make_field_har1_experienced(16)
    har1_experienced_17 = make_field_har1_experienced(17)
    har1_experienced_18 = make_field_har1_experienced(18)
    har1_experienced_19 = make_field_har1_experienced(19)
    har1_experienced_20 = make_field_har1_experienced(20)
    har1_experienced_21 = make_field_har1_experienced(21)
    har1_experienced_22 = make_field_har1_experienced(22)
    har1_experienced_23 = make_field_har1_experienced(23)
    har1_experienced_24 = make_field_har1_experienced(24)
    har1_experienced_25 = make_field_har1_experienced(25)
    har1_experienced_26 = make_field_har1_experienced(26)
    har1_experienced_27 = make_field_har1_experienced(27)
    har1_experienced_28 = make_field_har1_experienced(28)
    har1_experienced_29 = make_field_har1_experienced(29)
    har1_experienced_30 = make_field_har1_experienced(30)
    har1_experienced_31 = make_field_har1_experienced(31)

    har1_seen_1 = make_field_har1_seen(1)
    har1_seen_2 = make_field_har1_seen(2)
    har1_seen_3 = make_field_har1_seen(3)
    har1_seen_4 = make_field_har1_seen(4)
    har1_seen_5 = make_field_har1_seen(5)
    har1_seen_6 = make_field_har1_seen(6)
    har1_seen_7 = make_field_har1_seen(7)
    har1_seen_8 = make_field_har1_seen(8)
    har1_seen_9 = make_field_har1_seen(9)
    har1_seen_10 = make_field_har1_seen(10)
    har1_seen_11 = make_field_har1_seen(11)
    har1_seen_12 = make_field_har1_seen(12)
    har1_seen_13 = make_field_har1_seen(13)
    har1_seen_14 = make_field_har1_seen(14)
    har1_seen_15 = make_field_har1_seen(15)
    har1_seen_16 = make_field_har1_seen(16)
    har1_seen_17 = make_field_har1_seen(17)
    har1_seen_18 = make_field_har1_seen(18)
    har1_seen_19 = make_field_har1_seen(19)
    har1_seen_20 = make_field_har1_seen(20)
    har1_seen_21 = make_field_har1_seen(21)
    har1_seen_22 = make_field_har1_seen(22)
    har1_seen_23 = make_field_har1_seen(23)
    har1_seen_24 = make_field_har1_seen(24)
    har1_seen_25 = make_field_har1_seen(25)
    har1_seen_26 = make_field_har1_seen(26)
    har1_seen_27 = make_field_har1_seen(27)
    har1_seen_28 = make_field_har1_seen(28)
    har1_seen_29 = make_field_har1_seen(29)
    har1_seen_30 = make_field_har1_seen(30)
    har1_seen_31 = make_field_har1_seen(31)

    # HAR1

    har1_experienced_critical = models.IntegerField(
        min=1,
        max=len(Constants.HAR1_QUESTIONS),
        widget=widgets.RadioSelect,
    )

    har1_3 = models.IntegerField(
        label="응답하신 행위의 가해자는 귀하와 어떤 관계였습니까? 가해자가 여럿인 경우 주된 가해자를 기준으로 응답해주십시오.",
        widget=widgets.RadioSelect,
        choices=[
            [1, "상사"],
            [2, "동료"],
            [3, "부하"],
            [4, "누군지 모름"],
        ]
    )

    # Har1_1

    har1_4 = models.IntegerField(
        label="그 가해자의 성별은 무엇입니까? 여럿인 경우 주된 가해자를 기준으로 응답해주십시오",
        widget=widgets.RadioSelect,
        choices=GlobalConstants.GENDER_CHOICES,
    )

    # Har1_1_plus

    har1_5_1 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="오프라인에서",
        blank=True,
    )

    har1_5_2 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label=" 온라인을 통해(사내 전산망, SNS, 문자, 전화 등)",
        blank=True,
    )

    har1_6_1 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="① 아무에게도 이야기하지 않았다",
        blank=True,
    )

    har1_6_2 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="② 주변 동료에게 알렸다",
        blank=True,
    )

    har1_6_3 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="③ 잠시 휴직을 하거나 휴가를 가졌다",
        blank=True,
    )

    har1_6_4 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="④ 스스로 부서나 근무지를 이동했다",
        blank=True,
    )

    har1_6_5 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑤ 상사나 부서장 등에게 상담했다.",
        blank=True,
    )

    har1_6_6 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑥ 노동조합에 알리고 상담했다.",
        blank=True,
    )

    har1_6_7 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑦ 직장 내 고충처리절차를 이용했다",
        blank=True,
    )

    har1_6_8 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑧ 가해자에게 직접 문제를 제기하였다",
        blank=True,
    )

    har1_6_9 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑨ 직장 외부의 민간단체(고용평등상담실, 갑질119 등)나 공공기관(고용노동부, 국가인권위원회 등)등에 상담 혹은 신고를 했다.",
        blank=True,
    )

    har1_6_10 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑩ 소송 등 법적인 구제절차를 취했다",
        blank=True,
    )

    har1_6_op = models.LongStringField(
        label="⑪ 기타(직접입력)",
        blank=True,
    )

    # HAR1_2

    har1_7_1st = make_field_har1_7(1)
    har1_7_1st_op = models.LongStringField(
        blank=True,
        label="",
    )
    har1_7_2nd = make_field_har1_7(2)
    har1_7_2nd_op = models.LongStringField(
        blank=True,
        label="",
    )
    har1_7_3rd = make_field_har1_7(3)
    har1_7_3rd_op = models.LongStringField(
        blank=True,
        label="",
    )

    # HAR1_3

    har1_8_1 = models.BooleanField(
        label="① 아무런 조치가 없었다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_8_2 = models.BooleanField(
        label="② 행위자가 사과하도록 했다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_8_3 = models.BooleanField(
        label="③ 행위자에게 인사조치가 있었다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_8_4 = models.BooleanField(
        label="④ 피해자인 나와 행위자를 분리했다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_8_5 = models.BooleanField(
        label="⑤ 예방 교육이나 지침 안내 등 해당사안과 관련해 직장 교육을 했다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_8_6 = models.BooleanField(
        label="⑥ 피해에 대한 금전적 보상이 이루어지도록 했다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_8_7 = models.BooleanField(
        label="⑦ 상담이나 치료, 유급 휴직 등 지원을 해주었다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_8_8 = models.BooleanField(
        label="⑧ 조사 결과를 내게 알려주었다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_8_9 = models.BooleanField(
        label="⑨ 사건 종결과 처리를 미루었다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_8_op = models.LongStringField(
        label="⑩ 기타(직접입력)",
        blank=True,
    )

    # Har1_4

    har1_9 = models.IntegerField(
        label="피해 상황은 이후 귀하가 원치 않았던 직장 구성원들에게까지 알려지게 되었습니까? ",
        widget=widgets.RadioSelect,
        choices=GlobalConstants.YNU_CHOICES,
    )

    # Har1_5

    har1_10_1 = models.BooleanField(
        label="① 피해가 남들이 보는 앞에서 혹은 행정절차(성과평가, 승진, 휴가 등)를 통해 공공연히 이뤄져서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_10_2 = models.BooleanField(
        label="② 피해 이후 직장동료, 노조, 상담기구 등을 통한 상담이나 하소연하는 과정에서 소문이 나서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_10_3 = models.BooleanField(
        label="③ 고충처리나 직장으로부터의 지원 등 문제제기 절차를 진행하는 과정(조사, 피해자의 휴가 사용 등을 통해서)에서 비밀보호가 제대로 되지 않아서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_10_4 = models.BooleanField(
        label="④ 가해자가 먼저 제멋대로 소문을 내고 다녀서 ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_10_5 = models.BooleanField(
        label="⑤ 가해자에 대한 징계나 조치(피해자와의 공간분리, 배치이동 등) 과정에서 소문이 나서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_10_op = models.LongStringField(
        label="⑥ 기타(직접입력)",
        blank=True,
    )

    # Har1_6

    har1_11_1 = models.BooleanField(
        label="① 직장에 문제제기하거나 분란을 만들었다는 이유로 비난을 받음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_11_2 = models.BooleanField(
        label="② 악의적으로 가해자를 신고했다거나 나에게 잘못이 있는 것처럼 오해받거나 소문에 시달림",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_11_3 = models.BooleanField(
        label="③ 사람들이 나를 피하거나 따돌림",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_11_4 = models.BooleanField(
        label="④ 다른 유사사건이 생기거나 논의될 때마다 나의 피해 사례를 굳이 반복해 거론함",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_11_5 = models.BooleanField(
        label="⑤ 분란을 만들지 말고 조용히 넘어가기를 강요받거나 참으라는 얘기를 들음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_11_6 = models.BooleanField(
        label="⑥ 내 조력자에게 해고, 징계, 고용, 업무상 불이익 등을 주거나 끼어들지 말라고 회유, 강요하는 등 괴롭힘이 가해짐",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    #har1_6_2

    har1_11_7 = models.BooleanField(
        label="⑦ 회사가 인사상 불이익 처우를 암시하며 사건을 축소 또는 은폐하려 함",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_11_8 = models.BooleanField(
        label="⑧ 회사가 가해자와의 합의를 종용함",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_11_9 = models.BooleanField(
        label="⑨ 과도한 업무 혹은 다른 업무를 부여받거나 업무를 부여받지 못함",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_11_10 = models.BooleanField(
        label="⑩ 회사가 가해자가 아닌 나만 부서이동을 시킴",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_11_11 = models.BooleanField(
        label="⑪ 근무평가, 승진, 근로계약 갱신 거절 등 인사상 부당한 대우나 불이익을 받음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    #har1_7

    har1_12_1 = models.BooleanField(
        label="① 근무 의욕, 업무 능력, 집중도가 떨어졌다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_12_2 = models.BooleanField(
        label="② 상급자나 직장에 대한 신뢰가 떨어졌다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_12_3 = models.BooleanField(
        label="③ 또 피해를 당할까봐 직장 동료들과 관계 맺는 것이 이전보다 조심스러워졌다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_12_4 = models.BooleanField(
        label="④ 분노나 불안감, 우울, 무력감, 감정조절 및 수면에 어려움을 느꼈다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_12_5 = models.BooleanField(
        label="⑤ 특별한 영향은 없었다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1_13_1st = make_field_har1_13(1)
    har1_13_2nd = make_field_har1_13(2)
    har1_13_1st_op = models.LongStringField(
        label="",
        blank=True,
    )
    har1_13_2nd_op = models.LongStringField(
        label="",
        blank=True,
    )

    # Har1s.html

    har1_seen_critical = models.IntegerField(
        min=1,
        max=len(Constants.HAR1_QUESTIONS),
        widget=widgets.RadioSelect,
    )

    har1s_3 = models.IntegerField(
        label="응답하신 행위는 누가(가해자)가 누구에게(피해자) 한 것이었습니까? 여럿인 경우 주된 가해자와 피해자의 관계를 기준으로 응답해주십시오.",
        widget=widgets.RadioSelect,
        choices=[
            [1, "① 상사가 부하직원에게"],
            [2, "② 동료끼리"],
            [3, "③ 부하직원이 상사에게"],
            [4, "④ 가해자가 누구인지 모름"],
        ]
    )

    # Har1s_2

    har1s_4 = models.IntegerField(
        label="가해자의 성별은 무엇입니까? 여럿인 경우 주된 가해자를 기준으로 응답해주십시오.",
        widget=widgets.RadioSelect,
        choices=GlobalConstants.GENDER_CHOICES,
    )

    # Har1s_3

    har1s_5 = models.IntegerField(
        label="피해자의 성별은 무엇입니까? 여럿인 경우 주된 피해자를 기준으로 응답해주십시오.",
        widget=widgets.RadioSelect,
        choices=GlobalConstants.GENDER_CHOICES,
    )

    har1s_6_1 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="오프라인에서",
        blank=True,
    )

    har1s_6_2 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label=" 온라인을 통해(사내 전산망, SNS, 문자, 전화 등)",
        blank=True,
    )

    har1s_7_1 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="① 아무에게도 이야기하지 않았다",
        blank=True,
    )

    har1s_7_2 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="② 주변 동료에게 알렸다",
        blank=True,
    )

    har1s_7_3 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="③ 피해자를 위로하거나 조언했다. ",
        blank=True,
    )

    har1s_7_4 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="④ 가해자에게 직접 문제를 제기하거나 말렸다. ",
        blank=True,
    )

    har1s_7_5 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑤ 상사나 부서장 등에게 상담했다.",
        blank=True,
    )

    har1s_7_6 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑥ 노동조합에 알리고 상담했다.",
        blank=True,
    )

    har1s_7_7 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑦ 직장 내 상담창구나 고충처리절차를 이용했다",
        blank=True,
    )

    # har1s_7_8 = models.BooleanField(
    #     widget=widgets.CheckboxInput,
    #     label="⑧ 기타(직접입력)",
    #     blank=True,
    # )

    har1s_7_op = models.LongStringField(
        label="⑧ 기타(직접입력)",
        blank=True,
    )

    # Har1s_4

    har1s_8_1st = make_field_har1s_8(1)
    har1s_8_2nd = make_field_har1s_8(2)
    har1s_8_3rd = make_field_har1s_8(3)

    # Har1s_5

    har1s_9 = models.IntegerField(
        label="피해 상황은 이후 귀하가 원치 않았던 직장 구성원들에게까지 알려지게 되었습니까? ",
        widget=widgets.RadioSelect,
        choices=GlobalConstants.YNU_CHOICES,
    )

    # Har1s_6

    har1s_10_1 = models.BooleanField(
        label="① 피해가 남들이 보는 앞에서 혹은 행정절차(성과평가, 승진, 휴가 등)를 통해 공공연히 이뤄져서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1s_10_2 = models.BooleanField(
        label="② 피해자가 직장동료, 노조, 상담기구 등을 통한 상담이나 하소연하는 과정에서 소문이 나서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1s_10_3 = models.BooleanField(
        label="③ 고충처리나 직장으로부터의 지원 등 문제제기 절차를 진행하는 과정(조사,  피해자의 휴가 사용 등을 통해서)에서 비밀보호가 제대로 되지 않아서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1s_10_4 = models.BooleanField(
        label="④ 가해자가 먼저 제멋대로 소문을 내고 다녀서 ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1s_10_5 = models.BooleanField(
        label="⑤ 가해자에 대한 징계나 조치(피해자와의 공간분리, 배치이동 등) 과정에서 소문이 나서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    # har1s_10_6 = models.BooleanField(
    #     label="⑥ 기타________________ ",
    #     widget=widgets.CheckboxInput,
    #     blank=True,
    # )

    har1s_10_op = models.LongStringField(
        label="⑥ 기타(직접입력)",
        blank=True,
    )

    # Har1s_7

    har1s_11_1 = models.BooleanField(
        label="① 근무 의욕, 업무 능력, 집중도가 떨어졌다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1s_11_2 = models.BooleanField(
        label="② 상급자나 직장에 대한 신뢰가 떨어졌다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1s_11_3 = models.BooleanField(
        label="③ 나도 피해를 경험하게 될까봐 직장 동료들과 관계 맺는 것이 이전보다 조심스러워졌다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1s_11_4 = models.BooleanField(
        label="④ 내가 가해자로 지목될 수도 있을까봐 직장 동료들과 선별적으로 관계를 맺게 되었다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1s_11_5 = models.BooleanField(
        label="⑤ 특별한 영향은 없었다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har1s_12_1st = make_field_har1s_12(1)
    har1s_12_2nd = make_field_har1s_12(2)
    har1s_12_1st_op = models.LongStringField(
        label="",
        blank=True,
    )
    har1s_12_2nd_op = models.LongStringField(
        label="",
        blank=True,
    )


################################## PAGES ######################################################

class Experience(Page):
    form_model = 'player'
    form_fields = [
        'har1_experienced_1',
        'har1_seen_1',
        'har1_experienced_2',
        'har1_seen_2',
        'har1_experienced_3',
        'har1_seen_3',
        'har1_experienced_4',
        'har1_seen_4',
        'har1_experienced_5',
        'har1_seen_5',
        'har1_experienced_6',
        'har1_seen_6',
        'har1_experienced_7',
        'har1_seen_7',
        'har1_experienced_8',
        'har1_seen_8',
    ]

    @staticmethod
    def vars_for_template(player):
        return {
            'INIT': 1,
            'END': len(Experience.form_fields) / 2,
        }


class Experience2(Page):
    form_model = 'player'
    form_fields = [
        'har1_experienced_9',
        'har1_seen_9',
        'har1_experienced_10',
        'har1_seen_10',
        'har1_experienced_11',
        'har1_seen_11',
        'har1_experienced_12',
        'har1_seen_12',
        'har1_experienced_13',
        'har1_seen_13',
        'har1_experienced_14',
        'har1_seen_14',
    ]

    @staticmethod
    def vars_for_template(player):
        return {
            'INIT': 1,
            'END': len(Experience2.form_fields) / 2,
        }


class Experience3(Page):
    form_model = 'player'
    form_fields = [
        'har1_experienced_15',
        'har1_seen_15',
        'har1_experienced_16',
        'har1_seen_16',
        'har1_experienced_17',
        'har1_seen_17',
        'har1_experienced_18',
        'har1_seen_18',
        'har1_experienced_19',
        'har1_seen_19',
    ]

    @staticmethod
    def vars_for_template(player):
        return {
            'INIT': 1,
            'END': len(Experience3.form_fields) / 2,
        }


class Experience4(Page):
    form_model = 'player'
    form_fields = [
        'har1_experienced_20',
        'har1_seen_20',
        'har1_experienced_21',
        'har1_seen_21',
        'har1_experienced_22',
        'har1_seen_22',
        'har1_experienced_23',
        'har1_seen_23',
    ]

    @staticmethod
    def vars_for_template(player):
        return {
            'INIT': 1,
            'END': len(Experience4.form_fields) / 2,
        }


class Experience5(Page):
    form_model = 'player'
    form_fields = [
        'har1_experienced_24',
        'har1_seen_24',
        'har1_experienced_25',
        'har1_seen_25',
        'har1_experienced_26',
        'har1_seen_26',
        'har1_experienced_27',
        'har1_seen_27',
        'har1_experienced_28',
        'har1_seen_28',
        'har1_experienced_29',
        'har1_seen_29',
        'har1_experienced_30',
        'har1_seen_30',
        'har1_experienced_31',
        'har1_seen_31',
    ]

    @staticmethod
    def vars_for_template(player):
        return {
            'INIT': 1,
            'END': len(Experience5.form_fields) / 2,
        }


class Har1(Page):
    form_model = 'player'
    form_fields = [
        'har1_experienced_critical',
        'har1_3',
    ]

    @staticmethod
    def vars_for_template(player):
        return {
            'CASE': player.participant.HAR1_CASE,
            'EXPERIENCED_INDICES': player.participant.HAR1_EXPERIENCED_INDICES,
            'EXPERIENCED_LIST': player.participant.HAR1_EXPERIENCED_LIST,
            'SEEN_INDICES': player.participant.HAR1_SEEN_INDICES,
            'SEEN_LIST': player.participant.HAR1_SEEN_LIST,
        }

    @staticmethod
    def is_displayed(player):
        # Experience.html  이 실행되고 한 번 정리해야 하는데 여기 말고 정리할 수 있는 곳을 찾을 수 없다.
        # 코드 스멜이 나지만 일단 여기다 쓰자.

        player.participant.HAR1_EXPERIENCED_INDICES = [
            player.har1_experienced_1,
            player.har1_experienced_2,
            player.har1_experienced_3,
            player.har1_experienced_4,
            player.har1_experienced_5,
            player.har1_experienced_6,
            player.har1_experienced_7,
            player.har1_experienced_8,
            player.har1_experienced_9,
            player.har1_experienced_10,
            player.har1_experienced_11,
            player.har1_experienced_12,
            player.har1_experienced_13,
            player.har1_experienced_14,
            player.har1_experienced_15,
            player.har1_experienced_16,
            player.har1_experienced_17,
            player.har1_experienced_18,
            player.har1_experienced_19,
            player.har1_experienced_20,
            player.har1_experienced_21,
            player.har1_experienced_22,
            player.har1_experienced_23,
            player.har1_experienced_24,
            player.har1_experienced_25,
            player.har1_experienced_26,
            player.har1_experienced_27,
            player.har1_experienced_28,
            player.har1_experienced_29,
            player.har1_experienced_30,
            player.har1_experienced_31,
        ]

        player.participant.HAR1_SEEN_INDICES = [
            player.har1_seen_1,
            player.har1_seen_2,
            player.har1_seen_3,
            player.har1_seen_4,
            player.har1_seen_5,
            player.har1_seen_6,
            player.har1_seen_7,
            player.har1_seen_8,
            player.har1_seen_9,
            player.har1_seen_10,
            player.har1_seen_11,
            player.har1_seen_12,
            player.har1_seen_13,
            player.har1_seen_14,
            player.har1_seen_15,
            player.har1_seen_16,
            player.har1_seen_17,
            player.har1_seen_18,
            player.har1_seen_19,
            player.har1_seen_20,
            player.har1_seen_21,
            player.har1_seen_22,
            player.har1_seen_23,
            player.har1_seen_24,
            player.har1_seen_25,
            player.har1_seen_26,
            player.har1_seen_27,
            player.har1_seen_28,
            player.har1_seen_29,
            player.har1_seen_30,
            player.har1_seen_31,
        ]

        player.participant.HAR1_EXPERIENCED_LIST = [[i + 1, Constants.HAR1_QUESTIONS[i]] for i, value in
                                                    enumerate(player.participant.HAR1_EXPERIENCED_INDICES) if value]
        player.participant.HAR1_SEEN_LIST = [[i + 1, Constants.HAR1_QUESTIONS[i]] for i, value in
                                             enumerate(player.participant.HAR1_SEEN_INDICES) if value]

        total_number_of_experienced = sum(player.participant.HAR1_EXPERIENCED_INDICES)
        total_number_of_seen = sum(player.participant.HAR1_SEEN_INDICES)

        # print("total_number_of_experienced is ", total_number_of_experienced)
        # print("total_number_of_seen is ", total_number_of_seen)

        return_value = False
        case = "NOT_ASSIGNED_THIS_MEANS_ERROR"

        if total_number_of_experienced >= 2:
            case = "E2"
            return_value = True
            player.participant.HAR1_EXP_GOGO = True
        elif total_number_of_experienced == 1:
            case = "E3"
            return_value = True
            player.participant.HAR1_EXP_GOGO = True
        elif total_number_of_seen >= 2:
            case = "S2"
            player.participant.HAR1_EXP_GOGO = False
        elif total_number_of_seen == 1:
            case = "S3"
            player.participant.HAR1_EXP_GOGO = False
        else:
            case = "PASS"
            player.participant.HAR1_EXP_GOGO = False

        player.participant.HAR1_CASE = case

        return return_value


def har1_experienced_critical_choices(player):
    print(player.participant.HAR1_EXPERIENCED_LIST)
    choices = [
        v for i, v in enumerate(player.participant.HAR1_EXPERIENCED_LIST)
    ]
    return choices


def har1_seen_critical_choices(player):
    choices = [
        v for i, v in enumerate(player.participant.HAR1_SEEN_LIST)
    ]
    return choices


class Har1_1(Page):
    form_model = 'player'
    form_fields = [
        'har1_4',
    ]

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        elif not player.participant.HAR1_EXP_GOGO:
            return False
        elif player.har1_3 == 4:
            return False
        else:
            return True


class Har1_1_plus(Page):
    form_model = 'player'
    form_fields = [
        'har1_5_1',
        'har1_5_2',
        'har1_6_1',
        'har1_6_2',
        'har1_6_3',
        'har1_6_4',
        'har1_6_5',
        'har1_6_6',
        'har1_6_7',
        'har1_6_8',
        'har1_6_9',
        'har1_6_10',
        'har1_6_op',
    ]

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        elif not player.participant.HAR1_EXP_GOGO:
            return False
        else:
            return True


class Har1_2(Page):
    form_model = 'player'
    form_fields = [
        'har1_7_1st',
        'har1_7_2nd',
        'har1_7_3rd',
        'har1_7_1st_op',
        'har1_7_2nd_op',
        'har1_7_3rd_op',
    ]

    @staticmethod
    def vars_for_template(player):
        return {
            'EXPERIENCED_INDICES': player.participant.HAR1_EXPERIENCED_INDICES,
            'EXPERIENCED_LIST': player.participant.HAR1_EXPERIENCED_LIST,
            'SEEN_LIST': player.participant.HAR1_SEEN_INDICES,
            'PARTICIPANT_VALUES': player.participant.HAR1_CASE,
        }

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if not player.participant.HAR1_EXP_GOGO:
            return False
        har1_6_list = [
            player.har1_6_1,
            player.har1_6_2,
            player.har1_6_3,
            player.har1_6_4,
            player.har1_6_5,
            player.har1_6_6,
            player.har1_6_7,
            player.har1_6_8,
            player.har1_6_9,
            player.har1_6_10,
        ]
        if player.har1_6_1 == True or (
                player.har1_6_2 == False and
                player.har1_6_5 == False and
                player.har1_6_6 == False and
                player.har1_6_7 == False and
                player.har1_6_8 == False and
                player.har1_6_9 == False and
                player.har1_6_10 == False
        ):
            player.participant.HAR1_8 = False
            return True
        elif (
                player.har1_6_5 == True or
                player.har1_6_6 == True or
                player.har1_6_7 == True or
                player.har1_6_8 == True or
                player.har1_6_9 == True or
                player.har1_6_10 == True
        ):
            player.participant.HAR1_8 = True
            return False
        else:
            player.participant.HAR1_8 = False
            return False


class Har1_3(Page):
    form_model = 'player'
    form_fields = [
        'har1_8_1',
        'har1_8_2',
        'har1_8_3',
        'har1_8_4',
        'har1_8_5',
        'har1_8_6',
        'har1_8_7',
        'har1_8_8',
        'har1_8_9',
        'har1_8_op',
    ]

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if not player.participant.HAR1_EXP_GOGO:
            return False
        else:
            return player.participant.HAR1_8


class Har1_4(Page):
    form_model = 'player'
    form_fields = [
        'har1_9',
    ]

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if not player.participant.HAR1_EXP_GOGO:
            return False
        else:
            return True


class Har1_5(Page):
    form_model = 'player'
    form_fields = [
        'har1_10_1',
        'har1_10_2',
        'har1_10_3',
        'har1_10_4',
        'har1_10_5',
        'har1_10_op',
    ]

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if not player.participant.HAR1_EXP_GOGO:
            return False
        return player.har1_9 == 1


class Har1_6(Page):
    form_model = 'player'
    form_fields = [
        'har1_11_1',
        'har1_11_2',
        'har1_11_3',
        'har1_11_4',
        'har1_11_5',
        'har1_11_6',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if not player.participant.HAR1_EXP_GOGO:
            return False
        else:
            return True


class Har1_6_2(Page):
    form_model = 'player'
    form_fields = [
        'har1_11_7',
        'har1_11_8',
        'har1_11_9',
        'har1_11_10',
        'har1_11_11',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if not player.participant.HAR1_EXP_GOGO:
            return False
        else:
            return True


class Har1_7(Page):
    form_model = 'player'
    form_fields = [
        'har1_12_1',
        'har1_12_2',
        'har1_12_3',
        'har1_12_4',
        'har1_12_5',

        'har1_13_1st',
        'har1_13_2nd',
        'har1_13_1st_op',
        'har1_13_2nd_op',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if not player.participant.HAR1_EXP_GOGO:
            return False
        else:
            return True


class Har1s(Page):
    form_model = 'player'
    form_fields = [
        'har1_seen_critical',
        'har1s_3',
    ]

    @staticmethod
    def vars_for_template(player):
        return {
            'CASE': player.participant.HAR1_CASE,
            'EXPERIENCED_INDICES': player.participant.HAR1_EXPERIENCED_INDICES,
            'EXPERIENCED_LIST': player.participant.HAR1_EXPERIENCED_LIST,
            'SEEN_INDICES': player.participant.HAR1_SEEN_INDICES,
            'SEEN_LIST': player.participant.HAR1_SEEN_LIST,
        }

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if player.participant.HAR1_EXP_GOGO:
            return False
        else:
            return True


class Har1s_2(Page):
    form_model = 'player'
    form_fields = [
        'har1s_4'
    ]

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if player.participant.HAR1_EXP_GOGO:
            return False
        if player.har1s_3 == 4:
            return False
        else:
            return True


class Har1s_3(Page):
    form_model = 'player'
    form_fields = [
        'har1s_5',
        'har1s_6_1',
        'har1s_6_2',
        'har1s_7_1',
        'har1s_7_2',
        'har1s_7_3',
        'har1s_7_4',
        'har1s_7_5',
        'har1s_7_6',
        'har1s_7_7',
        'har1s_7_op',
    ]

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if player.participant.HAR1_EXP_GOGO:
            return False
        else:
            return True


class Har1s_4(Page):
    form_model = 'player'
    form_fields = [
        'har1s_8_1st',
        'har1s_8_2nd',
        'har1s_8_3rd',
    ]

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if player.participant.HAR1_EXP_GOGO:
            return False
        if player.har1s_7_1 or \
                not (player.har1s_7_3 or player.har1s_7_4 or player.har1s_7_5 or player.har1s_7_6 or player.har1s_7_7):
            return True
        else:
            return False


class Har1s_5(Page):
    form_model = 'player'
    form_fields = [
        'har1s_9',
    ]

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if player.participant.HAR1_EXP_GOGO:
            return False
        else:
            return True


class Har1s_6(Page):
    form_model = 'player'
    form_fields = [
        'har1s_10_1',
        'har1s_10_2',
        'har1s_10_3',
        'har1s_10_4',
        'har1s_10_5',
        'har1s_10_op',
    ]

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if player.participant.HAR1_EXP_GOGO:
            return False
        if player.har1s_9 == 1:
            return True
        else:
            return False


class Har1s_7(Page):
    form_model = 'player'
    form_fields = [
        'har1s_11_1',
        'har1s_11_2',
        'har1s_11_3',
        'har1s_11_4',
        'har1s_11_5',
        'har1s_12_1st',
        'har1s_12_2nd',
        'har1s_12_1st_op',
        'har1s_12_2nd_op',
    ]

    def is_displayed(player):
        if player.participant.HAR1_CASE == "PASS":
            return False
        if player.participant.HAR1_EXP_GOGO:
            return False
        else:
            return True


page_sequence = [
    Experience,
    Experience2,
    Experience3,
    Experience4,
    Experience5,
    Har1,
    Har1_1,
    Har1_1_plus,
    Har1_2,
    Har1_3,
    Har1_4,
    Har1_5,
    Har1_6,
    Har1_6_2,
    Har1_7,
    Har1s,
    Har1s_2,
    Har1s_3,
    Har1s_4,
    Har1s_5,
    Har1s_6,
    Har1s_7,
]
