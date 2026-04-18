# CLI_toolkit

## Overview
This repository provides a small collection of reusable command-line utilities designed to simplify the development of structured CLI applications in Python.
These tools aim to simplify and abstract elements of CLI-app designing and are designed to be easy to integrate.

The toolkit is growing currently includes:
	•	InputHandler: for parsing and validating user input, supporting standard responses and command-style interactions.
	•	EncryptionManager: for handling RSA-based key generation, secure storage, and encryption/decryption of sensitive data.

## Contents

### InputHandler
This standardises how user input is processed in a CLI environment. It distinguishes between normal input and command tokens (e.g. :help).
It validates responses against predefined constraints (i.e. a list of accepted responses or types of inputs) and routes recognised commands to their associated functions.

It is particularly useful for:
	•	Building interactive CLI workflows
	•	Enforcing allowed responses or input types
	•	Centralising command logic

### EncryptionManager
This encapsulates RSA-based encryption workflows using the Python cryptography library. 
It supports generating and storing key pairs, loading keys from disk, and encrypting/decrypting sensitive values such as passwords.
This lightweight tool is a foundation and NOT designed for ensuring secure sharing or advanced cryptographic purposes.

It is designed for:
	•	Secure local credential handling using password-encrypted private keys.
	•	Protecting secrets at rest using password-encrypted private keys
	•	Abstracting low-level cryptographic operations behind a simple interface
	
### Notes:
These utilities are intentionally lightweight and are not intended to replace full-featured frameworks. 
Instead, they provide a foundation for building custom CLI workflows.

Version 1.0
Author: Jaycee Kennett 2026

