# this characters need escaping . ^ $ * + ? { } [ ] \ | ( )
STMT = 'STMT'
ID = 'ID'
List = [
    ("\+=", STMT),
    ("-=", STMT),
    ("\*=", STMT),
    ("/=", STMT),
    ("==", STMT),
    ("=", STMT),
    ("-", STMT),
    ("\+", STMT),
    (r"/", STMT),
    ("<", STMT),
    (">", STMT),
    ("<>", STMT),
    (">=", STMT),
    ("<=", STMT),
    (r"\.", STMT),
    (r"\^", STMT),
    ("'", STMT),
    (r"(^[a-z_][a-z0-9_]*)", ID),
    (r"\s", None)
]
