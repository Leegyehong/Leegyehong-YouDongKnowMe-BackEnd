CREATE DATABASE crawled_data;
CREATE DATABASE airflow;

\c crawled_data;
CREATE TABLE noti (
	major_code int NOT NULL,
	num int NOT NULL,
	title text NULL,
	writer text NULL,
	"date" text NULL,
	"content" text NULL,
	img_url text NULL,
	file_url text NULL,
    primary key(major_code, num)
);

CREATE TABLE schedule (
	id SERIAL PRIMARY KEY,
	month int NOT NULL,
	"date" text NOT NULL,
	"content" text NULL
);