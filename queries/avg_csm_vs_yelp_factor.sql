use Food;

select restaurant_name, avg_csm, yelp_factor from
(
    select restaurant_name, avg(csm) as avg_csm from
    (
        select day, restaurant_name, avg_tip+veggie_count*v_factor as csm from
    
        (
        select day, restaurant_name, avg(tip) as avg_tip
        from Visit
        group by day, restaurant_name
        ) g
        natural join
        (
        select day, restaurant_name, count(*) as veggie_count
        from Visit natural join Patron
        where veggie = 'Y'
        group by day, restaurant_name
        ) h
        natural join
        (
        select restaurant_name, veggie_count/total_count as v_factor from
            ((select restaurant_name, count(item_name) as veggie_count
            from
                (Serves
                natural join
                (select name as item_name, veggie from Item) d)
            where veggie = 'Y'
            group by restaurant_name) e
                natural join
            (select restaurant_name, count(item_name) as total_count
            from Serves
            group by restaurant_name) c)
        ) j
    ) k
    group by restaurant_name
) l
natural join
(select restaurant_name, avg(positive) as yelp_factor
    from Reviewed
    group by restaurant_name) m

order by avg_csm desc

into outfile '/tmp/avg_csm_vs_yelp_factor.csv'
fields terminated by ','
lines terminated by '\n';
