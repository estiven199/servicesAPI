
CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE packages (
  id SERIAL PRIMARY KEY,
  description TEXT,
  price INTEGER,
  "typeOfServiceID" INTEGER,
  FOREIGN KEY ("typeOfServiceID") REFERENCES services(id)
);

CREATE TABLE deliverables (
  id SERIAL PRIMARY KEY,
  name TEXT,
  package_id INTEGER,
  FOREIGN KEY (package_id) REFERENCES packages(id)
);

