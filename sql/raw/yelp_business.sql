CREATE VIEW Reviews.raw.yelp_business as
select *
from datalake."demo-datalake"."extract"."yelp_academic_dataset_business.json"