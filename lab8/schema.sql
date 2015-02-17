BEGIN;
CREATE TABLE "order_customer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customer_name" varchar(128) NULL, "customer_address" varchar(64) NULL, "customer_phone" varchar(24) NULL);
CREATE TABLE "order_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "order_amount" integer NOT NULL, "order_date" date NOT NULL, "order_customer_id_id" integer NOT NULL REFERENCES "order_customer" ("id"));
CREATE TABLE "order_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "product_name" varchar(128) NULL, "product_price" decimal NOT NULL, "product_type" varchar(128) NULL, "product_description" text NOT NULL);
CREATE TABLE "order_stock" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "stock_quantity" integer NOT NULL, "stock_product_id_id" integer NOT NULL REFERENCES "order_product" ("id"));
CREATE TABLE "order_order__new" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "order_amount" integer NOT NULL, "order_date" date NOT NULL, "order_customer_id_id" integer NOT NULL REFERENCES "order_customer" ("id"), "order_product_id_id" integer NOT NULL REFERENCES "order_product" ("id"));
INSERT INTO "order_order__new" ("order_amount", "order_product_id_id", "id", "order_date", "order_customer_id_id") SELECT "order_amount", NULL, "id", "order_date", "order_customer_id_id" FROM "order_order";
DROP TABLE "order_order";
ALTER TABLE "order_order__new" RENAME TO "order_order";
CREATE INDEX "order_stock_7ddac4af" ON "order_stock" ("stock_product_id_id");
CREATE INDEX "order_order_e89d72db" ON "order_order" ("order_customer_id_id");
CREATE INDEX "order_order_72978deb" ON "order_order" ("order_product_id_id");

COMMIT;
