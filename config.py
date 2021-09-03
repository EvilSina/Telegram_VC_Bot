HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["7936714"])
    API_HASH = environ["6896b470aec284d6e0288a3033775f9a"]
    SESSION_STRING = environ[
        "AQDGBABah00wT1enxnQHuFC8mz3CXwsMzJZR-Z0D_EFBdYm0nyyArLuG78OruWqjtXK3hXHepTFjSVJATtd0rxWl1AV9aSGA8mz_9wpAoR1R0_rawohbUgnVzK9s7A_qx5AtLXCtvUpVXgtJd2mYV6n89-vrVv7mSN9G-_5RoeVW1gn2h_CHhQeJsiNlHzNzud6CaEwnxCli2MVJuDR2XwonrJojceCYPN77eMYesZ70ZkbXTdf7PdnkNvaeCzZNeV4G7uKuHoT-QPyGCd5z2bcufhT-ZmELad7rtvGQP97hKy9eJqgTB9PkD3nRMjW08CJfCvdNUPems19LhRw818VEbihVGgA"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ZCVOZO-MXZSCM-OSTXQB-DEAVTY-ARQ"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -100546355432
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://thearq.tech"
