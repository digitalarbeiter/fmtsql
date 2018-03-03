# fmtsql SQL formatter/beautifier script

The fmtsql script reads an SQL block from stdin (possibly within a
Python """ string construct), formats it (using sqlparse.format), and
prints the formatted SQL to stdout (in my preferred style).

The script is intended to be invoked from within Vim on a visual selection,
and can handle two classic situations:

    stmt = """select whatever from wherever
    join evenmore on my_arse """ + where_stmt

and
    stmt = """
        select whatever from wherever
        join evenmore on my_arse
    """ + where_stmt

In both cases in Vim just Ctrl-V the statement and !fmtsql it right away.
The script will take care of the triplequotes, prefix ("stmt =") and
postfix (the "+ wherei\_stmt" part) as well as the Python indentation.

Limitations:
 * statements in single " or ' quotes are not supported.
 * multiple """ blocks cannot currently be handled.
