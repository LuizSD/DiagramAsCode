from diagrams import Cluster, Diagram
from diagrams.azure.web import AppServices
from diagrams.azure.database import SQLDatabases
from diagrams.azure.web import APIConnections
from diagrams.azure.compute import FunctionApps
from diagrams.azure.mobile import AppServiceMobile
from diagrams.programming.framework import React

graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

with Diagram("Cashback", show=True, graph_attr=graph_attr, direction="TB"):

    
        
    with Cluster("Internal"):
        with Cluster("Azure"):
            checkSupplier = FunctionApps("Push Notification")
            apiRestFul = AppServices("ApiRestFul")
            sqlServerDataBase = SQLDatabases("Database")
            apiRestFul >> sqlServerDataBase

        with Cluster("Aplicativos"):
            reactAppClient = AppServiceMobile("App Cliente")
            reactAppParnet = AppServiceMobile("App Parceiro") 

    with Cluster("External"):
        agendamentoApi = APIConnections("Agendamento")
        carteiraApi = APIConnections("Pagamento Api")
        cashBackApi = APIConnections("CashBack Api")
    
    reactAppClient >> apiRestFul
    reactAppParnet >> apiRestFul
    apiRestFul << checkSupplier
    checkSupplier >> reactAppClient
    apiRestFul >> [cashBackApi, carteiraApi, agendamentoApi]
    
