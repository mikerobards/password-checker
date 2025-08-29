# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based password security checker that uses the HaveIBeenPwned API to check if passwords have been compromised in known data breaches. The application implements k-anonymity by sending only the first 5 characters of a SHA-1 hashed password to the API, ensuring the full password is never transmitted.

## Architecture

**Single File Application**: `checkmypass.py` - Contains all functionality including API interaction, password hashing, and command-line interface.

**Key Functions**:
- `request_api_data(query_char)`: Makes API requests to HaveIBeenPwned with first 5 chars of SHA-1 hash
- `pwned_api_check(password)`: Hashes password with SHA-1, queries API, and checks for matches
- `main(args)`: Processes multiple passwords and displays results

**Security Approach**: Uses SHA-1 hashing with k-anonymity - only first 5 characters of hash are sent to API, remaining characters are matched locally from API response.

## Usage

Run the password checker from command line:
```bash
python checkmypass.py <password1> <password2> ...
```

## Dependencies

- `requests`: For API calls to HaveIBeenPwned
- `hashlib`: For SHA-1 password hashing (built-in)
- `sys`: For command-line arguments (built-in)

## API Integration

Uses HaveIBeenPwned Passwords API v3:
- Endpoint: `https://api.pwnedpasswords.com/range/{first5HashChars}`
- Returns list of hash suffixes with breach counts
- No authentication required