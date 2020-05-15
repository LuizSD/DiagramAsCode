from urllib.request import urlretrieve
from diagrams.custom import Custom
from diagrams import Cluster, Diagram
from diagrams.azure.web import AppServices
from diagrams.azure.database import SQLDatabases
from diagrams.azure.web import APIConnections
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.azure.compute import FunctionApps

react_url = "http://assets.stickpng.com/images/584830f5cef1014c0b5e4aa1.png"
react_icon = "react.png"
urlretrieve(react_url, react_icon)


with Diagram("Marketplace", show=False):

    checkSupplier = FunctionApps("Supplier Connection")

    apiSupplier = APIConnections("Supplier Api")

    apiRestFul = [AppServices("ApiRestFul")]

    sqlServerDataBase = SQLDatabases("Database")

    sapConnection = APIConnections("SAP Conection")

    checkSAPStatus = FunctionApps("SAP Status")

    reactFrontend = Custom("WebApp", react_icon)

    
    reactFrontend >> apiRestFul
    checkSupplier >> apiRestFul
    checkSupplier >> apiSupplier 
    apiRestFul >> sqlServerDataBase
    apiRestFul >> sapConnection
    checkSAPStatus >> sapConnection
    checkSAPStatus >> apiRestFul