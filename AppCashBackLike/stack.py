from diagrams import Cluster, Diagram
from diagrams.programming.framework import React
from diagrams.programming.language import Csharp
from diagrams.azure.database import SQLDatabases

graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

with Diagram("Stack", show=True, graph_attr=graph_attr):

    mobileApps = React("Android/IOS Apps")
    with Cluster("Azure"):
        apiRestFul = Csharp("ApiRestFul")
        sqlServerDataBase = SQLDatabases("Database")
    mobileApps - apiRestFul - sqlServerDataBase

