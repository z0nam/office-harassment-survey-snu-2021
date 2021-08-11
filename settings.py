from os import environ

SESSION_CONFIGS = [
    dict(
        name='survey_master',
        display_name='사무금융노동자 직장 내 괴롭힘 설문조사(연맹)',
        app_sequence=[
            'introduction',
            'culture',
            'harassment1',
            'harassment2',
            'policy',
            'basic',
            'ending',
        ],
        num_demo_participants=1,
    ),
    dict(
        name='survey_master_union',
        display_name='사무금융노동자 직장 내 괴롭힘 설문조사(노조)',
        app_sequence=[
            'introduction_union',
            'culture',
            'harassment1',
            'harassment2',
            'policy',
            'basic',
            'ending',
        ],
        num_demo_participants=1,
    ),
    dict(
        name='culture',
        display_name='1. [전체] 직장문화에 대한 평가',
        app_sequence=[
            'culture',
        ],
        num_demo_participants=1,
    ),
    dict(
        name='harassment1',
        display_name='2. 피해 및 목격 경험 Ⅰ',
        app_sequence=[
            'harassment1',
        ],
        num_demo_participants=1,
    ),
    dict(
        name='harassment2',
        display_name='3. 피해 및 목격 경험 Ⅱ',
        app_sequence=[
            'harassment2',
        ],
        num_demo_participants=1,
    ),
    dict(
        name='policy',
        display_name='4. 관련 제도 운용 실태와 정책 수요',
        app_sequence=[
            'policy',
        ],
        num_demo_participants=1,
    ),
    dict(
        name='basic',
        display_name='5. [전체]응답자 배경 정보',
        app_sequence=[
            'basic',
        ],
        num_demo_participants=1,
    ),
    dict(
        name='interview_request',
        display_name='인터뷰 요청 (조건부 - 미사용)',
        app_sequence=[
            'interview_request',
        ],
        num_demo_participants=1,
    ),
    dict(
        name='ending',
        display_name='감사합니다 표시화면',
        app_sequence=[
            'ending',
        ],
        num_demo_participants=1,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    'HAR1_EXPERIENCED_INDICES', # 경험 리스트 (불리언 리스트)
    'HAR1_EXPERIENCED_LIST', # 경험 질문/인덱스숫자 리스트
    'HAR1_SEEN_INDICES', # 목격 리스트
    'HAR1_SEEN_LIST',
    'HAR1_CASE', # 분기를 위한 플래그
    'HAR1_EXP_GOGO', # 피해경험 설문할지 여부 (이것이  True 면 반드시 목격설문은 패스)
    'HAR1_8',

    'HAR2_CASE',
    'HAR2_EXPERIENCED_INDICES',
    'HAR2_EXPERIENCED_LIST',
    'HAR2_SEEN_INDICES',
    'HAR2_SEEN_LIST',
    'HAR2_EXP_GOGO',
    'HAR2_9',
]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ko'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4098553728246'


ROOMS = [
    dict(
        name="fed",
        display_name="연명용 설문지",
    ),
    dict(
        name="union",
        display_name="노조용 설문지",
    )
]