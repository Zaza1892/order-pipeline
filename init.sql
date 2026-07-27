create table order_lookups (
    id serial primary key,
    message_id text unique not null,
    order_id int not null,
    customer_id int not null,
    adress text ,
    products JSONB,
    event_timestamp TIMESTAMPTZ,
    raw_payload JSONB
)