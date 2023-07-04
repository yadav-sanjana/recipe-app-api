#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/niginx/conf.d/default.conf
nginx -g 'daemon off;'