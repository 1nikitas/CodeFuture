from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


keyboard = InlineKeyboardMarkup(row_width=1,
                                       inline_keyboard=[
                                            [InlineKeyboardButton(text='КЛАССНАЯ', url='https://official.contest.yandex.ru/futurecode/contest/41525/enter'),
                                            InlineKeyboardButton(text="ДЗ", url="https://official.contest.yandex.ru/futurecode/contest/41524/enter"),
                                            ],
                                           [InlineKeyboardButton(text='Конспект 1', url='https://drive.google.com/drive/folders/1INOVdjBo0v_Dt7Tcm0q1LRE_dL8h2NXl?usp=share_link'),
                                            InlineKeyboardButton(text="Разбор 1", url="https://drive.google.com/drive/folders/1INOVdjBo0v_Dt7Tcm0q1LRE_dL8h2NXl?usp=share_link"),
                                            ],
                                           [InlineKeyboardButton(text='Конспект 2', url='https://drive.google.com/file/d/1Tg_l-JpH19gZdtxC7J4mTOWlsjRX7Ejx/view?usp=share_link'),
                                            InlineKeyboardButton(text="Разбор 2", url="https://drive.google.com/drive/folders/1INOVdjBo0v_Dt7Tcm0q1LRE_dL8h2NXl?usp=share_link"),
                                            ],
                                           [InlineKeyboardButton(text='Конспект 3', url='https://drive.google.com/drive/folders/1owJ45dnwu829Xk8Kzhz6fN-THWieRtqi?usp=share_link'),
                                            InlineKeyboardButton(text="Разбор 3", url="https://docs.google.com/document/d/1urvQIU8FLziMtPtic-Z239v_Pge4PZ3ovpTQ0jK6fTQ/edit?usp=sharing"),
                                            ],
                                           [InlineKeyboardButton(text='ДЕМО КР', url='https://docs.google.com/document/d/1tetKRMAJ8vjfRB6Dp3a5rfyi-JAeq9jpGRdHdSjXweE/edit?usp=share_link'),
                                            InlineKeyboardButton(text="РАЗБОР ДЕМО КР", url="https://docs.google.com/document/d/1F1pgBpaGRlVdx46J8gEftcxpBX9G9Q-k/edit"),
                                            ],
                                            [
                                            InlineKeyboardButton(text='КР', url='https://official.contest.yandex.ru/contest/43293/enter/'),
                                           ]

                                       ]
                                    )

