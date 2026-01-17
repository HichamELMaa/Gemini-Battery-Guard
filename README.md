# Gemini-Battery-Guard 🔋🤖

A Python-based system utility that monitors battery health and uses Google Gemini AI to send smart, contextual notifications.

## Features

- **Real-time Monitoring**: Uses `psutil` to poll hardware battery data.
- **State Management**: Implements logic flags to prevent notification spam.
- **AI-Powered Alerts**: Integrates Gemini 1.5 Flash for unique, dynamic warnings.
- **Secure**: Uses `.env` for API key protection.

## Prerequisites

You will need:

1. Python 3.x installed.
2. A Google AI Studio API Key.
