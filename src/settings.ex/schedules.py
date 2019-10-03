from datetime import datetime as dt
from datetime import timedelta as td
import pytz

SCHEDULES = [
    # daily work card
    {
        # cron-like schedule (pycron)
        'schedule': '0 8 * * 1-5',

        # target board and list
        'board': '<board-id>',
        'list': '<list-id>',

        # required fields
        'card': {
            'title': 'check for donuts',
        },

        # more card details
        # https://wekan.github.io/api/v3.00/#put_board_list_card
        'details': {
            'description': 'first-come, first-served',
            'color': 'pink',
            'labelIds': ['<label-id>'],
            'members': ['<user-id>'],
            # set due time to 17 o'clock
            # 'dueAt': lambda: dt.now().replace(hour=17, minute=0, second=0, microsecond=0).astimezone(pytz.utc).isoformat(),
            # set due time to tomorrow 17 o'clock
            # 'dueAt': lambda: (dt.now() + td(days=1)).replace(hour=17, minute=0, second=0, microsecond=0).astimezone(pytz.utc).isoformat(),
        },
    },
]
