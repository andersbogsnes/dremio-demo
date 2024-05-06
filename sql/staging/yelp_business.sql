CREATE TABLE Nessie.staging.yelp_business as

SELECT business_id as yelp_id,
       "name"      as business_name,
       address,
       city,
       "state",
       postal_code,
       latitude,
       longitude,
       stars,
       review_count,
       CAST
       (
               is_open as
           BOOLEAN
       )           as is_open,
       attributes,
       hours,
       REGEXP_SPLIT
       (
               categories,
               ', ',
               'INDEX',
               0
       )           as categories
from Reviews.raw.yelp_business;

CREATE
or replace VIEW Reviews.staging.yelp_business as
select *
from Nessie.staging.yelp_business at branch main;