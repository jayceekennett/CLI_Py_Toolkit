# README.md

## EncryptionManager
EncryptionManager handles RSA-based encryption workflows for CLI applications.
It can generate a public/private key pair, securely store them on disk (with the private key protected by a password).
This password is not stored in the CLI environment and the RSA keys are serialised to PEM files.
Once keys are available, the public key to encrypt brief sensitive input (e.g. a password) the private key is used to decrypt it.
EncryptionHandler encapsulates key management/encryption/decryption, seperating it from other CLI logic.

### NOTE:
This lightweight tool is a foundation and NOT designed for ensuring secure sharing or advanced cryptographic purposes.
It is not intended to replace full-featured frameworks. Note: tool does not support the recovery of data if the private key password is lost.


Author: Jaycee Kennett 2026