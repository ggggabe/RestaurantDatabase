use Food;

select restaurant_name, v_factor, avg_tip from
-- restaurant and v_factor
((select restaurant_name, veggie_count/total_count as v_factor from
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
        natural join
-- restaurant and average tip
(select restaurant_name, avg(tip) as avg_tip
    from Visit
    group by restaurant_name) g)

order by v_factor desc
into outfile '/tmp/v_factor_vs_average_tip.csv'
fields terminated by ','
lines terminated by '\n';
