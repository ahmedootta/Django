# Django Training Repo

A Django learning/practice project with two apps:

- **`trackingsystem`** — a working order-tracker: add an order (id, name, username,
  status) through a Django form, orders are stored/read from a CSV file, and listed
  on an index page. Routes: `/trackingsystem/` (list), `/trackingsystem/add`,
  `/trackingsystem/order/<id>`.
- **`mart`** — an e-commerce app scaffold (`startapp mart`), not yet implemented.

## Getting Started

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

Then visit `/trackingsystem/`.
