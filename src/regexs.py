# this characters need escaping . ^ $ * + ? { } [ ] \ | ( )
import resources.Constants as const

List = [
    (r"\s", None),

    ("MOD", const.STMT), # TODO
    ("NOT", const.STMT), # TODO
    ("AND", const.STMT), # TODO
    ("OR", const.STMT), # TODO

    ("\+=", const.STMT),
    ("-=", const.STMT),
    ("\*=", const.STMT),
    ("/=", const.STMT),
    ("==", const.STMT),
    ("<>", const.STMT),
    (">=", const.STMT),
    ("<=", const.STMT),
    (">=", const.STMT),

    (">>", const.STMT), # TODO
    ("<<", const.STMT), # TODO

    (r"\.", const.STMT),
    (r"\^", const.STMT),
    ("=", const.STMT),
    ("-", const.STMT),
    ("\+", const.STMT),
    (r"/", const.STMT),
    ("<", const.STMT),
    (">", const.STMT),
    ("'", const.STMT),
    (r"(^[a-z_][a-z0-9_]*)", const.ID),
    ('\"(.*)\"', const.STRING)
]
