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
            'time': int, (time left for the brew to complete)
        }

* GET /api/specs

    Describes the static specifications of the coffeemaker.

        {
            'brewTime': int (number of seconds to brew a pot)
        }

* POST /api/brew

    Control brewing state.

        {
            'brewing': boolean,
        }
