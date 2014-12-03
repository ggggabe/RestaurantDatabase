use Food;

select vegetarian, meat_eater, vegetarian/meat_eater as ratio
    from
    (select count(*) as vegetarian
        from
        (select *
            from
            Reviewed r
            where
            (select veggie
                from
                Patron p
                where
                    p.firstname = r.firstname
                    and
                    p.lastname = r.lastname
            ) = 'Y'
        ) c
    ) a,
    (select count(*) as meat_eater
        from
        (select *
            from
            Reviewed r
            where
            (select veggie
                from
                Patron p
                where
                    p.firstname = r.firstname
                    and
                    p.lastname = r.lastname
            ) = 'N'
        ) d
    ) b

into outfile '/tmp/reviews.csv'
fields terminated by ','
lines terminated by '\n';
