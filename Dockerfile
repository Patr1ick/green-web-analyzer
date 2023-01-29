FROM caddy:2.6.2

COPY Caddyfile /etc/caddy/Caddyfile
COPY ./frontend/dist /srv