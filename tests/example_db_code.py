# -*- coding: utf-8 -*-
#
# Open this file in Vim, visual select (Ctrl-V) one of the SQL
# statements and !fmtsql them.
#

def one():
    sql_statement = """select s.name as shop, c.shop_id, description as category, c.category_id, count(*) as count_clickouts
    from aggregations.clickout c
    left join views.category ca on ca.category_id = c.category_id
    left join views.shop s on s.shop_id = c.shop_id
    left join views.traffic_channel t on t.mediacode_token = c.mc_token
    where reclick = false and (crawler_id is null or crawler_id = 0) and traffic_group in (2,5,6,7) and t_date >= date_sub(current_date,31) and t_date < current_date
    group by s.name, description, c.shop_id,c.category_id
    order by s.name desc""" + "; -- whatever"
    db.execute(sql_statement)


def two():
    sql_statement = """
    select s.name as shop, c.shop_id, description as category, c.category_id, count(*) as count_clickouts
    from aggregations.clickout c
    left join views.category ca on ca.category_id = c.category_id
    left join views.shop s on s.shop_id = c.shop_id
    left join views.traffic_channel t on t.mediacode_token = c.mc_token
    where reclick = false and (crawler_id is null or crawler_id = 0) and traffic_group in (2,5,6,7) and t_date >= date_sub(current_date,31) and t_date < current_date
    group by s.name, description, c.shop_id,c.category_id
    """
    db.execute(sql_statement)
