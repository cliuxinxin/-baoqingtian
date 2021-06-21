CREATE TABLE "Batch" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "dt" DATETIME
);

CREATE TABLE "Item" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "idx" TEXT NOT NULL,
  "dt" DATETIME
);

CREATE TABLE "Batch_Item" (
  "batch" INTEGER NOT NULL REFERENCES "Batch" ("id"),
  "item" INTEGER NOT NULL REFERENCES "Item" ("id"),
  PRIMARY KEY ("batch", "item")
);

CREATE INDEX "idx_batch_item" ON "Batch_Item" ("item");

CREATE TABLE "Label" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "dt" DATETIME,
  "item" INTEGER NOT NULL REFERENCES "Item" ("id") ON DELETE CASCADE
);

CREATE INDEX "idx_label__item" ON "Label" ("item");

CREATE TABLE "Model" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "dt" TEXT NOT NULL
);

CREATE TABLE "Process" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "dt" DATETIME,
  "item" INTEGER NOT NULL REFERENCES "Item" ("id")
);

CREATE INDEX "idx_process__item" ON "Process" ("item");

CREATE TABLE "Resource" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "dt" DATETIME
);

CREATE TABLE "Process_Resource" (
  "process" INTEGER NOT NULL REFERENCES "Process" ("id"),
  "resource" INTEGER NOT NULL REFERENCES "Resource" ("id"),
  PRIMARY KEY ("process", "resource")
);

CREATE INDEX "idx_process_resource" ON "Process_Resource" ("resource");

CREATE TABLE "Tag" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "dt" DATETIME
);

CREATE TABLE "Model_Tag" (
  "model" INTEGER NOT NULL REFERENCES "Model" ("id"),
  "tag" INTEGER NOT NULL REFERENCES "Tag" ("id"),
  PRIMARY KEY ("model", "tag")
);

CREATE INDEX "idx_model_tag" ON "Model_Tag" ("tag");

CREATE TABLE "Resource_Tag" (
  "resource" INTEGER NOT NULL REFERENCES "Resource" ("id"),
  "tag" INTEGER NOT NULL REFERENCES "Tag" ("id"),
  PRIMARY KEY ("resource", "tag")
);

CREATE INDEX "idx_resource_tag" ON "Resource_Tag" ("tag");

CREATE TABLE "Test" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL
);

CREATE TABLE "Item_Test" (
  "item" INTEGER NOT NULL REFERENCES "Item" ("id"),
  "test" INTEGER NOT NULL REFERENCES "Test" ("id"),
  PRIMARY KEY ("item", "test")
);

CREATE INDEX "idx_item_test" ON "Item_Test" ("test");

CREATE TABLE "Train" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "dt" TEXT NOT NULL,
  "model" INTEGER NOT NULL REFERENCES "Model" ("id"),
  "result" TEXT NOT NULL,
  "parameters" TEXT NOT NULL,
  "label" INTEGER NOT NULL REFERENCES "Label" ("id")
);

CREATE INDEX "idx_train__label" ON "Train" ("label");

CREATE INDEX "idx_train__model" ON "Train" ("model");

CREATE TABLE "Evaluation" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "dt" TEXT NOT NULL,
  "test" INTEGER NOT NULL REFERENCES "Test" ("id") ON DELETE CASCADE,
  "train" INTEGER NOT NULL REFERENCES "Train" ("id") ON DELETE CASCADE,
  "result" TEXT NOT NULL
);

CREATE INDEX "idx_evaluation__test" ON "Evaluation" ("test");

CREATE INDEX "idx_evaluation__train" ON "Evaluation" ("train")