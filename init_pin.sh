#!/bin/bash

set -e

echo '3' > /sys/class/gpio/export
chown brewer /sys/class/gpio/gpio3/*
