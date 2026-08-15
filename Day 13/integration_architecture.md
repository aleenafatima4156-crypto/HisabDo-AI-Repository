# Day 13 – AI Integration Architecture

## Smart Expense Categorization

User
↓
Website / Web Application / Mobile Application
↓
HisabDo Backend
↓
Flask REST API - POST /categorize
↓
Input Validation
↓
TF-IDF Text Processing
↓
Logistic Regression ML Model
↓
Category + Confidence + Processing Time
↓
Response Validation
↓
JSON Response
↓
Application

## Integration Strategy

The AI service is exposed through a REST API so that different
HisabDo application clients can use the same ML service.

### Website

Website → Backend → AI API → ML Model → JSON Response → Website

### Web Application

Web App → Backend/API → AI Service → ML Model → JSON Response → Web App

### Mobile Application

Mobile App → Backend → AI API → ML Model → JSON Response → Mobile App