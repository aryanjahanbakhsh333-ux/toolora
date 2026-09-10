# Toolora Production Deployment Guide

## Prerequisites

- Docker and Docker Compose installed
- Domain name (e.g., toolora.com)
- SSL Certificate (Let's Encrypt recommended)
- Server with at least 2GB RAM

## Quick Start with Docker

### 1. Clone the repository
```bash
git clone https://github.com/aryanjahanbakhsh333-ux/Toolora.git
cd Toolora
```

### 2. Setup environment
```bash
cp .env.example .env
# Edit .env with your settings
vi .env
```

### 3. Generate Sitemap
```bash
python scripts/generate_sitemap.py > public/sitemap.xml
```

### 4. Build and run with Docker Compose
```bash
docker-compose up -d
```

### 5. Initialize database
```bash
docker-compose exec toolora python -c "from app.database import init_db; init_db()"
```

### 6. Access the application
- Application: http://localhost:8000
- Or with your domain: https://toolora.com

## SSL Setup (Let's Encrypt)

### Install Certbot
```bash
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx
```

### Generate Certificate
```bash
sudo certbot certonly --standalone -d toolora.com -d www.toolora.com
```

### Copy certificates
```bash
sudo cp /etc/letsencrypt/live/toolora.com/fullchain.pem ./certs/
sudo cp /etc/letsencrypt/live/toolora.com/privkey.pem ./certs/
```

## Production Configuration

### Environment Variables
```bash
DEBUG=False
RELOAD=False
ALLOWED_HOSTS=toolora.com,www.toolora.com
CORS_ORIGINS=https://toolora.com,https://www.toolora.com
```

### Security
- Enable HTTPS
- Configure firewall rules
- Set up fail2ban for DDoS protection
- Regular backups of database

### Monitoring
- Monitor logs: `docker-compose logs -f toolora`
- Check health: `curl http://localhost:8000/health`

## Performance Optimization

- Enable Gzip compression (configured in nginx.conf)
- Static files cached for 30 days
- Rate limiting enabled (100 req/min general, 30 req/min for API)
- Database indexing on frequently queried columns

## Troubleshooting

### Port already in use
```bash
# Change port in docker-compose.yml
# Or kill existing process
sudo lsof -i :8000
sudo kill -9 <PID>
```

### Database issues
```bash
# Reset database
rm toolora.db
docker-compose restart
```

### Permission denied
```bash
# Fix permissions
chmod 755 public/
chmod 644 public/robots.txt
```

## Scaling

For high traffic:
- Increase worker processes: `worker_processes auto;` in nginx.conf
- Use external database (PostgreSQL)
- Implement caching layer (Redis)
- Use CDN for static files

## Backup and Recovery

```bash
# Backup database
docker-compose exec toolora sqlite3 toolora.db ".dump" > backup.sql

# Restore database
docker-compose exec toolora sqlite3 toolora.db < backup.sql
```
