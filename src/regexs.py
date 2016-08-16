#this characters need escaping . ^ $ * + ? { } [ ] \ | ( )
STMT = 'STMT'
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
    (r"(^[a-z_][a-z0-9_]+)(?:[\D\d]+)", STMT),
    (r"\s", None)
]
