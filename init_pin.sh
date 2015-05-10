#!/bin/bash

set -e

PIN=17

echo $PIN > /sys/class/gpio/export || true
echo 'out' > /sys/class/gpio/gpio$PIN/direction
echo '0' > /sys/class/gpio/gpio$PIN/value
chown brewer /sys/class/gpio/gpio$PIN/*
