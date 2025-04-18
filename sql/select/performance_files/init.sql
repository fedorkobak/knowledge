CREATE TABLE tenk1 (
    unique1     int4,
    unique2     int4,
    two        int4,
    four        int4,
    ten        int4,
    twenty      int4,
    hundred    int4,
    thousand    int4,
    twothousand int4,
    fivethous   int4,
    tenthous    int4,
    odd         int4,
    even        int4,
    stringu1    name,
    stringu2    name,
    string4     name
);

COPY tenk1 FROM '/data/tenk.data' WITH (FORMAT 'text', DELIMITER E'\t');
