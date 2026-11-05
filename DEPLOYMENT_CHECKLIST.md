# Deployment and App Store checklist

## Hosting
- [ ] Create a Railway project (or choose AWS).
- [ ] Connect the GitHub repository.
- [ ] Provision managed PostgreSQL.
- [ ] Set `DJANGO_SECRET_KEY` to a unique random secret.
- [ ] Set `DJANGO_DEBUG=False`.
- [ ] Set `DJANGO_ALLOWED_HOSTS` to the assigned API hostname.
- [ ] Set `CSRF_TRUSTED_ORIGINS` to the HTTPS API origin.
- [ ] Set `DATABASE_URL` from the managed PostgreSQL service.
- [ ] Deploy and verify `/health/`.
- [ ] Configure automated database backups and retention.
- [ ] Configure domain, HTTPS, logs, alerts and recovery procedures.

## Mobile release
- [ ] Replace local API URL with production HTTPS API URL.
- [ ] Connect all screens to live API data; remove demo balances and sample transactions.
- [ ] Complete add/edit/delete transaction and account workflows.
- [ ] Complete transfer workflow and verify balances.
- [ ] Add refresh-token renewal, logout and session-expiry handling.
- [ ] Add app icon, launch screen, screenshots and store descriptions.
- [ ] Add privacy policy URL, terms URL and support contact.
- [ ] Add account deletion workflow and disclose financial data collection.
- [ ] Test on real iOS and Android devices.
- [ ] Configure Android signing key and build AAB.
- [ ] Configure Apple certificates/profiles and App Store Connect.
- [ ] Submit builds for store review.

## Required user-owned access
- Hosting provider account and project permission.
- GitHub repository access (if deploying from GitHub).
- Apple Developer Program membership for App Store distribution.
- Google Play Console developer account for Play Store distribution.

Never send passwords, private keys, signing certificates or recovery codes in chat.
