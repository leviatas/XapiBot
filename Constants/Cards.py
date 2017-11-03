actions = {
    "Ver" : {
        "costo" : "2",
        "comando" : "_Ver" 
    },
    "Limpiar" : {
        "costo" : "3",
        "comando" : "_Limpiar" 
    },
    "Asesinar" : {
        "costo" : "Mitad +1",
        "comando" : "_Ver" 
    },
    "Ver" : {
        "costo" : "Cantidad de jugadores investigadores",
        "comando" : "_Ver" 
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
