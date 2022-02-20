from django.shortcuts import render

import asyncio

from .filters import FilterDatabase


async def get_client(db, first_name, last_name, email):
    """Get a client from a database."""
    database = FilterDatabase(db)
    return database.query(first_name=first_name, last_name=last_name, email=email)

async def multiple_databases(request):
    """
    Retrieve a client from multiple databases.
    Return the client's datas.
    """
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        clients = asyncio.create_task(get_client("default", first_name, last_name, email))
        clients_db1 = asyncio.create_task(get_client("db_1", first_name, last_name, email))
        default_clients = await clients
        db1_clients = await clients_db1
        context = {"clients":default_clients, "clients_db1": db1_clients}
        return render(request, "index.html", context)
    return render(request,"index.html")
