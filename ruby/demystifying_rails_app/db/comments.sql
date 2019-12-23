-- db/comments.sql --

CREATE TABLE "comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "body" text,
  "author" varchar,
  "post_id" integer,
  "created_at" datetime NOT NULL);
