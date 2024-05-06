CREATE
OR REPLACE VIEW Reviews.raw.yelp_tips as
select *
from datalake."demo-datalake"."extract"."yelp_academic_dataset_tip.json"