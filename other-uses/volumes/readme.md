exists two types of volumes:
- **the bind volumes:** se mantiene en tu local y está más expuesto
- **the named volumes:** es persistente así el docker esté apagado

the next .yml has a type of bind volume:  

```bash
version: '3.8'
services:
  web:
    image: nginx
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html

```

By other hand, this is the named volume:


```bash
version: '3.8'
services:
  db:
    image: mysql
    volumes:
      - dbdata:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: example

volumes:
  dbdata:
```