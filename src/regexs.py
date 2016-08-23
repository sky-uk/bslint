# this characters need escaping . ^ $ * + ? { } [ ] \ | ( )
import resources.Constants as const

List = [
    (r"\n", const.NEW_LINE),
    (r"\s", None),

    ("\+=", const.STMT),
    ("-=", const.STMT),
    ("\*=", const.STMT),
    ("/=", const.STMT),
    (r"\\=", const.STMT),  # divide integer
    ("<<=", const.STMT),
    (">>=", const.STMT),
    ("<>", const.STMT),
    (">=", const.STMT),
    ("<=", const.STMT),
    (">=", const.STMT),
    ("=>", const.STMT),
    ("=<", const.STMT),

    (">>", const.STMT),
    ("<<", const.STMT),

    (r"\.", const.STMT),
    (r"\^", const.STMT),
    ("=", const.STMT),
    ("-", const.STMT),
    ("\+", const.STMT),
    ("\*", const.STMT),
    (r"/", const.STMT),
    ("<", const.STMT),
    (">", const.STMT),
    (r"\(", const.STMT),
    (r"\)", const.STMT),
    (r"\[", const.STMT),
    (r"\]", const.STMT),

    ("TRUE", const.STMT),
    ("GETLASTRUNCOMPILEERROR", const.STMT),
    ("GETLASTRUNRUNTIMEERROR", const.STMT),
    ("GETGLOBALAA", const.STMT),
    ("ELSE IF", const.STMT),
    ("END IF", const.STMT),
    ("EXIT FOR", const.STMT),
    ("FOR EACH", const.STMT),
    ("END FOR", const.STMT),
    ("END WHILE", const.STMT),
    ("EXIT WHILE", const.STMT),
    ("END FUNCTION", const.STMT),
    ("END SUB", const.STMT),
    ("LINE_NUM", const.STMT),
    ("GOTO", const.STMT),
    ("CREATEOBJECT", const.STMT),
    ("ENDIF", const.STMT),
    ("ENDSUB", const.STMT),
    ("ENDWHILE", const.STMT),
    ("EXITWHILE", const.STMT),
    ("OBJFUN", const.STMT),

    ("IF", const.STMT),
    ("THEN", const.STMT),
    ("ELSE", const.STMT),
    ("FOR", const.STMT),
    ("TO", const.STMT),
    ("STEP", const.STMT),
    ("INVALID", const.STMT),
    ("IN", const.STMT),
    ("WHILE", const.STMT),
    ("FUNCTION", const.STMT),
    ("AS", const.STMT),
    ("RETURN", const.STMT),
    ("PRINT", const.STMT),
    ("DIM", const.STMT),
    ("END", const.STMT),
    ("MOD", const.STMT),
    ("STOP", const.STMT),
    ("AND", const.STMT),
    ("BOX", const.STMT),
    ("EACH", const.STMT),
    ("EVAL", const.STMT),
    ("EXIT", const.STMT),
    ("FALSE", const.STMT),
    ("LET", const.STMT),
    ("NEXT", const.STMT),
    ("NOT", const.STMT),
    ("OR", const.STMT),
    ("POS", const.STMT),
    ("REM", const.STMT),
    ("RUN", const.STMT),
    ("SUB", const.STMT),
    ("TAB", const.STMT),
    ("TYPE", const.STMT),

    ("MAIN", const.STMT),

    (r"(?P<value>^[a-z_][a-z0-9_]*)(?P<type>\$|%|!|#|&?)", const.ID),
    ('\"(.*)\"', const.STRING),
    (r"^\d*(\.?\d+){1}", const.NUMERIC),
    (r"'(.*)\n", None)
]
