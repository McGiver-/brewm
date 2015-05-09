BrewM
=====

Virtual reality can suck it. Reality has coffee.

Coffeemaker controllable via a web interface, and HTCPCP.

API
-----

The API uses JSON for everything, because JSON is the only real dev data
interchange format.

* GET /api/status

    Describes the state of the coffeemaker.

        {
            'brewing': boolean,
            'coffee': float, (between 0.0 and 1.0)
            'water': float (between 0.0 and 1.0)
        }

* GET /api/specs

    Describes the static specifications of the coffeemaker.

        {
            'capacity': {
                'cups': integer, (advertized number of cups brewed)
                'ml': float (milliliters of fluid max)
            }
        }

* POST /api/brew

    Control brewing state.

        {
            'brewing': boolean,
            'time': float, (optional; number of seconds)
        }
