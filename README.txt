=============
 pelicanizer
=============

Pelicanizer is a webserver that tracks and renders multiple branches of
a git repo for a pelican project.

Features
========

(These are planned, not yet implemented.)

- Integrates with github.
- Creates new virtualhosts whenever new branches are discovered.
- Virtual hosts have an unguessable name:

  + Schema: ``${BRANCH_SECRET}.staging.${SITE}``
  + Example: ``tkjgvzqdyeo.staging.example.com``

- HTTPS everywhere, HTTP redirected. Automatic `letsencrypt` registration.
- The ``production`` git branch determines the root site contents at: ``${SITE}``
- A status site is available at: ``${STATUS_SECRET}.status.${SITE}``
- The ``staging.${SITE}`` and ``status.${SITE}`` sub-sites do not respond
  to requests to prevent remote fingerprinting of the server software.



