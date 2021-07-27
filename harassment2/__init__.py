from otree.api import *
from . import har2_questions
from GlobalConstants import GlobalConstants

doc = """
성적 괴롭힘 설문 ( part 2 )
@date 2021.7.13
@author 서울대 사회학과 추지현 교수팀
@developer namun@snu.ac.kr 
"""


class Constants(BaseConstants):
    name_in_url = 'harassment2'
    players_per_group = None
    num_rounds = 1

    HAR2_QUESTIONS = har2_questions.HAR2_QUESTIONS


##### massive filed generators ######

def make_field_har2_experienced(index):
    return models.BooleanField(
        label=Constants.HAR2_QUESTIONS[index-1],
        widget=widgets.CheckboxInput,
        blank=True,
    )


def make_field_har2_seen(index):
    return models.BooleanField(
        label=Constants.HAR2_QUESTIONS[index-1],
        widget=widgets.CheckboxInput,
        blank=True,
    )


def make_field_har2_8(order):
    return models.IntegerField(
        label="귀하가 피해 이후 개인적으로 감내하거나 적극적인 조치를 취하지 않은 이유는 무엇입니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "① 문제를 제기할만큼 심각한 것은 아거나 일상에서 흔한 일이라서"],
            [2, "② 나만 이상한 사람, 분란을 일으킨 사람으로 여겨질 것 같아서"],
            [3, "③ 업무능력 부족, 실수 등 나에게 책임이 있다고 생각해서"],
            [4, "④ 직장 내에서 피해 사실이 공개될까봐"],
            [5, "⑤ 알려도 공정하게 사건이 처리되지 않거나 상황이 개선되지 않을 것 같아서"],
            [6, "⑥ 조치를 취할 수 있는 방법을 모르거나 담당 기구를 몰라서"],
            [7, "⑦ 직장 내 괴롭힘에 대해 상담하기 어려운 분위기 때문에"],
            [8, "⑧ 직무 배치, 평가, 승진, 해고, 근로계약연장, 정규직 전환 등 인사상 불이익이 우려돼서"],
            [9, "⑨ 기타(직접입력)"],
        ]
    )


def make_field_har2_14(order):
    return models.IntegerField(
        label="귀하가 경험한 위 피해가 발생하게 된 가장 주된 원인은 무엇이라 생각합니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "① 직장의 경영정책(인력감축, 고객서비스정책 등)"],
            [2, "② 실적과 성과를 강조하는 직장 분위기 "],
            [3, "③ 성차별적 조직 문화"],
            [4, "④ 상명하복의 조직 문화"],
            [5, "⑤ 열악한 근무 여건과 과도한 업무로 인한 스트레스"],
            [6, "⑥ 고용 불안정"],
            [7, "⑦ 가해자 개인의 인성 문제"],
            [8, "⑧ 내 잘못"],
            [9, "⑨ 기타"],
        ]
    )


def make_field_har2s_8(order):
    return models.IntegerField(
        label="위 상황을 목격한 후 피해자를 돕거나 직장에 적극적인 조치를 취하지 않은 이유는 무엇입니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "① 문제를 제기할만큼 심각한 것은 아니거나 일상에서 흔한 일이라 생각해서 "],
            [2, "② 피해자와 함께 이상한 사람, 분란을 일으킨 사람으로 여겨질 것 같아서"],
            [3, "③ 업무능력 부족, 실수 등 피해자에게도 책임이 있다고 생각해서"],
            [4, "④ 피해자가 원하지 않을 것 같아서"],
            [5, "⑤ 알려도 공정하게 사건이 처리되지 않거나 상황이 개선되지 않을 것 같아서"],
            [6, "⑥ 딱히 도와줄 방법을 모르거나 담당 기구를 몰라서"],
            [7, "⑦ 직장내 괴롭힘에 대하여 문제제기를 하기 어려운 분위기 때문에"],
            [8, "⑧ 나까지 직무 배치, 평가, 승진, 해고, 근로계약연장, 정규직 전환 등 인사상 불이익을 받을까봐"],
            [9, "⑨ 남의 일에 관여할 이유가 없어서"],
        ]
    )


