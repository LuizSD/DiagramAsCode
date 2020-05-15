from urllib.request import urlretrieve
from diagrams.custom import Custom
from diagrams import Cluster, Diagram
from diagrams.azure.web import AppServices
from diagrams.azure.database import SQLDatabases
from diagrams.azure.web import APIConnections
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.azure.compute import FunctionApps

graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

react_url = "http://assets.stickpng.com/images/584830f5cef1014c0b5e4aa1.png"
react_icon = "react.png"
urlretrieve(react_url, react_icon)


with Diagram("Marketplace", show=True, graph_attr=graph_attr):

    apiSupplier = APIConnections("Supplier Api")
    sapConnection = APIConnections("Order Creation")

    with Cluster("Azure"):
        checkSupplier = FunctionApps("Supplier Api")
        checkSAPStatus = FunctionApps("Order Status")
        apiRestFul = AppServices("ApiRestFul")
        sqlServerDataBase = SQLDatabases("Database")
        reactFrontend = Custom("WebApp", react_icon) 
        checkSupplier >> apiRestFul 
        reactFrontend >> apiRestFul
        apiRestFul << checkSAPStatus
        apiRestFul >> sqlServerDataBase

    apiSupplier << checkSupplier  
    checkSAPStatus >> sapConnection
    apiRestFul >> sapConnection
