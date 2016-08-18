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
    (r"\\=", const.STMT), # divide integer
    ("<<=", const.STMT),
    (">>=", const.STMT),
    ("==", const.STMT),
    ("<>", const.STMT),
    (">=", const.STMT),
    ("<=", const.STMT),
    (">=", const.STMT),
    ("=>", const.STMT),
    ("=<", const.STMT),

    (">>", const.STMT), # TODO
    ("<<", const.STMT), # TODO

    (r"\.", const.STMT),
    (r"\^", const.STMT),
    ("=", const.STMT),
    ("-", const.STMT),
    ("\+", const.STMT),
    ("\*", const.STMT),
    (r"/", const.STMT),
    ("<", const.STMT),
    (">", const.STMT),
    ("'", const.STMT),

    ("FOR EACH", const.STMT),
    ("END FOR", const.STMT),
    ("ELSE IF", const.STMT),
    ("EXIT FOR", const.STMT),
    ("END IF", const.STMT),
    ("END WHILE", const.STMT),
    ("EXIT WHILE", const.STMT),
    ("END FOR", const.STMT),
    ("IF", const.STMT),
    ("THEN", const.STMT),
    ("ELSE", const.STMT),
    ("FOR", const.STMT),
    ("TO", const.STMT),
    ("END", const.STMT),
    ("STEP", const.STMT),
    ("IN", const.STMT),
    ("WHILE", const.STMT),

    (r"(^[a-z_][a-z0-9_]*)", const.ID),
    ('\"(.*)\"', const.STRING)
]
