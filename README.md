# Code located in AWM_CA Branch
Student Number: D18123630
Student Name: Junhan Dang


# Advanced Web Mapping Project (AWM_CA)

This project is an advanced web mapping application that integrates Django, PostGIS, Leaflet.js, and Nginx. The primary purpose of this application is to provide a location-based service with map visualization, allowing users to interact with geospatial data.

## Project Structure

- **Django**: Backend framework for handling requests and serving map data.
- **PostGIS**: PostgreSQL extension for spatial data support.
- **Leaflet.js**: Frontend JavaScript library for interactive maps.
- **Nginx**: Web server and reverse proxy for handling HTTPS and forwarding requests.
- **Certbot**: Tool for obtaining SSL certificates to secure the application.

## Features

- Location-based service using PostGIS for spatial data storage.
- Interactive map rendering with Leaflet.js.
- Secure HTTPS access using Let's Encrypt SSL certificate.
- Administrative interface through Django Admin.

## Prerequisites

- Docker & Docker Compose
- AWS account with a configured EC2 instance
- Domain name for application deployment

## Setup and Deployment

### Step 1: Configure AWS and Domain Name

1. **AWS EC2 Setup**: Launch an EC2 instance and set up necessary security groups to allow traffic on ports 80 and 443.
2. **Domain Setup**: Point your domain to the public IP of your EC2 instance (e.g., using GoDaddy or your domain registrar).


