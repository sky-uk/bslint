# this characters need escaping . ^ $ * + ? { } [ ] \ | ( )
import resources.Constants as const

List = [
    (r"\s", None),
    ("\+=", const.STMT),
    ("-=", const.STMT),
    ("\*=", const.STMT),
    ("/=", const.STMT),
    ("==", const.STMT),
    ("<>", const.STMT),
    (">=", const.STMT),
    ("<=", const.STMT),
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
