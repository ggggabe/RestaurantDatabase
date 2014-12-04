#!/bin/bash

mysql < avg_csm_vs_yelp_factor.sql
mysql < v_factor_vs_average_tip.sql 
mysql < v_factor_vs_yelp_factor.sql
mysql < reviews.sql 
mysql < csm.sql

mv /tmp/avg_csm_vs_yelp_factor.csv .
mv /tmp/v_factor_vs_average_tip.csv . 
mv /tmp/v_factor_vs_yelp_factor.csv .
mv /tmp/reviews.csv . 
mv /tmp/csm.csv .

python plot_v_factor_vs_average_tip.py
python plot_v_factor_vs_yelp_factor.py
python plot_avg_csm_vs_yelp_factor.py
