import csv

import sqlalchemy as sa

pg_meta = sa.MetaData()
sa_meta = sa.MetaData()

pg_engine = sa.create_engine("postgresql+psycopg://postgres:postgres@localhost:5432/postgres")
# sa_engine = sa.create_engine("mssql+pyodbc://sa:SecretPassword123@localhost:1433/master?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes")
pg_meta.create_all(pg_engine)
# sa_meta.create_all(sa_engine)

demographics_table = sa.Table("demographics", pg_meta,
                              sa.Column("zip_code", sa.String, primary_key=True),
                              sa.Column("total_population", sa.Integer),
                              sa.Column("under_5", sa.Integer),
                              sa.Column("5_to_9", sa.Integer),
                              sa.Column("10_to_14", sa.Integer),
                              sa.Column("15_to_19", sa.Integer),
                              sa.Column("20_to_24", sa.Integer),
                              sa.Column("25_to_29", sa.Integer),
                              sa.Column("30_to_34", sa.Integer),
                              sa.Column("35_to_39", sa.Integer),
                              sa.Column("40_to_44", sa.Integer),
                              sa.Column("45_to_49", sa.Integer),
                              sa.Column("50_to_54", sa.Integer),
                              sa.Column("55_to_59", sa.Integer),
                              sa.Column("60_to_64", sa.Integer),
                              sa.Column("65_to_69", sa.Integer),
                              sa.Column("70_to_74", sa.Integer),
                              sa.Column("75_to_79", sa.Integer),
                              sa.Column("80_to_84", sa.Integer),
                              sa.Column("over_85", sa.Integer),
                              )

pg_meta.create_all(pg_engine)

with open(
        "data/census.csv") as f, pg_engine.connect() as pg_conn:
    # Skip first line
    next(f)
    reader = csv.DictReader(f)
    for row in reader:
        row: dict[str, str]
        new_row = {
            "zip_code": row["Geographic Area Name"].split(" ")[1],
            "total_population": int(row['Estimate!!Total!!Total population']),
            "under_5": int(row['Estimate!!Total!!Total population!!AGE!!Under 5 years']),
            "5_to_9": int(row['Estimate!!Total!!Total population!!AGE!!5 to 9 years']),
            "10_to_14": int(row['Estimate!!Total!!Total population!!AGE!!10 to 14 years']),
            "15_to_19": int(row['Estimate!!Total!!Total population!!AGE!!15 to 19 years']),
            "20_to_24": int(row['Estimate!!Total!!Total population!!AGE!!20 to 24 years']),
            "25_to_29": int(row['Estimate!!Total!!Total population!!AGE!!25 to 29 years']),
            "30_to_34": int(row['Estimate!!Total!!Total population!!AGE!!30 to 34 years']),
            "35_to_39": int(row['Estimate!!Total!!Total population!!AGE!!35 to 39 years']),
            "40_to_44": int(row['Estimate!!Total!!Total population!!AGE!!40 to 44 years']),
            "45_to_49": int(row['Estimate!!Total!!Total population!!AGE!!45 to 49 years']),
            "50_to_54": int(row['Estimate!!Total!!Total population!!AGE!!50 to 54 years']),
            "55_to_59": int(row['Estimate!!Total!!Total population!!AGE!!55 to 59 years']),
            "60_to_64": int(row['Estimate!!Total!!Total population!!AGE!!60 to 64 years']),
            "65_to_69": int(row['Estimate!!Total!!Total population!!AGE!!65 to 69 years']),
            "70_to_74": int(row['Estimate!!Total!!Total population!!AGE!!70 to 74 years']),
            "75_to_79": int(row['Estimate!!Total!!Total population!!AGE!!75 to 79 years']),
            "80_to_84": int(row['Estimate!!Total!!Total population!!AGE!!80 to 84 years']),
            "over_85": int(row['Estimate!!Total!!Total population!!AGE!!85 years and over']),

        }
        sql = demographics_table.insert().values(new_row)
        pg_conn.execute(sql)
    pg_conn.commit()
