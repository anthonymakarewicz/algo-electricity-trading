MONTHS = ['January', 
          'February', 
          'March', 
          'April', 
          'May', 
          'June', 
          'July', 
          'August', 
          'September', 
          'October', 
          'November', 
          'December'
]

PLOT_CONFIGS = {
    "wind": {
        "title": "German day-ahead wind power forecast (MW)", 
        "label": "Wind Forecast", 
        "color": "blue", 
        "ylabel": "Megawatt (MW)"
    },
    "solar": {
        "title": "German day-ahead solar power forecast (MW)", 
        "label": "Solar Forecast", 
        "color": "orange", 
        "ylabel": "Megawatt (MW)"
    },
    "load": {
        "title": "German day-ahead load forecast (MW)", 
        "label": "Load Forecast", 
        "color": "green", 
        "ylabel": "Megawatt (MW)"
    },
    "spread": {
        "title": "Difference between Imbalances and Day-Ahead price (€)", 
        "label": "Price Spread", 
        "color": "red",  
        "ylabel": "Euro (€)"
    }
}