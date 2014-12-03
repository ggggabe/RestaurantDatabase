use Food;

select z.name, day, csm

where 
(select z.name, day, avg_tip+veggie_count *
    (select v_factor from
    (select restaurant_name, veggie_count/total_count as v_factor from
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
        group by restaurant_name) c)) h
    where restaurant_name = 'Harvest') as csm
    from
    ((select day, avg(tip) as avg_tip from
        (select * from Visit where restaurant_name = 'Harvest') a
    group by day) c
    natural join
    (select day, count(*) as veggie_count from
        ((select * from Visit where restaurant_name = 'Harvest') a
            natural join
        Patron)
        where veggie = 'Y'
    group by day) i))

-- restaurant and v_factor
-- (select v_factor from
-- ((select restaurant_name, veggie_count/total_count as v_factor from
--     ((select restaurant_name, count(item_name) as veggie_count
--     from
--         (Serves
--         natural join
--         (select name as item_name, veggie from Item) d)
--     where veggie = 'Y'
--     group by restaurant_name) e
--         natural join
--     (select restaurant_name, count(item_name) as total_count
--     from Serves
--     group by restaurant_name) c)) h)
-- where restaurant_name = 'Harvest')

into outfile '/tmp/csm.csv'
fields terminated by ','
lines terminated by '\n';
