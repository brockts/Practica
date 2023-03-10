"""
    comandos usados para crear la DB:
        `docker run --name djangoc -e POSTGRES_USER=mois -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres`
        nombre de base de datos creada por defecto `mois`
        `docker run --name djangoc -e POSTGRES_USER=mois -e POSTGRES_PASSWORD=password -e POSTRGRES_DB=practicadb -p 5432:5432 -d postgres`

    En caso de el siguiente error:
        `raise ImproperlyConfigured("Error loading psycopg2 module: %s" % e)
        django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 module: No module named 'psycopg2'`
        >>> hacer uso del siguiente comando
        ... pip install psycopg2
        para instalar la dependencia `psycopg2` y poder conectar el proyecto a PostgreSQL 
"""
