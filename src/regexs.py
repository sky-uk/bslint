# this characters need escaping . ^ $ * + ? { } [ ] \ | ( )
STMT = 'STMT'
ID = 'ID'
List = [
    (r"\s", None),
    ("\+=", STMT),
    ("-=", STMT),
    ("\*=", STMT),
    ("/=", STMT),
    ("==", STMT),
    ("<>", STMT),
    (">=", STMT),
    ("<=", STMT),
    (r"\.", STMT),
    (r"\^", STMT),
    ("=", STMT),
    ("-", STMT),
    ("\+", STMT),
    (r"/", STMT),
    ("<", STMT),
    (">", STMT),
    ("'", STMT),
    (r"(^[a-z_][a-z0-9_]*)", ID)
]
