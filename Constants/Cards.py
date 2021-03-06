actions = {
    "Ver" : {
        "costo" : "2",
        "comando" : "Ver" 
    },
    "Limpiar" : {
        "costo" : "3",
        "comando" : "Limpiar" 
    },
    "Asesinar" : {
        "costo" : "Mitad +1",
        "comando" : "Asesinar" 
    },
    "Exorcisar" : {
        "costo" : "Cantidad de jugadores investigadores",
        "comando" : "Exorcisar" 
    }
}

playerSets = {
    # only for testing purposes
    
    5: {
        "roles": [
            "Investigador",
            "Investigador",
            "Investigador",
            "Investigador",
            "Cultista"
        ],
        "track": [
            None,
            None,
            "policy",
            "kill",
            "kill",
            "win"
        ]
    },
    6: {
        "roles": [
            "Investigador",
            "Investigador",
            "Investigador",
            "Investigador",
            "Cultista",
            "Cultista"
        ],
        "track": [
            None,
            None,
            "policy",
            "kill",
            "kill",
            "win"
        ]
    },
    7: {
        "roles": [
            "Investigador",
            "Investigador",
            "Investigador",
            "Investigador",
            "Investigador",
            "Cultista",
            "Cultista"
        ],
        "track": [
            None,
            "inspect",
            "choose",
            "kill",
            "kill",
            "win"
        ]
    },
    8: {
        "roles": [
            "Investigador",
            "Investigador",
            "Investigador",
            "Investigador",
            "Investigador",
            "Investigador",
            "Cultista",
            "Cultista"
        ],
        "track": [
            None,
            "inspect",
            "choose",
            "kill",
            "kill",
            "win"
        ]
    },
    9: {
        "roles": [
            "Investigador",
            "Investigador",
            "Investigador",
            "Investigador",
            "Investigador",
            "Investigador",
            "Cultista",
            "Cultista",
            "Cultista"
        ],
        "track": [
            "inspect",
            "inspect",
            "choose",
            "kill",
            "kill",
            "win"
        ]
    },
}

policies = [
        "liberal",
        "liberal",
        "liberal",
        "liberal",
        "liberal",
        "liberal",
        "fascist",
        "fascist",
        "fascist",
        "fascist",
        "fascist",
        "fascist",
        "fascist",
        "fascist",
        "fascist",
        "fascist",
        "fascist"
    ]
