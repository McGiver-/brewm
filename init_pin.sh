#!/bin/bash

set -e

PIN=17

echo $PIN > /sys/class/gpio/export || true
echo 'out' > /sys/class/gpio/gpio$PIN/direction
chown brewer /sys/class/gpio/gpio$PIN/*
