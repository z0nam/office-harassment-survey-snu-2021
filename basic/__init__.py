from otree.api import *


doc = """
5. 응답자 배경 정보
@date 2021.7.13
@author 서울대 사회학과 추지현 교수팀
@developer namun@snu.ac.kr 
"""


class Constants(BaseConstants):
    name_in_url = 'basic'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    #다음은 개인 인적사항에 대한 질문입니다.
    gender = models.IntegerField(
        label="성별",
        widget=widgets.RadioSelect,
        choices=[
            [1, "여성"],
            [2, "남성"],
        ]
    )

    born_year = models.IntegerField(
        label="출생연도",
        choices=range(2006, 1949, -1),
    )

    education = models.IntegerField(
        label="학력",
        widget=widgets.RadioSelect,
        choices=[
            [1, "고졸 이하"],
            [2, "전문대졸"],
            [3, "대졸"],
            [4, "대학원 재학 이상"],
        ]
    )

    work_area = models.IntegerField(
        label="근무지역",
        widget=widgets.RadioSelect,
        choices=[
            [1, "서울"],
            [2, "광역시"],
            [3, "기타 시"],
            [4, "도농복합"],
            [5, "군"],
        ]
    )

    work_status = models.IntegerField(
        label="직장 근무 상황",
        widget=widgets.RadioSelect,
        choices=[
            [1, "본사 근무"],
            [2, "지점 근무"],
            [3, "기타(직접입력)"],
        ]
    )

    work_status_op = models.StringField(
        label="",
        blank=True,
    )


    #다음은 현재 직장 근무 상황에 대한 질문입니다.

    work_category = models.IntegerField(
        label="업종",
        widget=widgets.RadioSelect,
        choices=[
            [1, "여수신"],
            [2, "생명보험 "],
            [3, "손해보험 "],
            [4, "직할/일반사무"],
            [5, "공공기관"],
            [6, "협동조합 "],
            [7, "기타(직접입력)"],
        ]
    )

    work_category_op = models.StringField(
        label="",
        blank=True,
    )

    work_type = models.IntegerField(
        label="업무(직무)",
        widget=widgets.RadioSelect,
        choices=[
            [1, "관리 : 자산운용, 심사/채권관리, 기획, 홍보, 인사, 상품 개발 등 "],
            [2, "사무/현장 지원 : 총무, 지점 대면 업무 등"],
            [3, "영업/보상 : 개인, 법인 영업, 보상 등 "],
            [4, "서비스 : 고객지원센터, 콜센터, 고객 방문 케어 서비스 등  "],
            [5, "IT/전산 : IT/전산 업무 등"],
            [6, "기타(직접입력)"],
        ]
    )

    work_type_op = models.StringField(
        label="",
        blank=True,
    )

    work_rank = models.IntegerField(
        label="직급(직위)",
        widget=widgets.RadioSelect,
        choices=[
            [1, "관리자"],
            [2, "비관리자(사원)"],
        ]
    )

    work_form = models.IntegerField(
        label="고용형태",
        widget=widgets.RadioSelect,
        choices=[
            [1, "정규직"],
            [2, "비정규직(무기계약직, 기간제계약직, 파견 등)"],
        ]
    )

    employment_period = models.IntegerField(
        label="현 직장 근무 기간",
        widget=widgets.RadioSelect,
        choices=[
            [1, "3년 미만"],
            [2, "3년 이상 10년 미만"],
            [3, "10년 이상 20년 미만"],
            [4, "20년 초과"],
        ]
    )

    union_enrollment = models.IntegerField(
        label="노동조합 가입여부",
        widget=widgets.RadioSelect,
        choices=[
            [1, "가입함"],
            [2, "가입대상이나 가입하지 않음"],
            [3, "가입대상이 아님"],
        ]
    )

    number_of_workers = models.IntegerField(
        label="직장(회사 전체)의 직원 규모. 귀하의 직장이 본사(본점), 공장, 지사, 영업소, 출장소, 분점 등으로 나눠져 있는 경우, 귀하가 출퇴근을 하고 있는 건물(혹은 일상적 업무 통제가 이뤄지는 곳)을 기준으로 ‘직장’을 떠올려 주십시오. 여러 부서가 한 건물안에 있는 경우, 건물 전체를 기준으로 답해주십시오",
        widget=widgets.RadioSelect,
        choices=[
            [1, "30명 미만  "],
            [2, "30명 이상 100명 미만 "],
            [3, "100명 이상 300명 미만 "],
            [4, "300명 이상 "],
        ]
    )

    work_hour_weekly = models.IntegerField(
        label="1주 평균 근무 시간 (시간외 근무, 퇴근 후 업무와 관련된 시간도 포함)",
        widget=widgets.RadioSelect,
        choices=[
            [1, "40시간 미만"],
            [2, "40시간 이상 - 52시간 이하"],
            [3, "52시간 초과"],
        ]
    )


# PAGES
class BasicInfo(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'born_year',
        'education',
        'work_area',
        'work_status',
        'work_status_op',
        'work_category',
        'work_category_op',
        'work_type',
        'work_type_op',
        'work_rank',
        'work_form',
        'employment_period',
        'union_enrollment',
        'number_of_workers',
        'work_hour_weekly',
    ]


page_sequence = [BasicInfo]