def make_field_har2s_12(order):
    return models.IntegerField(
        label="귀하가 목격한 상황이 발생하게 된 가장 주된 원인은 무엇이라 생각합니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "① 직장의 경영정책(인력감축, 고객서비스정책 등)"],
            [2, "② 실적과 성과를 강조하는 직장 분위기"],
            [3, "③ 성차별적 조직 문화"],
            [4, "④ 상명하복의 조직 문화"],
            [5, "⑤ 열악한 근무 여건과 과도한 업무로 인한 스트레스"],
            [6, "⑥ 고용 불안정"],
            [7, "⑦ 가해자 개인의 인성 문제"],
            [8, "⑧ 피해자 잘못"],
            [9, "⑨ 기타"],
        ]
    )


#####################################


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


############################################# PLAYERS ######################################################

class Player(BasePlayer):
    har2_experienced_1 = make_field_har2_experienced(1)
    har2_experienced_2 = make_field_har2_experienced(2)
    har2_experienced_3 = make_field_har2_experienced(3)
    har2_experienced_4 = make_field_har2_experienced(4)
    har2_experienced_5 = make_field_har2_experienced(5)
    har2_experienced_6 = make_field_har2_experienced(6)
    har2_experienced_7 = make_field_har2_experienced(7)
    har2_experienced_8 = make_field_har2_experienced(8)
    har2_experienced_9 = make_field_har2_experienced(9)
    har2_experienced_10 = make_field_har2_experienced(10)
    har2_experienced_11 = make_field_har2_experienced(11)
    har2_experienced_12 = make_field_har2_experienced(12)
    har2_experienced_13 = make_field_har2_experienced(13)
    har2_experienced_14 = make_field_har2_experienced(14)
    har2_experienced_15 = make_field_har2_experienced(15)
    har2_experienced_16 = make_field_har2_experienced(16)
    har2_experienced_17 = make_field_har2_experienced(17)
    har2_experienced_18 = make_field_har2_experienced(18)

    har2_seen_1 = make_field_har2_seen(1)
    har2_seen_2 = make_field_har2_seen(2)
    har2_seen_3 = make_field_har2_seen(3)
    har2_seen_4 = make_field_har2_seen(4)
    har2_seen_5 = make_field_har2_seen(5)
    har2_seen_6 = make_field_har2_seen(6)
    har2_seen_7 = make_field_har2_seen(7)
    har2_seen_8 = make_field_har2_seen(8)
    har2_seen_9 = make_field_har2_seen(9)
    har2_seen_10 = make_field_har2_seen(10)
    har2_seen_11 = make_field_har2_seen(11)
    har2_seen_12 = make_field_har2_seen(12)
    har2_seen_13 = make_field_har2_seen(13)
    har2_seen_14 = make_field_har2_seen(14)
    har2_seen_15 = make_field_har2_seen(15)
    har2_seen_16 = make_field_har2_seen(16)
    har2_seen_17 = make_field_har2_seen(17)
    har2_seen_18 = make_field_har2_seen(18)

    #Har2

    har2_experienced_critical = models.IntegerField(
        min=1,
        max=len(Constants.HAR2_QUESTIONS),
        widget=widgets.RadioSelect,
    )

    har2_experienced_critical = models.IntegerField(
        min=1,
        max=len(Constants.HAR2_QUESTIONS),
        widget=widgets.RadioSelect,
    )

    har2_3 = models.IntegerField(
        label="응답하신 행위의 가해자는 귀하와 어떤 관계였습니까? 가해자가 여럿인 경우 주된 가해자를 기준으로 응답해주십시오.",
        widget=widgets.RadioSelect,
        choices=[
            [1, "상사"],
            [2, "동료"],
            [3, "부하"],
            [4, "누군지 모름"],
        ]
    )

    #Har2_1

    har2_4 = models.IntegerField(
        label="그 가해자의 성별은 무엇입니까? 여럿인 경우 주된 가해자를 기준으로 응답해주십시오.",
        widget=widgets.RadioSelect,
        choices=GlobalConstants.GENDER_CHOICES,
    )

    #Har2_1_plus

    har2_6_1 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="오프라인에서",
        blank=True,
    )

    har2_6_2 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="온라인을 통해(사내 전산망, SNS, 문자, 전화 등)",
        blank=True,
    )

    har2_7_1 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="① 아무에게도 이야기하지 않았다",
        blank=True,
    )

    har2_7_2 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="② 주변 동료에게 알렸다",
        blank=True,
    )

    har2_7_3 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="③ 잠시 휴직을 하거나 휴가를 가졌다",
        blank=True,
    )

    har2_7_4 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="④ 스스로 부서나 근무지를 이동했다",
        blank=True,
    )

    har2_7_5 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑤ 상사나 부서장 등에게 상담했다.",
        blank=True,
    )

    har2_7_6 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑥ 노동조합에 알리고 상담했다.",
        blank=True,
    )

    har2_7_7 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑦ 직장 내 고충처리절차를 이용했다",
        blank=True,
    )

    har2_7_8 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑧ 가해자에게 직접 문제를 제기하였다",
        blank=True,
    )

    har2_7_9 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑨ 직장 외부의 민간단체(고용평등상담실, 갑질119 등)나 공공기관(고용노동부, 국가인권위원회 등)등에 상담 혹은 신고를 했다.",
        blank=True,
    )

    har2_7_10 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="⑩ 소송 등 법적인 구제절차를 취했다",
        blank=True,
    )

    har2_7_op = models.LongStringField(
        label="⑪ 기타(직접입력)",
        blank=True,
    )

    # Har2_2

    har2_8_1st = make_field_har2_8(1)
    har2_8_1st_op = models.LongStringField(
        blank=True,
        label="",
    )

    har2_8_2nd = make_field_har2_8(2)
    har2_8_2nd_op = models.LongStringField(
        blank=True,
        label="",
    )

    har2_8_3rd = make_field_har2_8(3)
    har2_8_3rd_op = models.LongStringField(
        blank=True,
        label="",
    )


    #Har2_3

    har2_9_1 = models.BooleanField(
        label="① 아무런 조치가 없었다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_9_2 = models.BooleanField(
        label="② 행위자가 사과하도록 했다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_9_3 = models.BooleanField(
        label="③행위자에게 인사조치가 있었다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_9_4 = models.BooleanField(
        label="④ 피해자인 나와 행위자를 분리했다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_9_5 = models.BooleanField(
        label="⑤ 예방 교육이나 지침 안내 등 해당사안과 관련해 직장 교육을 했다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_9_6 = models.BooleanField(
        label="⑥ 피해에 대한 금전적 보상이 이루어지도록 했다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_9_7 = models.BooleanField(
        label="⑦ 상담이나 치료, 유급 휴직 등 지원을 해주었다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_9_8 = models.BooleanField(
        label="⑧ 조사 결과를 내게 알려주었다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_9_9 = models.BooleanField(
        label="⑨ 사건 종결과 처리를 미루었다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_9_op = models.LongStringField(
        label="⑩ 기타(직접입력)",
        blank=True,
    )


    #Har2_4

    har2_10 = models.IntegerField(
        label="피해 상황은 이후 귀하가 원치 않았던 직장 구성원들에게까지 알려지게 되었습니까?",
        widget=widgets.RadioSelect,
        choices=GlobalConstants.YNU_CHOICES,
    )

    #Har2_5

    har2_11_1 = models.BooleanField(
        label="① 피해가 남들이 보는 앞에서 혹은 행정절차(성과평가, 승진, 휴가 등)를 통해 공공연히 이뤄져서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_11_2 = models.BooleanField(
        label="② 피해 이후 직장동료, 노조, 상담기구 등을 통한 상담이나 하소연하는 과정에서 소문이 나서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_11_3 = models.BooleanField(
        label="③ 고충처리나 직장으로부터의 지원 등 문제제기 절차를 진행하는 과정(조사, 피해자의 휴가 사용 등을 통해서)에서 비밀보호가 제대로 되지 않아서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_11_4 = models.BooleanField(
        label="④ 가해자가 먼저 제멋대로 소문을 내고 다녀서 ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_11_5 = models.BooleanField(
        label="⑤ 가해자에 대한 징계나 조치(피해자와의 공간분리, 배치이동 등) 과정에서 소문이 나서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_11_op = models.LongStringField(
        label="⑥ 기타(직접입력)",
        blank=True,
    )

    # 피해 이후 귀하에게 다음과 같은 상황이 발생한 적 있습니까? 다음 중 해당하는 것을 모두 골라주십시오.

    har2_12_1 = models.BooleanField(
        label="① 직장에 문제제기하거나 분란을 만들었다는 이유로 비난을 받음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_12_2 = models.BooleanField(
        label="② 악의적으로 가해자를 신고했다거나 나에게 잘못이 있는 것처럼 오해받거나 소문에 시달림",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_12_3 = models.BooleanField(
        label="③ 사람들이 나를 피하거나 따돌림",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_12_4 = models.BooleanField(
        label="④ 다른 유사사건이 생기거나 논의될 때마다 나의 피해 사례를 굳이 반복해 거론함",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_12_5 = models.BooleanField(
        label="⑤ 분란을 만들지 말고 조용히 넘어가기를 강요받거나 참으라는 얘기를 들음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_12_6 = models.BooleanField(
        label="⑥ 회사가 인사상 불이익 처우를 암시하며 사건을 축소 또는 은폐하려 함",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_12_7 = models.BooleanField(
        label="⑦ 회사가 가해자와의 합의를 종용함",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_12_8 = models.BooleanField(
        label="⑧ 과도한 업무 혹은 다른 업무를 부여받거나 업무를 부여받지 못함",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_12_9 = models.BooleanField(
        label="⑨ 회사가 가해자가 아닌 나만 부서이동을 시킴",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_12_10 = models.BooleanField(
        label="⑩ 근무평가, 승진, 근로계약 갱신 거절 등 인사상 부당한 대우나 불이익을 받음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_12_11 = models.BooleanField(
        label="⑪ 내 조력자에게 해고, 징계, 고용, 업무상 불이익 등을 주거나 끼어들지 말라고 회유, 강요하는 등 괴롭힘이 가해짐",
        widget=widgets.CheckboxInput,
        blank=True,
    )


    # 위 피해를 경험한 후 귀하에게는 다음과 같은 변화가 있었습니까? 다음 중 해당하는 것을 모두 골라주십시오.

    har2_13_1 = models.BooleanField(
        label="① 근무 의욕, 업무 능력, 집중도가 떨어졌다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_13_2 = models.BooleanField(
        label="② 상급자나 직장에 대한 신뢰가 떨어졌다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_13_3 = models.BooleanField(
        label="③ 또 피해를 당할까봐 직장 동료들과 관계 맺는 것이 이전보다 조심스러워졌다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_13_4 = models.BooleanField(
        label="④ 이직을 고민했다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_13_5 = models.BooleanField(
        label="⑤ 분노나 불안감, 우울, 무력감, 감정조절 및 수면에 어려움을 느꼈다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_13_6 = models.BooleanField(
        label="⑥ 이직을 고민하였다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2_13_7 = models.BooleanField(
        label="⑦ 특별한 영향은 없었다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

# 귀하가 경험한 위 피해가 발생하게 된 가장 주된 원인은 무엇이라 생각합니까?

    har2_14_1st = make_field_har2_14(1)
    har2_14_2nd = make_field_har2_14(2)



    #Har2s

    har2_seen_critical = models.IntegerField(
        min=1,
        max=len(Constants.HAR2_QUESTIONS),
        widget=widgets.RadioSelect,
    )

    har2s_3 = models.IntegerField(
        label="응답하신 행위는 누가(가해자)가 누구에게(피해자) 한 것이었습니까? 여럿인 경우 주된 가해자와 피해자의 관계를 기준으로 응답해주십시오.",
        widget=widgets.RadioSelect,
        choices=[
            [1, "① 상사가 부하직원에게"],
            [2, "② 동료끼리"],
            [3, "③ 부하직원이 상사에게"],
            [4, "④ 가해자가 누구인지 모름"],
        ]
    )

    #Har2s_2

    har2s_4 = models.IntegerField(
        label="그 가해자의 성별은 무엇입니까? 여럿인 경우 주된 가해자를 기준으로 응답해주십시오.",
        widget=widgets.RadioSelect,
        choices=GlobalConstants.GENDER_CHOICES,
    )


    #Har2s_3

    har2s_5 = models.IntegerField(
        label="피해자의 성별은 무엇입니까? 여럿인 경우 주된 피해자를 기준으로 응답해주십시오.",
        widget=widgets.RadioSelect,
        choices=GlobalConstants.GENDER_CHOICES,
    )

    har2s_6_1 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="오프라인에서",
        blank=True,
    )

    har2s_6_2 = models.BooleanField(
        widget=widgets.CheckboxInput,
        label="온라인을 통해(사내 전산망, SNS, 문자, 전화 등)",
        blank=True,
    )

    har2s_7_1 = models.BooleanField(
        label="① 아무에게도 이야기하지 않았다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_7_2 = models.BooleanField(
        label="② 주변 동료에게 알렸다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_7_3 = models.BooleanField(
        label="③ 피해자를 위로하거나 조언했다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_7_4 = models.BooleanField(
        label="④ 가해자에게 직접 문제를 제기하거나 말렸다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_7_5 = models.BooleanField(
        label="⑤ 상사나 부서장 등에게 상담했다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_7_6 = models.BooleanField(
        label="⑥ 노동조합에 알리고 상담했다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_7_7 = models.BooleanField(
        label="⑦ 직장 내 상담창구나 고충처리절차를 이용했다",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_7_op = models.LongStringField(
        label="⑧ 기타(직접입력)",
        blank=True,
    )

    #Har2s_4

    har2s_8_1st = make_field_har2s_8(1)
    har2s_8_2nd = make_field_har2s_8(2)
    har2s_8_3rd = make_field_har2s_8(3)


    #Har2s_5

    har2s_9 = models.IntegerField(
        label="피해 상황은 이후 귀하가 원치 않았던 직장 구성원들에게까지 알려지게 되었습니까?",
        widget=widgets.RadioSelect,
        choices=GlobalConstants.YNU_CHOICES,
    )

    #Har1s_6

    har2s_10_1 = models.BooleanField(
        label="① 피해가 남들이 보는 앞에서 혹은 행정절차(성과평가, 승진, 휴가 등)를 통해 공공연히 이뤄져서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_10_2 = models.BooleanField(
        label="② 피해자가 직장동료, 노조, 상담기구 등을 통한 상담이나 하소연하는 과정에서 소문이 나서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_10_3 = models.BooleanField(
        label="③ 고충처리나 직장으로부터의 지원 등 문제제기 절차를 진행하는 과정(조사,  피해자의 휴가 사용 등을 통해서)에서 비밀보호가 제대로 되지 않아서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_10_4 = models.BooleanField(
        label="④ 가해자가 먼저 제멋대로 소문을 내고 다녀서 ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_10_5 = models.BooleanField(
        label="⑤ 가해자에 대한 징계나 조치(피해자와의 공간분리, 배치이동 등) 과정에서 소문이 나서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_10_op = models.LongStringField(
        label="⑥ 기타(직접입력)",
        blank=True,
    )


    #Har2s_7

    har2s_11_1 = models.BooleanField(
        label="① 근무 의욕, 업무 능력, 집중도가 떨어졌다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_11_2 = models.BooleanField(
        label="② 상급자나 직장에 대한 신뢰가 떨어졌다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_11_3 = models.BooleanField(
        label="③ 나도 피해를 경험하게 될까봐 직장 동료들과 관계 맺는 것이 이전보다 조심스러워졌다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_11_4 = models.BooleanField(
        label="④ 내가 가해자로 지목될 수도 있을까봐 직장 동료들과 선별적으로 관계를 맺게 되었다. ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_11_5 = models.BooleanField(
        label="⑤ 특별한 영향은 없었다.",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    har2s_12_1st = make_field_har2s_12(1)
    har2s_12_2nd = make_field_har2s_12(2)



############################################# PAGES ######################################################

class Experience(Page):
    form_model = 'player'
    form_fields = [
        'har2_experienced_1',
        'har2_seen_1',
        'har2_experienced_2',
        'har2_seen_2',
        'har2_experienced_3',
        'har2_seen_3',
        'har2_experienced_4',
        'har2_seen_4',
        'har2_experienced_5',
        'har2_seen_5',
        'har2_experienced_6',
        'har2_seen_6',
        'har2_experienced_7',
        'har2_seen_7',
        'har2_experienced_8',
        'har2_seen_8',
    ]

    @staticmethod
    def vars_for_template(player):
        return{
            'INIT': 1,
            'END': len(Experience.form_fields)/2,
        }


class Experience2(Page):
    form_model = 'player'
    form_fields = [
        'har2_experienced_9',
        'har2_seen_9',
        'har2_experienced_10',
        'har2_seen_10',
        'har2_experienced_11',
        'har2_seen_11',
        'har2_experienced_12',
        'har2_seen_12',
        'har2_experienced_13',
        'har2_seen_13',
        'har2_experienced_14',
        'har2_seen_14',
        'har2_experienced_15',
        'har2_seen_15',
        'har2_experienced_16',
        'har2_seen_16',
        'har2_experienced_17',
        'har2_seen_17',
        'har2_experienced_18',
        'har2_seen_18',
    ]

    @staticmethod
    def vars_for_template(player):
        return{
            'INIT': 1,
            'END': len(Experience2.form_fields)/2,
        }


class Har2(Page):
    form_model = 'player'
    form_fields = [
        'har2_experienced_critical',
        'har2_3',
    ]

    @staticmethod
    def vars_for_template(player):
        return{
            'CASE': player.participant.HAR2_CASE,
            'EXPERIENCED_INDICES': player.participant.HAR2_EXPERIENCED_INDICES,
            'EXPERIENCED_LIST': player.participant.HAR2_EXPERIENCED_LIST,
            'SEEN_INDICES': player.participant.HAR2_SEEN_INDICES,
            'SEEN_LIST': player.participant.HAR2_SEEN_LIST,
        }

    # @staticmethod
    def is_displayed(player):
        player.participant.HAR2_EXPERIENCED_INDICES = [
            player.har2_experienced_1,
            player.har2_experienced_2,
            player.har2_experienced_3,
            player.har2_experienced_4,
            player.har2_experienced_5,
            player.har2_experienced_6,
            player.har2_experienced_7,
            player.har2_experienced_8,
            player.har2_experienced_9,
            player.har2_experienced_10,
            player.har2_experienced_11,
            player.har2_experienced_12,
            player.har2_experienced_13,
            player.har2_experienced_14,
            player.har2_experienced_15,
            player.har2_experienced_16,
            player.har2_experienced_17,
            player.har2_experienced_18,
        ]

        player.participant.HAR2_SEEN_INDICES = [
            player.har2_seen_1,
            player.har2_seen_2,
            player.har2_seen_3,
            player.har2_seen_4,
            player.har2_seen_5,
            player.har2_seen_6,
            player.har2_seen_7,
            player.har2_seen_8,
            player.har2_seen_9,
            player.har2_seen_10,
            player.har2_seen_11,
            player.har2_seen_12,
            player.har2_seen_13,
            player.har2_seen_14,
            player.har2_seen_15,
            player.har2_seen_16,
            player.har2_seen_17,
            player.har2_seen_18,
        ]

        player.participant.HAR2_EXPERIENCED_LIST = [[i+1, Constants.HAR2_QUESTIONS[i]] for i, value in enumerate(player.participant.HAR2_EXPERIENCED_INDICES) if value]
        player.participant.HAR2_SEEN_LIST = [[i+1, Constants.HAR2_QUESTIONS[i]] for i, value in enumerate(player.participant.HAR2_SEEN_INDICES) if value]

        total_number_of_experienced = sum(player.participant.HAR2_EXPERIENCED_INDICES)
        total_number_of_seen = sum(player.participant.HAR2_SEEN_INDICES)

        return_value = False
        case = "CASE_WAS_NOT_ASSIGNED_THIS_MEANS_ERROR"

        if total_number_of_experienced >= 2:
            case = "E2"
            return_value = True
            player.participant.HAR2_EXP_GOGO = True
        elif total_number_of_experienced == 1:
            case = "E3"
            return_value = True
            player.participant.HAR2_EXP_GOGO = True
        elif total_number_of_seen >= 2:
            case = "S2"
            player.participant.HAR2_EXP_GOGO = False
        elif total_number_of_seen == 1:
            case = "S3"
            player.participant.HAR2_EXP_GOGO = False
        else:
            case = "PASS"
            player.participant.HAR2_EXP_GOGO = False

        player.participant.HAR2_CASE = case

        return return_value


def har2_experienced_critical_choices(player):
    print(player.participant.HAR2_EXPERIENCED_LIST)
    choices = [
        v for i, v in enumerate(player.participant.HAR2_EXPERIENCED_LIST)
    ]
    return choices


def har2_seen_critical_choices(player):
    choices =  [
        v for i, v in enumerate(player.participant.HAR2_SEEN_LIST)
    ]
    return choices


class Har2_1(Page):
    form_model = 'player'
    form_fields = [
        'har2_4',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        elif not player.participant.HAR2_EXP_GOGO:
            return False
        elif player.har2_3 == 4:
            return False
        else:
            return True


class Har2_1_plus(Page):
    form_model = 'player'
    form_fields = [
        'har2_6_1',
        'har2_6_2',
        'har2_7_1',
        'har2_7_2',
        'har2_7_3',
        'har2_7_4',
        'har2_7_5',
        'har2_7_6',
        'har2_7_7',
        'har2_7_8',
        'har2_7_9',
        'har2_7_10',
        'har2_7_op',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        elif not player.participant.HAR2_EXP_GOGO:
            return False
        else:
            return True


class Har2_2(Page):
    form_model = 'player'
    form_fields = [
        'har2_8_1st',
        'har2_8_1st_op',
        'har2_8_2nd',
        'har2_8_2nd_op',
        'har2_8_3rd',
        'har2_8_3rd_op',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        if not player.participant.HAR2_EXP_GOGO:
            return False
        if player.har2_7_1 == True or (
            player.har2_7_2 == False and
            player.har2_7_5 == False and
            player.har2_7_6 == False and
            player.har2_7_7 == False and
            player.har2_7_8 == False and
            player.har2_7_9 == False and
            player.har2_7_10 == False
        ):
            player.participant.HAR2_9 = False
            return True
        elif (
                player.har2_7_5 == True or
                player.har2_7_6 == True or
                player.har2_7_7 == True or
                player.har2_7_8 == True or
                player.har2_7_9 == True or
                player.har2_7_10 == True
        ):
            player.participant.HAR2_9 = True
            return False
        else:
            player.participant.HAR2_9 = False
            return False


class Har2_3(Page):
    form_model = 'player'
    form_fields = [
        'har2_9_1',
        'har2_9_2',
        'har2_9_3',
        'har2_9_4',
        'har2_9_5',
        'har2_9_6',
        'har2_9_7',
        'har2_9_8',
        'har2_9_9',
        'har2_9_op',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        if not player.participant.HAR2_EXP_GOGO:
            return False
        else:
            return player.participant.HAR2_9


class Har2_4(Page):
    form_model = 'player'
    form_fields = [
        'har2_10',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        elif not player.participant.HAR2_EXP_GOGO:
            return False
        else:
            return True


class Har2_5(Page):
    form_model = 'player'
    form_fields = [
        'har2_11_1',
        'har2_11_2',
        'har2_11_3',
        'har2_11_4',
        'har2_11_5',
        'har2_11_op',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        elif not player.participant.HAR2_EXP_GOGO:
            return False
        else:
            return player.har2_10 == 1


class Har2_6(Page):
    form_model = 'player'
    form_fields = [
        'har2_12_1',
        'har2_12_2',
        'har2_12_3',
        'har2_12_4',
        'har2_12_5',
        'har2_12_6',
        'har2_12_7',
        'har2_12_8',
        'har2_12_9',
        'har2_12_10',
        'har2_12_11',

        'har2_13_1',
        'har2_13_2',
        'har2_13_3',
        'har2_13_4',
        'har2_13_5',
        'har2_13_6',
        'har2_13_7',

        'har2_14_1st',
        'har2_14_2nd',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        elif not player.participant.HAR2_EXP_GOGO:
            return False
        else:
            return True


class Har2s(Page):
    form_model = 'player'
    form_fields = [
        'har2_seen_critical',
        'har2s_3',
    ]

    @staticmethod
    def vars_for_template(player):
        return {
            'CASE': player.participant.HAR2_CASE,
        }

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        elif player.participant.HAR2_EXP_GOGO:
            return False
        else:
            return True


class Har2s_2(Page):
    form_model = 'player'
    form_fields = [
        'har2s_4',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        elif player.participant.HAR2_EXP_GOGO:
            return False
        elif player.har2s_3 == 4:
            return False
        else:
            return True


class Har2s_3(Page):
    form_model = 'player'
    form_fields = [
        'har2s_5',
        'har2s_6_1',
        'har2s_6_2',
        'har2s_7_1',
        'har2s_7_2',
        'har2s_7_3',
        'har2s_7_4',
        'har2s_7_5',
        'har2s_7_6',
        'har2s_7_7',
        'har2s_7_op',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        elif player.participant.HAR2_EXP_GOGO:
            return False
        else:
            return True


class Har2s_4(Page):
    form_model = 'player'
    form_fields = [
        'har2s_8_1st',
        'har2s_8_2nd',
        'har2s_8_3rd',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        elif player.participant.HAR2_EXP_GOGO:
            return False
        elif player.har2s_7_1 or \
                not (player.har2s_7_3 or player.har2s_7_4 or player.har2s_7_5 or player.har2s_7_6 or player.har2s_7_7):
            return True
        else:
            return False


class Har2s_5(Page):
    form_model = 'player'
    form_fields = [
        'har2s_9',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        if player.participant.HAR2_EXP_GOGO:
            return False
        else:
            return True


class Har2s_6(Page):
    form_model='player'
    form_fields = [
        'har2s_10_1',
        'har2s_10_2',
        'har2s_10_3',
        'har2s_10_4',
        'har2s_10_5',
        'har2s_10_op',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        if player.participant.HAR2_EXP_GOGO:
            return False
        if player.har2s_9 == 1:
            return True
        else:
            return False


class Har2s_7(Page):
    form_model = 'player'
    form_fields = [
        'har2s_11_1',
        'har2s_11_2',
        'har2s_11_3',
        'har2s_11_4',
        'har2s_11_5',
        'har2s_12_1st',
        'har2s_12_2nd',
    ]

    @staticmethod
    def is_displayed(player):
        if player.participant.HAR2_CASE == "PASS":
            return False
        if player.participant.HAR2_EXP_GOGO:
            return False
        else:
            return True


page_sequence = [
    Experience,
    Experience2,
    Har2,
    Har2_1,
    Har2_1_plus,
    Har2_2,
    Har2_3,
    Har2_4,
    Har2_5,
    Har2_6,
    Har2s,
    Har2s_2,
    Har2s_3,
    Har2s_4,
    Har2s_5,
    Har2s_6,
    Har2s_7,
]
