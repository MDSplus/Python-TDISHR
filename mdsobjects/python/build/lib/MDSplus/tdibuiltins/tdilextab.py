# tdilextab.py. This file automatically created by PLY (version 3.4). Don't edit!
_tabversion   = '3.4'
_lextokens    = {'IAND': 1, 'INOT': 1, 'RSHIFT': 1, 'LPAREN': 1, 'LESS': 1, 'DEFAULT': 1, 'EQ_S': 1, 'ARROW': 1, 'EQUAL': 1, 'LBRACKET': 1, 'BU': 1, 'WU': 1, 'IDENT': 1, 'AND_NOT_S': 1, 'LSHIFT': 1, 'MOD_S': 1, 'FUN': 1, 'BACKQUOTE': 1, 'RAISE': 1, 'NOT_S': 1, 'MINUS': 1, 'L': 1, 'RBRACE': 1, 'CASE': 1, 'GE_S': 1, 'NOT_EQUAL': 1, 'RPAREN': 1, 'GREATER_EQUAL': 1, 'GT_S': 1, 'COLON': 1, 'QUESTION': 1, 'IOR': 1, 'SWITCH': 1, 'LU': 1, 'PLUS': 1, 'COMMA': 1, 'IDENTTYPE': 1, 'EQUALSFIRST': 1, 'SLASHSLASH': 1, 'SEMICOLON': 1, 'B': 1, 'DIVIDE': 1, 'FOR': 1, 'PLUSPLUS': 1, 'T2': 1, 'EQUALS': 1, 'FloatNum': 1, 'TIMES': 1, 'Q': 1, 'LE_S': 1, 'T': 1, 'W': 1, 'ARG_TYPE': 1, 'LESS_EQUAL': 1, 'MINUSMINUS': 1, 'ELSE': 1, 'LT_S': 1, 'GREATER': 1, 'AND': 1, 'NE_S': 1, 'LBRACE': 1, 'QU': 1, 'NAME': 1, 'IF': 1, 'WHILE': 1, 'NOR_S': 1, 'TREEPATH': 1, 'BREAK': 1, 'OR_S': 1, 'CONTINUE': 1, 'AND_S': 1, 'NOT': 1, 'RBRACKET': 1, 'AS_IS': 1, 'PLACEHOLDER': 1, 'OR': 1}
_lexreflags   = 0
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive', 'nestcomment': 'exclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_COMMENT>(/\\*(.|\\n)*?(\\*/|/\\*)))|(?P<t_T>"(?:[^"\\\\]|\\\\.)*")|(?P<t_T2>\'(?:[^\'\\\\]|\\\\.)*\')', [None, ('t_COMMENT', 'COMMENT'), None, None, None, ('t_T', 'T'), ('t_T2', 'T2')]), ('(?P<t_BU>(?i)(byte_unsigned|unsigned_byte)\\((?P<number1>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))\\)|(?P<number2>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))(bu|ub))', [None, ('t_BU', 'BU'), None, None, None, None]), ('(?P<t_WU>(?i)(word_unsigned|unsigned_word)\\((?P<number1>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))\\)|(?P<number2>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))(wu|uw))', [None, ('t_WU', 'WU'), None, None, None, None]), ('(?P<t_W>(?i)word\\((?P<number1>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))\\)|(?P<number2>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))w)', [None, ('t_W', 'W'), None, None, None]), ('(?P<t_QU>(?i)(quadword_unsigned|unsigned_quadword)\\((?P<number1>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))\\)|(?P<number2>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))(uq|qu))', [None, ('t_QU', 'QU'), None, None, None, None]), ('(?P<t_LU>(?i)(long_unsigned|unsigned_long)\\((?P<number1>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))\\)|(?P<number2>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))(lu|ul|u))', [None, ('t_LU', 'LU'), None, None, None, None]), ('(?P<t_Q>(?i)quadword\\((?P<number1>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))\\)|(?P<number2>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))q)', [None, ('t_Q', 'Q'), None, None, None]), ('(?P<t_FloatNum>(?i)([0-9]+\\.(?!\\.)[0-9]*|[0-9]*\\.[0-9]+|[0-9]+)(?P<exp>([dgef]))[-+]?[0-9]+|[0-9]+\\.(?!\\.)[0-9]*|[0-9]*\\.[0-9]+)|(?P<t_B>(?i)byte\\((?P<number1>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))\\)|(?P<number2>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))b)', [None, ('t_FloatNum', 'FloatNum'), None, None, None, ('t_B', 'B'), None, None, None]), ('(?P<t_L>(?i)long\\((?P<number1>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))\\)|(?P<number2>(0[Xx][0-9A-Fa-f]+|0[Bb][01]+|0[0-7]+|[1-9]+[0-9]*|0))l?)|(?P<t_IDENT>(?i)(\\$([a-z]+[a-z0-9_\\$]*)|(\\$[0-9]+[a-z_\\$]+[a-z0-9_\\$]*))|(_[a-z0-9_\\$]*))', [None, ('t_L', 'L'), None, None, None, None, ('t_IDENT', 'IDENT')]), ('(?P<t_PLACEHOLDER>\\$[1-9]*[0-9]*)|(?P<t_TREEPATH>(?i)(((\\\\([a-z][a-z0-9$_]*::)?|[\\.:])?[a-z][a-z0-9$_]*)|(\\.-(\\.?-)*))([\\.:][a-z][a-z0-9$_]*)*)|(?P<t_COLON>\\.\\.|:)|(?P<t_NAME>(?i)\\b[a-z]+[a-z0-9_]*\\b)|(?P<t_newline>\\n+)|(?P<t_EQUALSFIRST>\\+=|-=|\\*=|/=|\\^=|\\*\\*=|<==|>==|>>=|<<=|&=|&&=|!==|\\|=|\\|\\|=|//=)|(?P<t_RAISE>\\^|\\*\\*)|(?P<t_NOT_EQUAL>!=|<>)|(?P<t_PLUSPLUS>\\+\\+)|(?P<t_OR>\\|\\|)|(?P<t_PLUS>\\+)|(?P<t_GREATER_EQUAL>>=)|(?P<t_SLASHSLASH>//)', [None, ('t_PLACEHOLDER', 'PLACEHOLDER'), ('t_TREEPATH', 'TREEPATH'), None, None, None, None, None, None, None, ('t_COLON', 'COLON'), ('t_NAME', 'NAME'), ('t_newline', 'newline'), (None, 'EQUALSFIRST'), (None, 'RAISE'), (None, 'NOT_EQUAL'), (None, 'PLUSPLUS'), (None, 'OR'), (None, 'PLUS'), (None, 'GREATER_EQUAL'), (None, 'SLASHSLASH')]), ('(?P<t_MINUSMINUS>--)|(?P<t_AND>&&)|(?P<t_RBRACKET>\\])|(?P<t_LESS_EQUAL><=)|(?P<t_LBRACKET>\\[)|(?P<t_EQUALS>==)|(?P<t_RPAREN>\\))|(?P<t_LSHIFT><<)|(?P<t_IOR>\\|)|(?P<t_RSHIFT>>>)|(?P<t_LPAREN>\\()|(?P<t_ARROW>->)|(?P<t_QUESTION>\\?)|(?P<t_TIMES>\\*)|(?P<t_RBRACE>})|(?P<t_EQUAL>=)|(?P<t_DIVIDE>/)|(?P<t_LBRACE>{)|(?P<t_MINUS>-)|(?P<t_GREATER>>)|(?P<t_SEMICOLON>;)|(?P<t_LESS><)|(?P<t_COMMA>,)|(?P<t_NOT>!)|(?P<t_BACKQUOTE>`)|(?P<t_IAND>&)|(?P<t_INOT>~)', [None, (None, 'MINUSMINUS'), (None, 'AND'), (None, 'RBRACKET'), (None, 'LESS_EQUAL'), (None, 'LBRACKET'), (None, 'EQUALS'), (None, 'RPAREN'), (None, 'LSHIFT'), (None, 'IOR'), (None, 'RSHIFT'), (None, 'LPAREN'), (None, 'ARROW'), (None, 'QUESTION'), (None, 'TIMES'), (None, 'RBRACE'), (None, 'EQUAL'), (None, 'DIVIDE'), (None, 'LBRACE'), (None, 'MINUS'), (None, 'GREATER'), (None, 'SEMICOLON'), (None, 'LESS'), (None, 'COMMA'), (None, 'NOT'), (None, 'BACKQUOTE'), (None, 'IAND'), (None, 'INOT')])], 'nestcomment': [('(?P<t_nestcomment_comment>(.|\\n)*?(\\*/|/\\*))', [None, ('t_nestcomment_comment', 'comment')])]}
_lexstateignore = {'INITIAL': ' \t\r\x00', 'nestcomment': ' \t\r\x00'}
_lexstateerrorf = {'INITIAL': 't_ANY_error', 'nestcomment': 't_ANY_error'}
